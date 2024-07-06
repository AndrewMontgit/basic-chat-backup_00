

import sys
import os
from dotenv import load_dotenv

load_dotenv()

project_path = os.getenv("PROJECT_PATH")
venv_path = os.getenv("VENV_PATH")

if project_path:
    sys.path.append(project_path)

if venv_path:
    sys.path.append(venv_path)

# Add the virtual environment's site-packages directory to the Python path
# sys.path.append(venv_site_packages)
# from typeclasses.objects import Object
from langchain.prompts import (HumanMessagePromptTemplate,
                               ChatPromptTemplate, MessagesPlaceholder)
from langchain_core.messages import SystemMessage
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory





class ChatBot():
    def __init__(self):
        

        self.chat = ChatOpenAI(temperature=0.7)
        self.system_message = ("Your job is to greet respond to travelers and welcome them."
                                "You mostly provide general chit chat but are knowledgeable."
                                "You are a NPC in a world referred to as Shadows of Neon (S.O.N). Your name is Vera Chrome are you are a cyborg Lab technician,"
                                "with half your brain upgraded with robot tech. The World contains 3 main areas. the  world marked by the aftermath of a catastrophic event known as The Collapse." 
				"This event fractured global society, giving rise to powerful factions that now vie for control over the remnants of civilization. "
				"The City is a sprawling metropolis dominated by towering skyscrapers, neon lights, and high-tech corporations."
				"The Jungle-like Area is a lush, biodiverse region teeming with life and ancient mysteries. The Wasteland is a harsh, desolate expanse characterized by barren landscapes and constant strife.")

        self.memory = ConversationBufferMemory(
            memory_key="messages",
            return_messages=True,
            chat_memory=FileChatMessageHistory("messages.json")
        )

        input_variables = ["content", "messages", "system_message"]
        self.prompt = ChatPromptTemplate(
            input_variables=input_variables,
            messages=[
                SystemMessage(content=self.system_message, additional_kwargs={}),
                MessagesPlaceholder(variable_name="messages"),
                HumanMessagePromptTemplate.from_template("{content}")
            ]
        )

        self.chain = LLMChain(
            llm=self.chat,
            prompt=self.prompt,
            memory=self.memory
        )

    def process_input(self, content):
        result = self.chain({"content": content})
        return result["text"]

# Usage in Evennia:
# import chatbot
# bot = chatbot.ChatBot()
# response = bot.process_input("Hello, chatbot!")
# print(response)
