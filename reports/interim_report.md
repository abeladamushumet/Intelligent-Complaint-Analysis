# Interim Report: Intelligent Complaint Analysis for Financial Services

## 1. Introduction  
CrediTrust Financial is a fast-growing digital finance company operating in East Africa. This project aims to build a Retrieval-Augmented Generation (RAG) powered chatbot that transforms raw customer complaints into actionable insights for internal teams. This interim report covers Exploratory Data Analysis (EDA), preprocessing, text chunking, embedding, and vector store creation.

---

## 2. Exploratory Data Analysis (EDA) and Data Preprocessing

### 2.1 Dataset Overview  
- Source: Consumer Financial Protection Bureau (CFPB) complaint dataset  
- Total records loaded: **[9,609,797]**  
- Key fields: Product, Consumer complaint narrative, Issue label, Submission date  

### 2.2 Filtering and Cleaning  
- Focused on 5 products: Credit Cards, Personal Loans, Buy Now Pay Later (BNPL), Savings Accounts and Money Transfers  
- Removed complaints with empty or missing narratives  
- Cleaned text by lowercasing, removing special characters, and boilerplate phrases  
- Final dataset size after filtering: **[80,667]**  

### 2.3 Data Insights  
- Distribution of complaints by product category 
- Narrative length varied widely, from very short to very long texts  
- Identified some common issue types and recurring keywords 

---

## 3. Text Chunking, Embedding, and Vector Store Indexing

### 3.1 Chunking Strategy  
- Used LangChain’s RecursiveCharacterTextSplitter  
- Parameters: chunk size = 500 characters, chunk overlap = 100 characters  
- This balances context preservation and embedding quality by avoiding overly long or short chunks  

### 3.2 Embedding Model  
- Selected `sentence-transformers/all-MiniLM-L6-v2` for its balance of speed and accuracy in semantic search  
- Successfully generated embeddings for all text chunks  

### 3.3 Vector Store  
- Implemented with ChromaDB for efficient similarity search and metadata support  
- Indexed all chunks with metadata including source complaint index and product category  
- Persisted vector database locally for fast retrieval in the RAG pipeline  

---

## 4. Summary of Deliverables

| Task                   | Status           | Notes                          |
|------------------------|------------------|--------------------------------|
| Data Loading & EDA     | Completed        | Dataset filtered and cleaned   |
| Text Chunking          | Completed        | Chunking strategy finalized    |
| Embedding Generation   | Completed        | Embeddings generated           |
| Vector Store Creation  | Completed        | ChromaDB vector store persisted|

---

## 5. Next Steps  
- Develop the RAG pipeline for retrieval and answer generation  
- Create an interactive chatbot UI using Streamlit or Gradio  
- Perform qualitative evaluation with representative queries  
- Optimize chunking, embeddings, and prompt design based on feedback  

---

## 6. References  
- CFPB Consumer Complaint Database  
- LangChain Text Splitter Documentation: https://python.langchain.com/en/latest/modules/indexes/text_splitters.html  
- Sentence Transformers: https://www.sbert.net/  
- ChromaDB Documentation: https://docs.trychroma.com/

---

**Prepared by:** [Abel Adamu Shumet]  
**Date:** [7/6/2025]