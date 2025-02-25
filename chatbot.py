from langchain.prompts import PromptTemplate # type: ignore
from langchain_openai import OpenAI 
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()
KNOWLEDGE_BASE = {
    "What’s my account balance?": "Please log in to your BMO online banking to view your current account balance.",
    "How do I reset my password?": "Visit bmo.com/reset-password and follow the instructions to reset your password.",
    "What are your product features?": "BMO offers savings accounts, credit cards, and investment options with competitive rates and rewards.",
    "When are your customer service hours?": "BMO customer service is available Monday to Friday, 8:00 AM to 8:00 PM EST.",
    "How do I contact support?": "You can contact BMO support by calling 1-800-123-4567 or emailing support@bmo.com."
}

OpenAiKey = os.getenv("OpenAiKey")
os.environ["OPENAI_API_KEY"] = OpenAiKey

llm = OpenAI()

prompt_template = PromptTemplate(
    input_variables=["query", "knowledge_base"],
    template="You are a customer support chatbot for BMO Financial Group. Answer the following customer query: '{query}'. Use the provided knowledge base if applicable: {knowledge_base}. If the query isn’t in the knowledge base, provide a polite response suggesting they contact support."
)

chain = LLMChain(llm=llm, prompt=prompt_template)

def chatbot_response(query):
    if(query in KNOWLEDGE_BASE): return KNOWLEDGE_BASE[query]
    
    response = chain.run(query=query, KNOWLEDGE_BASE=str(KNOWLEDGE_BASE))
    return response.strip()

def main():
    print("welcome to Customer Support Chatbot!")
    query=""
    while query.lower() != 'q':
        query = input("Enter your questions or q to quit").strip()
        if query.lower() != 'q':
            response = chatbot_response(query)
            print(response)
if __name__ == "__main__":
    main()