"""CodeAlpha Python Internship - Task 4: Basic Rule-Based Chatbot"""
from datetime import datetime


def get_response(user_input):
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif "your name" in text:
        return "I'm CodeBot, a simple Python chatbot."
    elif "time" in text:
        return f"The time is {datetime.now():%I:%M %p}."
    elif "help" in text:
        return "Try: hello, how are you, what's your name, time, or bye."
    elif text in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Type 'help' for options."


def main():
    print("CodeBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("CodeBot:", reply)
        if user_input.lower().strip() in ("bye", "goodbye", "exit"):
            break


if __name__ == "__main__":
    main()
