from taipy.gui import Gui, State, notify
import openai
import os
import json

import predictionguard as pg
from getpass import getpass

# pg_access_token = getpass("q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E")
os.environ['PREDICTIONGUARD_TOKEN'] = ACCESS_TOKEN
pg.Chat.list_models()
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant that provide clever and sometimes funny responses."
    },
    {
        "role": "user",
        "content": "What's up!"
    },
    {
        "role": "assistant",
        "content": "Well, technically vertically out from the center of the earth."
    },
    {
        "role": "user",
        "content": "Haha. Good one."
    }
]

result = pg.Chat.create(
    model="Neural-Chat-7B",
    messages=messages
)

print(json.dumps(
    result,
    sort_keys=True,
    indent=4,
    separators=(',', ': ')
))
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant that provide clever and sometimes funny responses. You respond with concise responses in only 1 or 2 complete sentences."
    }
]
print('Welcome to the Chatbot! Let me know how can I help you')

while True:
  print('')
  request = input('User' + ': ')
  if request=="Stop" or request=='stop':
      print('Bot: Bye!')
      break
  else:
      messages.append({
          "role": "user",
          "content": request
      })
      response = pg.Chat.create(
          model="Neural-Chat-7B",
          messages=messages
      )['choices'][0]['message']['content'].split('\n')[0].strip()
      messages.append({
          "role": "assistant",
          "content": response
      })
      print('Bot: ', response)

# context = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today? "
# conversation = {
#     "Conversation": ["Who are you?", "Hi! I am GPT-3. How can I help you today?"]
# }

# current_user_message = ""

# client = openai.Client(api_key="q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E")

# def request(state: State, prompt: str) -> str:
#     """
#     Send a prompt to the GPT-3 API and return the response.

#     Args:
#         - state: The current state.
#         - prompt: The prompt to send to the API.

#     Returns:
#         The response from the API.
#     """
#     response = state.client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": f"{prompt}",
#             }
#         ],
#         model="gpt-3.5-turbo",
#     )
#     return response.choices[0].message.content

# def send_message(state: State) -> None:
#     """
#     Send the user's message to the API and update the conversation.

#     Args:
#         - state: The current state.
#     """
#     # Add the user's message to the context
#     state.context += f"Human: \n {state.current_user_message}\n\n AI:"
#     # Send the user's message to the API and get the response
#     answer = request(state, state.context).replace("\n", "")
#     # Add the response to the context for future messages
#     state.context += answer
#     # Update the conversation
#     conv = state.conversation._dict.copy()
#     conv["Conversation"] += [state.current_user_message, answer]
#     state.conversation = conv
#     # Clear the input field
#     state.current_user_message = ""

# page = """
# <|{conversation}|table|show_all|width=100%|>
# <|{current_user_message}|input|label=Write your message here...|on_action=send_message|class_name=fullwidth|>
# """


# Gui(page).run(title="Taipy Chat", use_reloader=True, port=5001)