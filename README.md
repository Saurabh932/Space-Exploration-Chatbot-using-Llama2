# Space Exploration Chatbot using Llama2

## Project Overview

The Space Exploration Chatbot is developed to enhance the user's understanding of space-related topics and provide a conversational interface for accessing information about space missions, celestial events, planets, stars, galaxies, and more. By leveraging the capabilities of the Llama2 model, the chatbot can engage in natural language conversations, understand user queries, and provide informative responses.

## Problem Statement

Despite the growing interest in space exploration and astronomy, accessing reliable and comprehensive information about space-related topics can be challenging for individuals without a background in the field. Traditional sources of information, such as textbooks and scientific papers, may be too technical or difficult to understand for the general public. Additionally, searching for specific information online can be time-consuming and overwhelming due to the vast amount of content available.

## Dataset

The Space Exploration Chatbot utilizes a custom dataset compiled from various books and papers related to space exploration, astronomy, and astrophysics. This dataset includes information about space missions, celestial bodies, astronomical phenomena, and more. Stored in a Vector Database (VectorDB), specifically Pinecone, the dataset undergoes preprocessing and indexing to convert textual data into vector embeddings for efficient storage and retrieval. By leveraging Pinecone's capabilities, the chatbot can efficiently search and retrieve relevant information to provide users with comprehensive and accurate responses to their queries.

## Objectives

- Develop a chatbot capable of answering questions and providing information about space exploration using technologies such as Python, LangChain, Flask, Meta Llama2, and Pinecone.
- Create an intuitive and user-friendly interface for interacting with the chatbot.
- Ensure that the chatbot's responses are accurate, informative, and easy to understand for users with varying levels of knowledge about space.

## Key Features

- Natural language understanding: The chatbot can interpret user queries written in natural language and generate appropriate responses using LangChain and Meta Llama2.
- Comprehensive knowledge base: Leveraging pre-trained models and knowledge bases, the chatbot has access to a wide range of information about space exploration topics.
- Interactive interface: Users can engage in conversational interactions with the chatbot through a user-friendly interface built using Flask.
- Continuous learning: The chatbot can be updated with new information and improve its responses over time with the help of Pinecone.


# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/Saurabh932/Space-Exploration-Chatbot-using-Llama2.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mchatbot python=3.8 -y
```

```bash
conda activate mchatbot
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost: http://localhost:8080.
```


### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone


# Web Application Demo:

![](https://github.com/Saurabh932/Space-Exploration-Chatbot-using-Llama2/blob/main/Screenshot%202024-01-16%20211111.jpg)
