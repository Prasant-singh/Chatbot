# from flask import Flask, render_template, request, jsonify
# from chatbot import chatbot  # Import your chatbot class

# app = Flask(__name__)

# # Initialize the chatbot
# chat = chatbot()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_response', methods=['POST'])
# def get_response():
#     user_message = request.json['message']
    
#     # Process the user's message using your chatbot logic
#     chat.input_quest = user_message
#     chat.quest = chat.remove_punctuation(chat.input_quest)
    
#     # Get the response from your chatbot
#     response = chat.process_input()
    
#     return jsonify({'response': response})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, jsonify
from chatbot import get_chatbot_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    response = get_chatbot_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)