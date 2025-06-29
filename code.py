import spacy
import datetime

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define some intents and responses
intent_responses = {
    "greeting": ["Hi there!", "Hello!", "Hey! How can I help you?","Hii","how are you"],
    "goodbye": ["Bye!", "Goodbye!", "See you later!"],
    "time": [f"The current time is {datetime.datetime.now().strftime('%H:%M')}"],
    "date": [f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"],
    "weather": ["I'm not connected to a weather service, but it looks nice outside!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"]
}

def get_intent(user_input):
    doc = nlp(user_input.lower())

    # Rule-based intent recognition
    if any(token.lemma_ in ["hi", "hello", "hey"] for token in doc):
        return "greeting"
    elif any(token.lemma_ in ["bye", "goodbye", "see you"] for token in doc):
        return "goodbye"
    elif "time" in user_input.lower():
        return "time"
    elif "date" in user_input.lower() or "day" in user_input.lower():
        return "date"
    elif "weather" in user_input.lower():
        return "weather"
    elif "thank" in user_input.lower():
        return "thanks"
    else:
        return "unknown"

def chatbot_response(user_input):
    intent = get_intent(user_input)
    if intent in intent_responses:
        return intent_responses[intent][0]
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

# Main chatbot loop
def chat():
    print("🤖 Chatbot is ready! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye! 👋")
            break
        response = chatbot_response(user_input)
        print(f"Bot: {response}")

# Start chatting
if __name__ == "__main__":
    chat()
