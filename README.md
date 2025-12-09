# RAG_pipeline
This project implements a complete Retrieval-Augmented Generation (RAG) pipeline designed to simulate a website widget. It involves three main Python scripts that handle the flow from data acquisition to query resolution. The system first performs a Deep Web Crawl on the ITNB company website, ingests the content into a GroundX knowledge base, and finally uses an LLM (Llama 4 Maverick) to generate precise, context-aware answers to user queries directly in the terminal. This repository contains the three core scripts: scraping.py (analysing and extracting website content), ingest.py (uploading data to GroundX), and query.py (chatbot providing RAG answers).

You must install the Python libraries necessary for crawling, GroundX API interaction, and generation using the OpenAI SDK. Run the following command in your terminal to ensure all mandatory dependencies are installed: 
pip install groundx openai crawl4ai asyncio aiohttp

The RAG pipeline requires execution in three sequential steps to build the knowledge base and then query it:

1. Data Collection (Scraping): Run python scraping.py to perform a deep, recursive crawl of the target website and save the structured content to itnb_content.md.

2. Content Ingestion (GroundX): Run python ingest.py to upload the cleaned itnb_content.md file to your configured Bucket ID in GroundX (see documentation below). 

3. Chat: Run python query.py. This will launch the interactive chatbot in your terminal. You can input questions about the ITNB website content, and the RAG system will retrieve the relevant context, augment the query, and generate the final answer using the LLM.

Note that you will need to create a GroundX account to store the database and handle the API key (documentation: https://docs.eyelevel.ai/documentation/fundamentals/quickstart). Moreover, you will need to use an API key for the LLM in the generation step. In this case, we are using Llama 4 Maverick to generate the responses.
