
responses={
    "sad": "I'm sorry to hear that you're feeling this way. It's important to talk about it. Would you like to share more about what's been bothering you?",
    "depress": "I'm sorry to hear that you're feeling this way. It's important to talk about it. Would you like to share more about what's been bothering you?",
    "happy": "That's great to hear! It's always nice to have good days. What has been making you feel happy?",
    "good": "That's great to hear! It's always nice to have good days. What has been making you feel happy?",
    "angry": "Anger is a natural emotion. It's okay to feel that way sometimes. Would you like to talk about what's making you feel angry?",
    "frustrate": "Anger is a natural emotion. It's okay to feel that way sometimes. Would you like to talk about what's making you feel angry?",
    "anxious": "Anxiety can be tough to deal with. It's good that you're reaching out. Can you tell me more about what's making you feel anxious?",
    "nervous": "Anxiety can be tough to deal with. It's good that you're reaching out. Can you tell me more about what's making you feel anxious?",
    "stress": "Stress can be really challenging. It's important to take care of yourself. What do you think is causing your stress?",
    "overwhelm": "Stress can be really challenging. It's important to take care of yourself. What do you think is causing your stress?",
    "quit": "Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!",
    "exit": "Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!",
    "bye": "Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!"
}

track_mood={"sad":0,"depress":0,"happy":0,"good":0,"angry":0,"frustrate":0,"anxious":0,"nervous":0,"stress":0,"overwhelm":0}


print("Bot : Hello! I am your mental health companion.. How can I assist you today?")

with open("chat_history.txt","a") as f:
    while True:
        user=input("You : ").lower()

        if "quit" in user:
            print("Bot : ",responses["bye"])
            break
    
        elif "exit" in user:
            print("Bot : ",responses["bye"])
            break

        elif "bye" in user:
            print("Bot : ",responses["bye"])
            break
        
        bot_reply=""
        response_found=False
        for keyword in responses:
            if keyword in user:

                if keyword in ["sad","depress","angry","frustrate","anxious","nervous","stress","overwhelm"]:
                    if track_mood[keyword]>=3:
                        bot_reply="It seems like you're going through a tough time. It might be helpful to talk to a mental health professional who can provide you with the support you need."
                        print("Bot : "+bot_reply)
                        response_found=True
                        break

                elif keyword in ["happy","good"]:
                    if track_mood[keyword]>=3:
                        bot_reply="I'm glad to hear that you're feeling good! Keep doing what makes you happy and take time to appreciate the positive moments in your life."
                        print("Bot : "+bot_reply)
                        response_found=True
                        break

                bot_reply=responses[keyword]
                print("Bot : "+bot_reply)
                response_found=True
                track_mood[keyword]+=1
                break

        if not response_found:
            bot_reply="I'm here to listen. Can you tell me more about how you're feeling?"
            print("Bot : "+bot_reply)

        f.write("You : "+user+"\n")
        f.write("Bot : "+bot_reply+"\n")