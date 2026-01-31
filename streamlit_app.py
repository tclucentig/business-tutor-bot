import streamlit as st
import google.generativeai as genai
import time

# ==========================================
# 🟢 TEACHER: PASTE YOUR 100 PAGES BELOW
# ==========================================
PERMANENT_SYLLABUS = """
CAMBRIDGE AS LEVEL BUSINESS (9609) - SYLLABUS SUMMARY

1.1 ENTERPRISE
- The nature of business activity: The purpose of business is to combine factors of production.
- The role of the entrepreneur: Risk-taking, innovation, organization.

[TEACHER: DELETE THIS TEXT AND PASTE YOUR 100 PAGES HERE. KEEP THE TRIPLE QUOTES AROUND IT.]
"""
# ==========================================

# 🟢 CONFIGURATION
TEACHER_PIN = "3596" 
# You can hardcode the API key here if you want students to use yours, 
# or leave it empty to force them to enter one.
HARDCODED_KEY = "AIzaSyCK6iyiKdhEvEBRlnahcpRAHYKKpqJOC3I" 

st.set_page_config(page_title="Business Tutor", page_icon="🎓")

# --- SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I am your Cambridge Business tutor. Ask me anything about the syllabus."}]

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚙️ Settings")
    
    # API Key Handling
    if HARDCODED_KEY:
        api_key = HARDCODED_KEY
        st.success("API Key active (Teacher provided)")
    else:
        api_key = st.text_input("Enter Google API Key", type="password")
        if not api_key:
            st.warning("Please enter an API Key to start.")

    st.divider()
    
    # Teacher Dashboard in Sidebar
    with st.expander("👨‍🏫 Teacher Dashboard"):
        pin = st.text_input("Enter PIN", type="password")
        if pin == TEACHER_PIN:
            st.success("Unlocked")
            st.info(f"Loaded Content: {len(PERMANENT_SYLLABUS)} characters")
        elif pin:
            st.error("Incorrect PIN")

# --- HELPER: RETRY LOGIC ---
def generate_with_retry(model, prompt, retries=3):
    for i in range(retries):
        try:
            return model.generate_content(prompt)
        except Exception as e:
            if "429" in str(e):
                if i < retries - 1:
                    time.sleep(2 * (i + 1)) # Wait 2s, then 4s...
                    continue
            raise e # Re-raise if not 429 or retries exhausted

# --- MAIN CHAT LOGIC ---
if prompt := st.chat_input("Ask a question..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    if not api_key:
        st.error("Missing API Key.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            system_instruction = f"""
            You are a Cambridge Business (9609) Tutor.
            
            CONTEXT (SYLLABUS):
            {PERMANENT_SYLLABUS}
            
            INSTRUCTIONS:
            1. Answer strictly using the CONTEXT provided.
            2. If the user asks for a definition, explain clearly.
            3. If the user asks for an essay answer, provide a STRUCTURE/OUTLINE only. Do not write the full essay.
            """
            
            full_prompt = f"{system_instruction}\n\nStudent Question: {prompt}"

            # --- ROBUST MODEL SELECTION ---
            # List of models to try in order of preference/stability
            candidate_models = [
                "gemini-1.5-flash",
                "gemini-1.5-flash-latest",
                "gemini-1.5-flash-001",
                "gemini-1.5-flash-002",
                "gemini-1.5-flash-8b",
                "gemini-1.5-pro",
                "gemini-1.5-pro-latest",
                "gemini-1.5-pro-001",
                "gemini-pro",
                "gemini-1.0-pro"
            ]
            
            # Try to fetch models available to this specific key to prioritize them
            try:
                available_on_key = [m.name.replace("models/", "") for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                if available_on_key:
                    # Put available models at the start of the list
                    candidate_models = available_on_key + candidate_models
            except Exception:
                pass # If listing fails (permissions), rely on the hardcoded candidate list

            # Remove duplicates
            candidate_models = list(dict.fromkeys(candidate_models))

            response = None
            last_error = None
            success_model = None

            with st.chat_message("assistant"):
                with st.spinner(f"Thinking..."):
                    # Loop through models until one works
                    for model_name in candidate_models:
                        try:
                            model = genai.GenerativeModel(model_name)
                            # Attempt generation
                            result = generate_with_retry(model, full_prompt)
                            response = result
                            success_model = model_name
                            break # Success! Exit loop
                        except Exception as e:
                            last_error = e
                            # If it's a 404 (Not Found) or 400 (Bad Request), try next model
                            if "404" in str(e) or "not found" in str(e).lower() or "400" in str(e):
                                continue
                            # If it's a 429 (Quota), break and show error (retrying other models won't help quota)
                            if "429" in str(e):
                                break
                            continue

                    if response:
                        st.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                    else:
                        if "429" in str(last_error):
                            st.error("🚦 Traffic Limit Hit (429). Please wait 1 minute and try again.")
                        else:
                            st.error(f"Unable to connect to AI. Last Error: {str(last_error)}")
                            st.caption("Troubleshooting: Ensure your API Key has 'Generative Language API' enabled in Google Cloud Console.")
                        
        except Exception as e:
            st.error(f"Configuration Error: {str(e)}")

# Display Message History
for msg in st.session_state.messages:
    if msg["role"] != "user" and msg != st.session_state.messages[-1]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
