# PII Handling & Data Retention Note

**Project:** Week 11 Security Hardening - RAG Retriever
**Date:** October 18, 2026

**1. Technical PII Controls (Enforceable Implementation)**
*   **Data Minimization:** The application only processes document text and queries necessary to answer the user's question. No user metadata is stored permanently.
*   **Masking Implementation:** Application logging is configured to exclude raw document text and user queries from standard logs. If an error occurs, only the endpoint and HTTP status code are logged to Application Insights, preventing PII leakage into monitoring dashboards.

**2. Identity & Access Control**
*   All secrets and API keys are securely stored in Azure Key Vault. 
*   Access is strictly controlled via Azure RBAC (Role-Based Access Control). The local development environment authenticates via Azure CLI, and production will use a System-Assigned Managed Identity.

**3. Data Retention (GDPR/NDPR Compliance)**
*   **Application Logs:** Telemetry data in Application Insights is retained for 30 days (default Azure setting), after which it is automatically purged.
*   **Vector Database (ChromaDB):** Uploaded documents and their embeddings are retained in the local `chroma_db` directory. A deletion endpoint/script is used to remove the document ID and its associated vector chunks permanently upon user request, fulfilling the "Right to Erasure."