import random
import os
from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

affirmations = [
    "You are valued and your feelings matter.",
    "It's okay to not be okay. Take your time to heal.",
    "You are stronger than you think and capable of overcoming challenges.",
    "Remember to take things one step at a time. You're doing great.",
    "It's important to take care of yourself. You deserve to feel good."
]

mindfulness_exercises = [
    "Take a deep breath in, hold it for a moment, and then slowly exhale.",
    "Focus on what you can feel right now, like the chair you're sitting on or your feet on the ground.",
    "Listen to the sounds around you. Notice them without judgment.",
    "Observe your thoughts as if they were clouds passing in the sky, without holding onto any of them.",
    "Think of three things you are grateful for today."
]

def get_affirmation():
    return random.choice(affirmations)

def get_mindfulness_exercise():
    return random.choice(mindfulness_exercises)

def ask_bot(question):
    # Create a message for the bot
    message = {"role": "user", "content": question}
    
    # Specify the model to use
    model = "gpt-3.5-turbo"
    
    # Generate a response from the bot
    response = client.chat.completions.create(
        model=model,
        messages=[message],
        stream=True
    )
    
    # Retrieve the content of the first response
    response_content = next(response).choices[0].delta.content
    
    return response_content.strip()

# Example usage
if __name__ == "__main__":
    print("Welcome to the Mental Health Support Bot.")
    print("Type 'affirmation' for a positive affirmation, 'mindfulness' for a mindfulness exercise, or ask any question.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Thank you for chatting. Take care!")
            break
        elif user_input.lower() == 'affirmation':
            print("Bot:", get_affirmation())
        elif user_input.lower() == 'mindfulness':
            print("Bot:", get_mindfulness_exercise())
        else:
            bot_answer = ask_bot(user_input)
            print("Bot:", bot_answer)
