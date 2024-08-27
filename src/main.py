from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from src.utils.write_markdown_file import write_markdown_file
from collections import OrderedDict
import os

# Using Llama3 on Groqs LPU
GROQ_LLM = ChatGroq(model="llama3-70b-8192")

# Categorize EMAIL --> 
# Research Router --> Search Keywords --> Write Draft Email -->Rewrite Router --> Draft Email Analysis --> Rewrite Email

prompt_folder = 'src/prompt'
full_path = lambda x: os.path.join(os.path.dirname(__file__), x)

prompts = OrderedDict(
    ['email_category_generator', full_path('1_categorize_email.md')],
    ['research_router', full_path('2_researcher_router.md')],
    ['search', full_path('3_search_keyword.md')],
    ['draft_writer', full_path('4_draft_email_writer.md')],
    ['rewrite_router', full_path('5_rewrite_router.md')],
    ['rewrite_draft_analyser', full_path('6_rewrite_draft_analyser.md')],
    ['rewrite_email', full_path('7_rewrite_email.md')],
)

#1
email_category_generator = PromptTemplate(template=prompts['email_category_generator'], input_variable = ["initial_email"]) | GROQ_LLM | StrOutputParser()
#2
research_router = PromptTemplate(template=prompts['research_router'], input_variables=["initial_email","email_category"]) | GROQ_LLM | JsonOutputParser()
#3
search_keyword_chain = PromptTemplate(template=prompts['search'], input_variables=["initial_email","email_category"]) | GROQ_LLM | JsonOutputParser()
#4
draft_writer_chain = PromptTemplate(template=prompts['draft_writer'], input_variables=["initial_email","email_category"]) | GROQ_LLM | JsonOutputParser()
#5
rewrite_router = PromptTemplate(template=prompts['rewrite_router'],input_variables=["initial_email","email_category","draft_email"]) | GROQ_LLM | JsonOutputParser()
#6
draft_analysis_chain = PromptTemplate(template=prompts['rewrite_draft_analyser'],input_variables=["initial_email","email_category","research_info"]) | GROQ_LLM | JsonOutputParser()
#7
rewrite_email_chain = PromptTemplate(template=prompts['rewrite_email'],input_variables=["initial_email","email_category","research_info","email_analysis","draft_email",]) | GROQ_LLM | JsonOutputParser()
