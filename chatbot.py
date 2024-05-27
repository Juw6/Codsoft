def chatbot():
    print("Hello! I am a chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hi there! What can I do for you?")
        elif user_input in ["how are you" , "how are you doing"]:
            print("Chatbot: I'm just a bot, but thanks for asking! How can I help you?")
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I am a simple chatbot created to help you.")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day.")
        elif user_input in["tell me a joke"]:
            print("Chatbot: Sure! Here's one for you- Why couldn't the bicycle stand up by itself?  Because it was two-tired!")    
        elif user_input in ["thanks", "thank you"]:
            print("Chatbot: It's always a pleasure to help you.")            
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you ask something else?")
            
if __name__ == "__main__":
    chatbot()
