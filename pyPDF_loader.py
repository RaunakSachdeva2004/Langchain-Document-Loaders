from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model = "openai/gpt-oss-120b")

loader = PyPDFLoader("dl-curriculum.pdf")
docs = loader.load()

print(docs[0].page_content)

print(docs[1].metadata)

print(len(docs))

