print("Bot : Hello! I am your mental health companion.. How can I assist you today?")

while True:
    user=input("You : ").lower()

    if "sad" in user or "depressed" in user:
        print("Bot : I'm sorry to hear that you're feeling this way. It's important to talk about it. Would you like to share more about what's been bothering you?")

    elif "happy" in user or "good" in user:
        print("Bot : That's great to hear! It's always nice to have good days. What has been making you feel happy?")

    elif "angry" in user or "frustrated" in user:
        print("Bot : Anger is a natural emotion. It's okay to feel that way sometimes. Would you like to talk about what's making you feel angry?")

    elif "anxious" in user or "nervous" in user:
        print("Bot : Anxiety can be tough to deal with. It's good that you're reaching out. Can you tell me more about what's making you feel anxious?")    

    elif "stressed" in user or "overwhelmed" in user:
        print("Bot : Stress can be really challenging. It's important to take care of yourself. What do you think is causing your stress?")

    elif "quit" in user or "exit" in user or "bye" in user:
        print("Bot : Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!")
        break

    else:
        print("Bot : I'm here to listen. Please tell me more about how you're feeling or what you would like to talk about.")



    