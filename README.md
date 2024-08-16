# Taylor Swift Q&A Bot

## Overview
Welcome! This repository contains a simple Question-and-Answer (Q&A) bot built using the Retrieval-Augmented Generation (RAG) approach. The bot utilizes Taylor Swift's song lyrics to answer questions, making it a fun and unique way to interact with her discography.

The dataset used for this project can be found on Kaggle: (https://www.kaggle.com/datasets/PromptCloudHQ/taylor-swift-song-lyrics-from-all-the-albums).

## Getting Started

### Prerequisites
Before you start, make sure you have the following:

1. **Dataset**: Download the `lyrics.csv` file from the Kaggle dataset linked above.
2. **API Key**: Obtain your OpenAI API key from: (https://platform.openai.com/settings/profile?tab=api-keys).
3. **Python Packages**: Install the necessary Python packages listed in the `requirements.txt` file.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Download the Dataset**:
    - Place the `lyrics.csv` file in the root directory of the project.

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Add API Key**:
    - Ensure you have your OpenAI API key ready.

## Usage

The main logic of the Q&A bot is implemented in the first part of the `data_prep_demo.ipynb` notebook. This notebook is divided into two key parts:

1. **Data Preparation**:
   - The first part of the notebook processes the lyrics dataset to prepare it for use by the RAG agent.

2. **RAG Agent**:
   - The second part implements the RAG-based Q&A bot that interacts with the processed lyrics data.

To run the bot, simply open the `data_prep_demo.ipynb` notebook in Jupyter or any compatible environment, and execute the cells sequentially.

The python file `QandA.py` implements a bettter bot and uses streamlit. This bot has better responsses. Too run this first implement the data preparation or part 1 of the data prep demo file an dthen run this Qand A file in an integrated terminal with the command streamlut run QandA.py

## Notes

- **References**: (https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_with_query_engine/).
- **Costs**: Using the OpenAI API for this bot is very affordable, with minimal costs involved.

Happy coding!
