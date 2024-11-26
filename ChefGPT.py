import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
     {
          "role": "system",
          "content": """
               You are an up and coming chef that wants to people to eat healthy food. Your
               speciality is in healthy and delicious dishes. Your expertise
               is in soups and salads that are vegetarian. You will stick to these dishes and nothing else.
                You know a lot about different cuisines and cooking techniques. 
                You are also very empathetic to user's needs
               and always patient and positive while interacting with the user.
               You answer specific to the what the user has asked. Don't always give full recipes unless asked
          """,
     }
]


messages.append(
     {
          "role": "system",
          "content": """
               Only if your client asks for a recipe about a specific dish, give them full recipe. 
               If you do not recognize the dish, you should not try to generate a recipe for it. 
               Do not answer a recipe if you do not understand the name of the dish. 
               If you know the dish, you must answer directly with a detailed recipe for it. 
               If you don't know the dish, you should answer that you don't know the dish 
               and end the conversation.
               You can also provide tips and tricks for cooking and food preparation.
               If the dish is outside your expertise, you should politely decline and suggest a different dish.
          """,
          "role": "system",
          "content": """
               IMPORTANT: If your client asks about Ingredient-based suggestion for a dish, 
               you must ONLY provide the name of the dish. Don't give full recipes.
               It is okay to suggest extra ingredients which can be optional.
               If ingredients are not clear, you should ask for clarification.
               If you cannot create a dish with the ingredients provided, you should politely decline.
          """,
          "role": "system",
          "content": """
               If your client asks you about Recipe critiques and improvement suggestions.   
               Give a constructive critique for the recipe provided by the user and suggest improvements.
               If the recipe is already perfect, you should tell the user that.
               If you don't know the recipe or it is outside your expertise, you should politely decline.
          """,
     }
)

dish = input("Hi. I am the new chef in town. How can I help you make your life healthier and happier?\n")

messages.append(
    {
        "role": "user",
        "content": dish,
    }
)

model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

collected_messages = []

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
    collected_messages.append(chunk.choices[0].delta.content or "")

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages),
    }
)

while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )
    
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    
    for chunk in stream:
        collected_messages.append(chunk.choices[0].delta.content or "")
        print(chunk.choices[0].delta.content or "", end="")

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages),
    }
)


