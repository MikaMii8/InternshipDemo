# Taylor Swift Q&A Bot 
## Overview
Welcome! This repository contains a simple Question-and-Answer (Q&A) bot built using the Retrieval-Augmented Generation (RAG) approach. The bot utilizes Taylor Swift's song lyrics to answer questions, making it a fun and unique way to interact with her discography. 
Link to project: (https://github.com/MikaMii8/InternshipDemo/tree/main)

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

This repository contains the implementation of a Q&A bot designed to interact with a lyrics dataset using a Retrieval-Augmented Generation (RAG) model. The bot is developed in two main parts:

1. **Data Preparation**
2. **Q&A Bot Deployment**

### 1. Data Preparation (`data_prep_demo.ipynb`)

The data preparation process is essential to ensure that the lyrics dataset is properly formatted and ready for use by the RAG agent.

### Steps:
1. Open the `data_prep_demo.ipynb` notebook in Jupyter or any compatible environment.
2. Execute all the cells sequentially. This will process the lyrics dataset and prepare it for the Q&A bot.

### 2. Running the Q&A Bot (`QandA.py`)

The `QandA.py` file provides a more advanced version of the Q&A bot, implemented with Streamlit for a better user experience and improved response quality.

### Steps:
1. Ensure that you have completed the data preparation by running `data_prep_demo.ipynb` as described above.
2. Open an integrated terminal in your development environment.
3. Run the Q&A bot with the following command:
   ```bash
   streamlit run QandA.py
   ```
   
## Notes

- **References**: (https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_with_query_engine/).
- **Costs**: Using the OpenAI API for this bot is very affordable, with minimal costs involved.

Happy coding!
