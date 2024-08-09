import requests


LLMFOUNDRY_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im11dGh1a3VtYXIucGFuY2hhYmVrYXNhbkBzdHJhaXZlLmNvbSJ9.uiwWDBAUFxkHaLY4duukUT0h94izwJH6rktK5mksef0"


def chat_with_llm(user_input):
    response = requests.post(
        "https://llmfoundry.straive.com/azure/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-05-01-preview",
        headers={"Authorization": f"Bearer {LLMFOUNDRY_TOKEN}:Muthu_bot"},
        json={"messages": [{"role": "user", "content": user_input}]},
    )
    
    if response.status_code == 200:
        response_json = response.json()
        answer = response_json['choices'][0]['message']['content']
        return answer
    else:
        return f"Error: {response.status_code} - {response.text}"
    
if __name__ == "__main__":
    print("Welcome to LLM Chat bot and type 'end','quit','exit','bye' to stop the convesation, chat with LLM for answer")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in {'end','quit','exit','bye'}:
            print("Conversation eneded")
            break
        response = chat_with_llm(user_input)
        print(f"Bot: {response}")   
    


