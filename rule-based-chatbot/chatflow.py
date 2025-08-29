
responses={
    "sad": "I'm sorry to hear that you're feeling this way. It's important to talk about it. Would you like to share more about what's been bothering you?",
    "depress": "I'm sorry to hear that you're feeling this way. It's important to talk about it. Would you like to share more about what's been bothering you?",
    "happy": "That's great to hear! It's always nice to have good days. What has been making you feel happy?",
    "good": "That's great to hear! It's always nice to have good days. What has been making you feel happy?",
    "angry": "Anger is a natural emotion. It's okay to feel that way    sometimes. Would you like to talk about what's making you feel angry?",
    "frustrate": "Anger is a natural emotion. It's okay to feel that way sometimes. Would you like to talk about what's making you feel angry?",
    "anxious": "Anxiety can be tough to deal with. It's good that you're reaching out. Can you tell me more about what's making you feel anxious?",
    "nervous": "Anxiety can be tough to deal with. It's good that you're reaching out. Can you tell me more about what's making you feel anxious?",
    "stress": "Stress can be really challenging. It's important to take care of yourself. What do you think is causing your stress?",
    "overwhelm": "Stress can be really challenging. It's important to take care of yourself. What do you think is causing your stress?",
    "quit": "Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!",
    "exit": "Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!",
    "bye": "Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!"
}



print("Bot : Hello! I am your mental health companion.. How can I assist you today?")

while True:
    user=input("You : ").lower()

    if "quit" in user:
        print("Bot :",responses["bye"])
        break
    
    elif "exit" in user:
        print("Bot :",responses["bye"])
        break

    elif "bye" in user:
        print("Bot :",responses["bye"])
        break

    response_found=False
    for keyword in responses:
        if keyword in user:
            print("Bot :",responses[keyword])
            response_found=True
            break

    if not response_found:
        print("Bot : I'm here to listen. Can you tell me more about how you're feeling?")