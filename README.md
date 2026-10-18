# RAG Retriever - Week 11 Security Hardening

A FastAPI-based Retrieval-Augmented Generation (RAG) application that performs hybrid search (Vector + BM25), reranking, and LLM generation with citations. 

This version (Week 11) introduces enterprise-grade security and observability:
*   **Secrets Management:** All API keys are removed from the codebase and fetched securely from **Azure Key Vault**.
*   **Identity-Based Access:** Uses `DefaultAzureCredential` to authenticate seamlessly via the developer's local Azure CLI login or a Managed Identity in the cloud.
*   **Observability:** Fully instrumented with **Azure Application Insights** (OpenTelemetry) to track requests, latency, exceptions, and dependencies.

## Prerequisites
*   Python 3.10+
*   [Azure CLI installed and authenticated](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) (`az login`)
*   An Azure Key Vault containing a secret named `OpenAI-API-Key`
*   An Azure Application Insights instance

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd week9-rag-retrieval