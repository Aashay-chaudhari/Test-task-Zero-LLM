from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
import os

from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = ""
llm = ChatOpenAI(model_name='gpt-3.5-turbo-16k', temperature=0)


def get_columns(tableA, template_cols):
    propmt_template_name1 = PromptTemplate(
        input_variables=["tableA", "template_cols"],
        template="Extract the column names from the given data in {tableA}. Provide a Python list of column names "
                 "that are most similar to the column names in the provided list {template_cols}. The returned list "
                 "should be formatted as a Python list so that it can be easily used to substitute the headers in a "
                 "dataframe. Also show the basis for the decision for selecting particular columns from given data. ("
                 "formats, distributions, and other features that are highlighted in the backend) and append this as "
                 "a element to the list. "
    )
    chain = LLMChain(llm=llm, prompt=propmt_template_name1)
    resp = chain.run({'tableA': tableA, 'template_cols': template_cols})
    print("resp from get columns is: ", resp)
    return resp


def get_temp_columns(tableA):
    propmt_template_name = PromptTemplate(
        input_variables=["tableA"],
        template="Extract the column names from the data given : {tableA}. Just return the columns in a list format."
    )
    chain = LLMChain(llm=llm, prompt=propmt_template_name)
    resp = chain.run(tableA)

    return resp


def get_replace_cols(tableA, template_cols):
    propmt_template_name1 = PromptTemplate(
        input_variables=["tableA", "template_cols"],
        template="Extract the column names from the given data in {tableA}. Provide a Python list of column names "
                 "that are most similar to the column names in the provided list {template_cols}. The returned list "
                 "should be formatted as a Python list so that it can be easily used to substitute the headers in a "
                 "dataframe."
    )
    chain = LLMChain(llm=llm, prompt=propmt_template_name1)
    resp = chain.run({'tableA': tableA, 'template_cols': template_cols})
    print("resp from get columns is: ", resp)
    return resp
