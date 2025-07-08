# Intelligent Complaint Analysis for Financial Services

## Introduction

CrediTrust Financial is a leading digital finance company operating across East Africa, offering products like Credit Cards, Personal Loans, Buy Now Pay Later (BNPL), Savings Accounts, and Money Transfers. Handling thousands of customer complaints monthly, CrediTrust aims to transition from reactive problem-solving to proactive customer experience improvement.

This project builds a Retrieval-Augmented Generation (RAG) chatbot that transforms unstructured complaint narratives into actionable insights. The chatbot enables internal teams to quickly query customer feedback and receive synthesized, evidence-backed answers.

---

## Technical Choices

### Data

- Source: Consumer Financial Protection Bureau (CFPB) complaint dataset
- Filtered to five core product categories: Credit Cards, Personal Loans, BNPL, Savings Accounts and Money Transfers
- Cleaned and preprocessed narratives to remove noise and standardize text

### Chunking

- Used LangChain’s RecursiveCharacterTextSplitter
- Chunk size: 500 characters with 100 characters overlap — balanced granularity and context retention

### Embedding Model

- Sentence-Transformers: `all-MiniLM-L6-v2`
- Selected for its efficiency, strong semantic representation, and compatibility with vector databases

### Vector Store

- ChromaDB persistent store to index and search embedded complaint chunks
- Metadata (e.g., product category, source index) stored with embeddings for filtering

### Language Model & Generation

- Used Hugging Face’s Mistral 7B Instruct model for generation
- Designed prompt templates to guide the model to answer strictly based on retrieved context, improving factuality

---

## System Evaluation
*Evaluation table included in `reports/evaluation_table.md`*

---

## UI Showcase

![Chatbot UI Demo](images/chatbot_ui.png)

---

## Challenges & Learnings

- Handling noisy, unstructured complaint narratives required robust preprocessing  
- Balancing chunk size and overlap was critical to preserve context without overwhelming the embedding model  
- Prompt engineering significantly impacted answer quality and factual correctness  
- Integrating vector search with generation enabled fast, relevant, and explainable answers

---

## Future Improvements

- Implement streaming responses for improved user experience  
- Expand metadata filtering for more granular product and issue segmentation  
- Explore fine-tuning the language model on domain-specific complaint data  
- Add multilingual support for broader East African market coverage

---

## References

- [LangChain Documentation](https://langchain.com)  
- [ChromaDB Docs](https://docs.trychroma.com)  
- [Sentence-Transformers](https://www.sbert.net)  
- [Hugging Face Models](https://huggingface.co/models)  
- Consumer Financial Protection Bureau (CFPB) Dataset  

---

**Prepared by:** [Abel Adamu Shumet]  
**Date:** [7/8/2025]