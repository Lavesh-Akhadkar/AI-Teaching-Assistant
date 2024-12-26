from swarmauri.llms.concrete.MistralModel import MistralModel
from swarmauri.conversations.concrete.MaxSystemContextConversation import (
    MaxSystemContextConversation,
)
from swarmauri.vector_stores.concrete.TfidfVectorStore import TfidfVectorStore
from swarmauri.messages.concrete.SystemMessage import SystemMessage
from swarmauri.documents.concrete.Document import Document
from swarmauri.agents.concrete.RagAgent import RagAgent
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("MISTRAL_API_KEY")
llm = MistralModel(api_key=API_KEY, name="mistral-large-latest")


conversation = MaxSystemContextConversation(max_size=4)
vector_store = TfidfVectorStore()


agent = RagAgent(
    llm=llm,
    conversation=conversation,
    system_context=SystemMessage(
        content="You are a helpful and knowledgeable teacher. Provide simple, accurate, and easy-to-understand explanations tailored to the user's level of understanding. Focus on clarity and avoid unnecessary complexity. Answer the questions based on this context (Might not be available always): "
    ),
    vector_store=vector_store,
)


def converse(user_query):

    result = agent.exec(user_query, llm_kwargs={"max_tokens": 4096})

    return str(result)


def clear_history():
    conversation.clear_history()


def add_document_to_store(content):
    vector_store.add_documents([Document(content=content)])


def delete_all_documents():
    vector_store.clear_documents()
