from langchain.prompts import PromptTemplate # type: ignore
from langchain.llms import OpenAI 
from langchain.chains import LLMChain
import OpenAiKey from .env
import os

KNOWLEDGE_BASE = {
    "What’s my account balance?": "Please log in to your BMO online banking to view your current account balance.",
    "How do I reset my password?": "Visit bmo.com/reset-password and follow the instructions to reset your password.",
    "What are your product features?": "BMO offers savings accounts, credit cards, and investment options with competitive rates and rewards.",
    "When are your customer service hours?": "BMO customer service is available Monday to Friday, 8:00 AM to 8:00 PM EST.",
    "How do I contact support?": "You can contact BMO support by calling 1-800-123-4567 or emailing support@bmo.com."
}

os.environ["OPENAI_API_KEY"] = OpenAiKey