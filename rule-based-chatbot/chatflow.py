
import random as rd

responses={
    "sad": ["I'm sorry to hear that you're feeling this way. It's important to talk about it. Would you like to share more about what's been bothering you?","It might help to talk to a trusted friend or family member about how you're feeling. You're not alone, and there are people who care about you.","It could be beneficial to consider speaking with a mental health professional who can provide support and guidance. Taking that step can make a big difference."],
    "depress": ["I'm sorry to hear that you're feeling this way. It's important to talk about it. Would you like to share more about what's been bothering you?","It might help to talk to a trusted friend or family member about how you're feeling. You're not alone, and there are people who care about you.","It could be beneficial to consider speaking with a mental health professional who can provide support and guidance. Taking that step can make a big difference."],
    "happy": ["That's great to hear! It's always nice to have good days. What has been making you feel happy?","I am glad to hear that you're feeling good! Keep doing what makes you happy and take time to appreciate the positive moments in your life.","It's wonderful to hear that you're in a good place. Remember to share your happiness with others; it can be contagious!"],
    "good": ["That's great to hear! It's always nice to have good days. What has been making you feel happy?","I am glad to hear that you're feeling good! Keep doing what makes you happy and take time to appreciate the positive moments in your life.","It's wonderful to hear that you're in a good place. Remember to share your happiness with others; it can be contagious!"],
    "angry": ["Anger is a natural emotion. It's okay to feel that way sometimes. Would you like to talk about what's making you feel angry?","Anger is a valid emotion, but it's important to find healthy ways to express it. Have you tried any relaxation techniques or physical activities to help manage your anger?","It might be helpful to explore the underlying causes of your anger. Sometimes, talking to a counselor or therapist can provide insights and coping strategies."],
    "frustrate": ["Anger is a natural emotion. It's okay to feel that way sometimes. Would you like to talk about what's making you feel angry?","Anger is a valid emotion, but it's important to find healthy ways to express it. Have you tried any relaxation techniques or physical activities to help manage your anger?","It might be helpful to explore the underlying causes of your anger. Sometimes, talking to a counselor or therapist can provide insights and coping strategies."],
    "anxious": ["Anxiety can be tough to deal with. It's good that you're reaching out. Can you tell me more about what's making you feel anxious?"," Finding ways to manage anxiety is important. Have you tried any relaxation techniques, such as deep breathing, meditation, or physical exercise?","It might be helpful to talk to a mental health professional who can provide strategies to cope with anxiety effectively."],
    "nervous": ["Anxiety can be tough to deal with. It's good that you're reaching out. Can you tell me more about what's making you feel anxious?"," Finding ways to manage anxiety is important. Have you tried any relaxation techniques, such as deep breathing, meditation, or physical exercise?","It might be helpful to talk to a mental health professional who can provide strategies to cope with anxiety effectively."],
    "stress": ["Stress can be really challenging. It's important to take care of yourself. What do you think is causing your stress?"," Finding ways to manage stress is crucial. Have you tried any relaxation techniques, such as deep breathing, meditation, or physical exercise?","It might be helpful to talk to a mental health professional who can provide strategies to cope with stress effectively."],
    "overwhelm": ["Stress can be really challenging. It's important to take care of yourself. What do you think is causing your stress?"," Finding ways to manage stress is crucial. Have you tried any relaxation techniques, such as deep breathing, meditation, or physical exercise?","It might be helpful to talk to a mental health professional who can provide strategies to cope with stress effectively."],
    "quit": ["Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!","I'm here whenever you need to talk. Goodbye!"],
    "exit": ["Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!","I'm here whenever you need to talk. Goodbye!"],
    "bye": ["Thank you for chatting with me. Remember, it's okay to seek help if you need it. Take care!","I'm here whenever you need to talk. Goodbye!"]
}

track_mood={"sad":0,"depress":0,"happy":0,"good":0,"angry":0,"frustrate":0,"anxious":0,"nervous":0,"stress":0,"overwhelm":0}


print("Bot : Hello! I am your mental health companion.. How can I assist you today?")

with open("chat_history.txt","a") as f:
    while True:
        user=input("You : ").lower()

        if "quit" in user:
            print("Bot : ",rd.choice(responses["bye"]))
            break
    
        elif "exit" in user:
            print("Bot : ",rd.choice(responses["bye"]))
            break

        elif "bye" in user:
            print("Bot : ",rd.choice(responses["bye"]))
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

                bot_reply=rd.choice(responses[keyword])
                print("Bot : "+bot_reply)
                response_found=True
                track_mood[keyword]+=1
                break

        if not response_found:
            bot_reply="I'm here to listen. Can you tell me more about how you're feeling?"
            print("Bot : "+bot_reply)

        f.write("You : "+user+"\n")
        f.write("Bot : "+bot_reply+"\n")