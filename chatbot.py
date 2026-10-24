import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="DEVA AI",
    page_icon="",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }

    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: #00d4ff;
    }

    .subtitle {
        text-align: center;
        color: #aaaaaa;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .user-message {
        background-color: #1f6feb;
        color: white;
        padding: 12px 18px;
        border-radius: 18px;
        margin: 10px 0;
        text-align: right;
    }

    .ai-message {
        background-color: #262730;
        color: white;
        padding: 12px 18px;
        border-radius: 18px;
        margin: 10px 0;
        text-align: left;
    }

    .footer {
        text-align: center;
        color: #777777;
        margin-top: 40px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    '<div class="title"> DEVA AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your intelligent local AI assistant powered by Ollama</div>',
    unsafe_allow_html=True
)


# Sidebar
with st.sidebar:
    st.header(" AI Settings")

    model = st.selectbox(
        "Choose Model",
        ["llama3.2"]
    )

    st.markdown("---")

    st.info(
        " Ask DEVA anything!\n\n"
        "• Explain concepts\n"
        "• Write code\n"
        "• Solve problems\n"
        "• Generate ideas"
    )


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-message">
                👤 <b>You:</b><br>
                {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="ai-message">
                 <b>DEVA AI:</b><br>
                {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


# User input
prompt = st.chat_input("Ask Nova something")


# Generate response
if prompt:

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    st.markdown(
        f"""
        <div class="user-message">
            👤 <b>You:</b><br>
            {prompt}
        </div>
        """,
        unsafe_allow_html=True
    )

    # AI response
    with st.spinner(" DEVA is thinking..."):

        response = ollama.chat(
            model=model,
            messages=st.session_state.messages
        )

        answer = response["message"]["content"]

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    # Display AI response
    st.markdown(
        f"""
        <div class="ai-message">
             <b>DEVA AI:</b><br>
            {answer}
        </div>
        """,
        unsafe_allow_html=True
    )


# Footer
st.markdown(
    '<div class="footer"> DEVA AI • Powered by Ollama & Streamlit</div>',
    unsafe_allow_html=True
)