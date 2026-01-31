import streamlit as st
import google.generativeai as genai
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Mr. Thiago's Bot", page_icon="🎓", layout="wide")

# --- DEFAULT SYLLABUS ---
DEFAULT_SYLLABUS = """
CAMBRIDGE AS LEVEL BUSINESS (9609) - SYLLABUS SUMMARY

1.1 ENTERPRISE
- The nature of business activity: The purpose of business is to combine factors of production (Land, Labour, Capital, Enterprise).
- The role of the entrepreneur: Risk-taking, innovation, organization.
- Social enterprise: Businesses with primarily social objectives (Triple Bottom Line: Profit, People, Planet).

[TEACHER: PASTE YOUR 100 PAGES HERE]
"""

# --- TEACHER PIN ---
TEACHER_PIN = "3596"

# --- SIDEBAR SETTINGS ---
with st.sidebar:
    st.title("⚙️ Settings")
    
    # API Key Input
    api_key = st.text_input("Google API Key", type="password", placeholder="Paste AIza... key here")
    
    # Mode Selection
    mode = st.radio("Select Mode", ["Study Assistant", "Exam Marker", "Teacher Dashboard"])
    
    st.divider()
    st.caption("Powered by Gemini AI")

# --- INITIALIZE SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "syllabus" not in st.session_state:
    st.session_state.syllabus = DEFAULT_SYLLABUS

# --- FUNCTIONS ---
def get_gemini_response(prompt, context, mode_type):
    if not api_key:
        return "⚠️ Please enter your Google API Key in the sidebar."
    
    try:
        genai.configure(api_key=api_key)
        # Try standard flash model, then pro if flash fails
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if mode_type == "study":
            system_instruction = f"""
            You are a Cambridge AS Level Business (9609) Tutor.
            CONTEXT: {context}
            INSTRUCTIONS:
            - If asking for a definition: Explain CLEARLY based on Context.
            - If asking for an essay answer: Provide STRUCTURE and HINTS only. Do NOT write the full essay.
            - Use ONLY the provided Context.
            """
        else: # marker
            system_instruction = f"""
            You are a Cambridge Business Examiner.
            CONTEXT: {context}
            TASK: Mark the student answer.
            Use [K], [App], [An], [Eval] annotations.
            """
            
        chat = model.start_chat(history=[])
        response = chat.send_message(f"{system_instruction}\n\nUSER QUERY: {prompt}")
        return response.text
        
    except Exception as e:
        return f"Error: {str(e)}"

# --- MAIN INTERFACE ---

if mode == "Teacher Dashboard":
    st.header("👨‍🏫 Teacher Dashboard")
    pin = st.text_input("Enter PIN to edit Syllabus", type="password")
    
    if pin == TEACHER_PIN:
        st.success("Access Granted")
        new_syllabus = st.text_area("Syllabus Content (Knowledge Base)", value=st.session_state.syllabus, height=400)
        if st.button("Save Changes"):
            st.session_state.syllabus = new_syllabus
            st.success("Syllabus updated!")
    elif pin:
        st.error("Incorrect PIN")
    else:
        st.info("Enter PIN to view/edit source material.")

elif mode == "Study Assistant":
    st.header("📚 Study Assistant")
    st.caption("Ask questions about the syllabus. I'll help you structure your answers.")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask a question..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_gemini_response(prompt, st.session_state.syllabus, "study")
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

elif mode == "Exam Marker":
    st.header("✅ Exam Marker")
    st.caption("Paste a question and your answer to get marked.")
    
    q = st.text_input("Question")
    marks = st.selectbox("Max Marks", [1, 2, 3, 5, 8, 12, 20])
    ans = st.text_area("Your Answer", height=150)
    
    if st.button("Mark Answer"):
        if q and ans:
            with st.spinner("Marking..."):
                prompt = f"Question: {q}\nStudent Answer: {ans}\nMax Marks: {marks}"
                response = get_gemini_response(prompt, st.session_state.syllabus, "marker")
                st.markdown("### Feedback")
                st.write(response)
        else:
            st.warning("Please fill in both Question and Answer.")
