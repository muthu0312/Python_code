import streamlit as st
import requests

# Set your OpenAI API key
api_key = "sk-VMq3LH7OC2K8BA6hDOLpwQID6n4u3J7l9ETumcCz_TT3BlbkFJgEY1JkHcPf6SS8aeATQcgh76VuO46vi52oltuIEy4A"

def chat_with_openai(messages):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        answer = response.json()['choices'][0]['message']['content']
        return answer.strip()
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    st.title("OpenAI Chatbot")

    if 'messages' not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.write(f"You: {message['content']}")
        elif message['role'] == 'assistant':
            st.write(f"Bot: {message['content']}")

    user_input = st.text_input("You: ", value="", placeholder="", key='text_input')

    if st.button("Send"):
        if user_input:  # Only proceed if there's new input
            st.session_state.messages.append({'role': 'user', 'content': user_input})
            response = chat_with_openai(st.session_state.messages)
            st.session_state.messages.append({'role': 'assistant', 'content': response})
            st.session_state.user_input = ""  # Properly reset the input

    if st.button("End Conversation"):
        st.write("Conversation ended.")
        st.session_state.messages.clear()

if __name__ == "__main__":
    main()
