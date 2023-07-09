import vertexai
from vertexai.language_models import TextGenerationModel
from google.oauth2 import service_account
import json
from vertexai.preview.language_models import ChatModel,InputOutputTextPair

with open ("credentials.json") as file:
    service_accountInfo=json.load(file)

myCredentials=service_account.Credentials.from_service_account_info(service_accountInfo)
vertexai.init(project="spyrai", location="us-central1",credentials=myCredentials)
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat()
response = chat.send_message("""hello""", **parameters)
print(f"Response from Model: {response.text}")