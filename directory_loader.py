from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader = DirectoryLoader(
    path = 'book',
    glob= '*.pdf',
    loader_cls=PyPDFLoader # type: ignore
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)