from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'YOUR_API_KEY'

conversation_history = []

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history
    user_input = request.json.get('input')
    conversation_history.append(f"User: {user_input}")
    prompt = "\n".join(conversation_history)
    response = chat_with_gpt(prompt)
    conversation_history.append(f"ChatGPT: {response}")
    return jsonify({'response': response})

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)
