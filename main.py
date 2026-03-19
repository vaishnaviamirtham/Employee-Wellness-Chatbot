from flask import Flask, request, jsonify
from flask import render_template
app = Flask(__name__)

def chatbot_response(user_input, user_name):
    user_input = user_input.lower()
    #name = str(input("What is your name? "))
    if "overwhelmed" in user_input or "stressed" in user_input:
        return f"Hello {user_name}, I can understand you. Work can feel heavy sometimes. Taking a short break or walk might help. Would you like me to share our Employee Assistance Program resources?"
    elif "sad" in user_input or "depressed" in user_input:
        return f"Hello {user_name}, I'm really sorry you're feeling this way. You're not alone. Talking to someone you trust or reaching out to HR/EAP could help."
    else:
        return f"Thanks for sharing, {user_name}. I'm here to listen and can point you to wellness resources if you'd like."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():



    data = request.get_json(silent=True)
    #if "name" in data:
     #   session["name"] = data["name"]
    if not data or "message" not in data or "name" not in data:
        return jsonify({"message": "Send JSON like {'name':'text','message': 'text'}"}), 400
    user_name = data.get("name", "Friend")
    user_input = data["message"]

    response = chatbot_response(user_input, user_name)

    #Add name in response
    #final_response = f"{user_name}, {response}"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
