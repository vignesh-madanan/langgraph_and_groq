from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from src.utils.write_markdown_file import write_markdown_file
import os

# Using Llama3 on Groqs LPU
GROQ_LLM = ChatGroq(model="llama3-70b-8192")

# Categorize EMAIL --> 
# Research Router --> Search Keywords --> Write Draft Email -->Rewrite Router --> Draft Email Analysis --> Rewrite Email

prompt_folder = 'src/prompt'
full_path = lambda x: os.path.join(os.path.dirname(__file__), x)
prompts = {
    'email_category_generator': full_path('1_categorize_email.md'),
    'research_router': full_path('2_researcher_router.md')
}

email_category_generator = PromptTemplate(prompts['email_category_generator']) | GROQ_LLM | StrOutputParser()
research_router = PromptTemplate(prompts['research_router_prompt']) | GROQ_LLM | JsonOutputParser()




