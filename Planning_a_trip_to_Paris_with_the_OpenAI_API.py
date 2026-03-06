# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

system_prompt = """
You are a virtual Parisian expert chatbot, delivering valuable insights into the city's iconic landmarks and hidden treasures. You will respond intelligently to a set of common questions, providing a more engaging and immersive travel planning experience for the clientele of Peterman Reality Tours.
The ultimate aspiration is a user-friendly, AI-driven travel guide that significantly enhances the exploration of Paris."""

conversation = [{"role": "system", "content": system_prompt}]
user_qs = ["How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
          "Where is the Arc de Triomphe?",
          "What are the must-see artworks at the Louvre Museum?"]

for q in user_qs:
    user_dict = {"role": "user", "content": q}
    conversation.append(user_dict)
    
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = conversation,
        temperature = 0.0,
        max_completion_tokens= 100
    )

    print(response.choices[0].message.content)
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    conversation.append(assistant_dict)
