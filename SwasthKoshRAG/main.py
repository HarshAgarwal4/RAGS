from fastapi import FastAPI
from RAG.Retriver import build_retriever
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get('/')
def main():
    print('Hello world')
    return 'HELLO'

@app.get('/chunks')
def get_context(query : str):
    try:
        retriever = build_retriever()
        print('retrieved succesfully')
        docs = retriever.invoke(query)
        print(docs)
        context = "\n\n".join([doc.page_content for doc in docs])
        return context
    except Exception as e:
        print(e)
        return e