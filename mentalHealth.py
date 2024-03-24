import random
import os
from openai import OpenAI


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

affirmations = [
    "You are valued", 
    "Your live matters",
    "It's okay to not be okay. Take your time to heal.",
    "You are stronger than you think and capable of overcoming challenges.",
    "You're doing great.",
    "It's important to take care of yourself",
    "You deserve to feel good."
]


def get_affirmation():
    return random.choice(affirmations)

def get_mindfulness_exercise():
    return random.choice(mindfulness_exercises)

def ask_bot(question):
   
    message = {"role": "user", "content": question}
    
 
    model = "gpt-3.5-turbo"
    
 
    response = client.chat.completions.create(
        model=model,
        messages=[message],
        stream=True
    )

    response_content = next(response).choices[0].delta.content
    
    return response_content.strip()



if __name__ == "__main__":
    print("Welcome to the Mental Health Support Bot.")
    print("Type 'affirmation' for a positive affirmation or ask any question.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Thank you for chatting. Take care of yourself!")
            break
        elif user_input.lower() == 'affirmation':
            print("Bot:", get_affirmation())
        else:
            bot_answer = ask_bot(user_input)
            print("Bot:", bot_answer)
