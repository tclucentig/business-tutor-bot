import streamlit as st
import google.generativeai as genai

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
# or leave it empty to force them to enter one (not recommended for students).
# Example: HARDCODED_KEY = "AIzaSy..."
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
        response_text = None
        last_error = None
        
        # List of models to try in case of 404 errors
        candidate_models = [
            "gemini-1.5-flash",
            "gemini-1.5-flash-001",
            "gemini-1.5-flash-002",
            "gemini-1.5-pro",
            "gemini-pro"
        ]

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

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Try models one by one
                    for model_name in candidate_models:
                        try:
                            # print(f"Trying model: {model_name}") 
                            model = genai.GenerativeModel(model_name)
                            response = model.generate_content(full_prompt)
                            response_text = response.text
                            break # It worked! Exit loop.
                        except Exception as e:
                            last_error = e
                            continue # Try next model

                    if response_text:
                        st.markdown(response_text)
                        st.session_state.messages.append({"role": "assistant", "content": response_text})
                    else:
                        st.error(f"Unable to connect to AI. Last Error: {str(last_error)}")
                        st.info("Troubleshooting: Ensure your API Key is valid and has 'Generative Language API' enabled in Google Cloud Console.")
                        
        except Exception as e:
            st.error(f"Configuration Error: {str(e)}")

# Display Message History
for msg in st.session_state.messages:
    if msg["role"] != "user" and msg != st.session_state.messages[-1]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
