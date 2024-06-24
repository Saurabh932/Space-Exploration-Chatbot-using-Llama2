from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone
from src.prompt import prompt_template

import pinecone
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
import boto3

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
S3_BUCKET_NAME = "spaceexplorationbucket"
MODEL_NAME = "llama-2-7b-chat.ggmlv3.q4_0.bin"
MODEL_LOCAL_PATH = f"model/{MODEL_NAME}"

# Download model from S3 if it doesn't exist locally
def download_model_from_s3(bucket_name, model_name, local_path):
    if not os.path.exists(local_path):
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        s3.download_file(bucket_name, model_name, local_path)
        print(f"Downloaded {model_name} from S3 to {local_path}")

# Ensure the model directory exists
os.makedirs(os.path.dirname(MODEL_LOCAL_PATH), exist_ok=True)

# Download the model
download_model_from_s3(S3_BUCKET_NAME, MODEL_NAME, MODEL_LOCAL_PATH)

embeddings = download_hugging_face_embeddings()

# Initializing Pinecone
pinecone.Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)

index_name = "space"

# Loading the index
docsearch = Pinecone.from_existing_index(index_name, embeddings)

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Initialize CTransformers with the local model path
llm = CTransformers(
    model=MODEL_LOCAL_PATH,
    model_type="llama",
    config={'max_new_tokens': 512, 'temperature': 0.8}
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result = qa.invoke({"query": input})
    print("Response: ", result["result"])
    return str(result["result"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6500, debug=True)
