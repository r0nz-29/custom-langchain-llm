from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from flask import Flask, request
from flask_cors import CORS
import requests, os
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from utils import template
from customs import CustomOutputParser, CustomPromptTemplate

def get_products(*args) -> str:
    result = requests.get("https://fakestoreapi.com/products")
    return result.content

app = Flask(__name__)
CORS(app)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [
    Tool.from_function(
        func=get_products,
        name="Get products",
        description="useful for when you need to return information about products from the internet",
        return_direct=True
    )
]

prompt = CustomPromptTemplate(
    template=template,
    tools=tools,
    input_variables=["input", "intermediate_steps"]
)

output_parser = CustomOutputParser()

llm = ChatOpenAI(
    openai_api_key=os.environ['OPENAI_API_KEY'], 
    temperature=0, 
)

agent_chain = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)

@app.route('/')
def test_api():
    return get_products()

@app.route('/ai', methods=['POST'])
def ai():
    prompt = request.form['prompt']

    try:
        return agent_chain.run(prompt)
    
    except Exception:
        return "Error: Max Tokens exceed 4097"