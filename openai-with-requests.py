import requests

# Set your OpenAI API key
api_key = "sk-O8BgGWTijWIiE2WP3UoLUeBIgbV-uLXyapN4IcP3oTT3BlbkFJIN4LTNyee_P3hqx49oAEHSkkWAQaIoxrzxTfnD06QA"

def chat_with_openai(user_input):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        answer = response.json()['choices'][0]['message']['content']
        return answer
    except requests.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Welcome to OpenAI Chat bot. Type 'end', 'quit', 'exit', or 'bye' to stop the conversation. Chat with OpenAI for answers.")
    
    while True:
        print(" ")
        user_input = input("You: ")
        if user_input.lower() in {'end', 'quit', 'exit', 'bye'}:
            print("Conversation ended.")
            break
        response = chat_with_openai(user_input)
        print(f"Bot: {response}")
