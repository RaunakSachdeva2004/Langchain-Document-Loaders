from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("cricket.txt",encoding="utf8")

llm = ChatGroq(model = "openai/gpt-oss-120b")

prompt= PromptTemplate(
    template="Summarize the following text:\n\n{text}",
    input_variables=["text"],
)


parser = StrOutputParser()

docs = loader.load()

# print(type(docs)) # <class 'list'>

# print(len(docs)) # 1

# print(type(docs[0])) # <class 'langchain.schema.document.Document'>

chain = prompt | llm | parser

res = chain.invoke({"text": docs[0].page_content})
print(res)
