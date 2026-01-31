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
# You can hardcode the API key here if you want students to use yours.
# If empty, students/teacher must enter it in the sidebar.
HARDCODED_KEY = "AIzaSyAeK_ntcfGUpuhF3OQihUfZ08ZqS9RIUsM" 

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
            st.caption("Get a free key at: https://aistudio.google.com/app/apikey")

    st.divider()
    
    # Teacher Dashboard in Sidebar
    with st.expander("👨‍🏫 Teacher Dashboard"):
        pin = st.text_input("Enter PIN", type="password")
        if pin == TEACHER_PIN:
            st.success("Unlocked")
            st.info(f"Loaded Content: {len(PERMANENT_SYLLABUS)} characters")
        elif pin:
            st.error("Incorrect PIN")

# --- HELPER: RETRY LOGIC WITH FEEDBACK ---
def generate_with_retry(model, prompt, status_container, retries=3):
    for i in range(retries):
        try:
            return model.generate_content(prompt)
        except Exception as e:
            # Check for Rate Limit (429)
            if "429" in str(e):
                if i < retries - 1:
                    wait_time = 5 * (i + 1) # Wait 5s, 10s...
                    status_container.warning(f"🚦 Traffic jam... waiting {wait_time}s before retry.")
                    time.sleep(wait_time)
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
            # 1. Clean the key (remove spaces)
            clean_key = api_key.strip()
            genai.configure(api_key=clean_key)
            
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
            # Added 2.0-flash-exp (often works when 1.5 is quota limited) and 8b (lightweight)
            candidate_models = [
                "gemini-2.0-flash-exp",
                "gemini-1.5-flash",
                "gemini-1.5-flash-002",
                "gemini-1.5-flash-8b",
                "gemini-1.5-pro",
                "gemini-pro"
            ]
            
            # Try to fetch models available to this specific key to prioritize them
            try:
                available_on_key = [m.name.replace("models/", "") for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                if available_on_key:
                    # Put available models at the start of the list
                    candidate_models = available_on_key + candidate_models
            except Exception:
                pass 

            # Remove duplicates
            candidate_models = list(dict.fromkeys(candidate_models))

            response = None
            last_error = None
            success_model = None

            with st.chat_message("assistant"):
                # Use a status container to show progress/retries
                with st.status("Connecting to AI...", expanded=True) as status:
                    # Loop through models until one works
                    for model_name in candidate_models:
                        try:
                            # status.write(f"Trying model: {model_name}...")
                            model = genai.GenerativeModel(model_name)
                            # Attempt generation with retry
                            result = generate_with_retry(model, full_prompt, status)
                            response = result
                            success_model = model_name
                            status.update(label=f"Connected! ({model_name})", state="complete", expanded=False)
                            break # Success! Exit loop
                        except Exception as e:
                            last_error = e
                            error_str = str(e).lower()
                            # If it's a 404 (Not Found) or 400 (Bad Request), try next model immediately
                            if "404" in error_str or "not found" in error_str or "400" in error_str:
                                continue
                            # If it's a 429 (Quota), we TRY the next model too, because different models sometimes have different quotas!
                            if "429" in error_str:
                                status.write(f"{model_name} busy, trying next...")
                                continue
                            continue

                    if response:
                        st.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                    else:
                        status.update(label="Connection Failed", state="error")
                        if last_error and "429" in str(last_error):
                            st.error("🚦 Daily Quota Exceeded for ALL models. Please use a fresh API Key.")
                        else:
                            st.error(f"Unable to connect. Last Error: {str(last_error)}")
                            st.caption("Troubleshooting: Ensure your API Key is valid and has 'Generative Language API' enabled.")
                        
        except Exception as e:
            st.error(f"Configuration Error: {str(e)}")

# Display Message History
for msg in st.session_state.messages:
    if msg["role"] != "user" and msg != st.session_state.messages[-1]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
