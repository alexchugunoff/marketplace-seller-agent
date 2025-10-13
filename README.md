# Marketplace Seller Assistant Agent

**A smart assistant agent designed to help marketplace sellers by leveraging open-source Large Language Models (LLMs), vector search, and a knowledge base of FAQ and process documentation.**

---

## 📚 Project Overview

This project implements an intelligent agent aimed at supporting sellers on a marketplace platform. The agent uses open-source LLMs (specifically [Deepseek](https://github.com/deepseekai/deepseek)) combined with a vector search engine to provide accurate and relevant answers based on a curated knowledge base composed of seller FAQs and account process descriptions.

The agent is accessible through a simple web application built with Streamlit, allowing sellers to interact with it easily and get timely assistance without needing to navigate complex documentation manually.

---

## 🚀 Key Features

- **Open-source LLM integration:** Utilizes Deepseek LLM to understand and process natural language queries from sellers.
- **Custom knowledge base:** Builds a vectorized search index from marketplace FAQs and seller account process descriptions.
- **Retrieval-Augmented Generation (RAG):** Combines retrieval of relevant documents with generative language modeling for precise, context-aware responses.
- **User-friendly interface:** Streamlit-powered application for quick and straightforward interaction.
- **Scalable and modular:** Easily extendable to add more data sources or switch LLMs/vector search backends.

---

## 🔧 Setup Instructions

Follow these steps to get the project up and running locally:

1. **Clone the repository:**
git clone https://github.com/yourusername/marketplace-seller-agent.git
cd marketplace-seller-agent

2. **Create and activate a Python virtual environment:**
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. **Install required dependencies:**
pip install -r requirements.txt

4. **Prepare the knowledge base:**
- Place your FAQ and process documents in the `data/` directory.
- Run the knowledge vectorization script:

  ```
  python vectorize_knowledge.py
  ```

5. **Run the Streamlit app:**
streamlit run app.py

6. **Open your browser and go to:** `http://localhost:8501`

---

## ⚙️ How It Works

1. **User input:** Sellers type their questions into the Streamlit interface.
2. **Vector search:** The input query is converted into a vector and matched against the vectorized knowledge base to retrieve the most relevant documents.
3. **LLM generation:** Deepseek LLM receives the retrieved documents along with the user question to generate a detailed and helpful answer.
4. **Response display:** The generated response is displayed back to the seller through the app interface.

---

## 📝 Example Usage

- **Input:**  
*"How do I update my payment details in the seller dashboard?"*

- **Output:**  
The agent provides a concise step-by-step guide referencing the relevant seller dashboard process, sourced from the knowledge base.

---

## 🛠️ Project Structure
marketplace-seller-agent/
├── data/ # FAQ and process documents for knowledge base
├── vectorize_knowledge.py # Script to create vector embeddings from data
├── app.py # Streamlit app code
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── utils/ # Helper functions for vector search and LLM integration

---

## 📈 Future Improvements

- Add multi-language support for cross-border sellers.
- Integrate additional external data sources for expanded knowledge.
- Implement user feedback loop to improve answer accuracy.
- Deploy as a cloud service with authentication and usage analytics.

---

## 👤 About Me

This project is a part of LLM Zoomcamp. I designed this to explore practical applications of modern NLP in e-commerce. Your feedback and contributions are welcome!

---

Feel free to reach out if you have questions or want to collaborate!

---