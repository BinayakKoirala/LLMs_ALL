import streamlit as st
import os
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain



st.title('SEE GURU GPT')
prompt = st.text_input('Plug in your prompt here') 

os.environ['OPENAI_API_KEY'] = "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"


loader = PyPDFLoader("/home/binayak/Desktop/LLM Research /Guru/book/science.pdf")
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings(openai_api_key= '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')
pinecone.init(
    api_key="d2b47cdd-8c4a-46a9-949a-3b6e0a8a1f52",  # find at app.pinecone.io
    environment="us-central1-gcp"  # next to api key in console
)
index_name = "langchain" # put in the name of your pinecone index here

docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)

llm = OpenAI(temperature=0, openai_api_key="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")
chain = load_qa_chain(llm, chain_type="stuff")

docs = docsearch.similarity_search(prompt)
chain.run(input_documents=docs, question=prompt)


st.write(chain.run(input_documents=docs, question=prompt))