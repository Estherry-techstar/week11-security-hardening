# PII Handling & Data Retention Note

**Project:** Week 11 Security Hardening - RAG Retriever
**Date:** October 18, 2026

**1. Data Minimization & Masking:**
Our application adheres to data minimization principles. We only collect PII (Personally Identifiable Information) strictly necessary for functionality. All PII (such as email addresses, names, or document contents) is masked or excluded from application logs before being sent to Application Insights to prevent sensitive data leakage.

**2. Identity & Access:**
All secrets and API keys (such as the OpenRouter API Key) are securely stored in Azure Key Vault. Access to these secrets is controlled via Azure RBAC (Role-Based Access Control) and Managed Identities. No static credentials or PII are stored in code repositories or `.env` files in production.

**3. Data Retention (GDPR/NDPR Compliance):**
*   **Application Logs:** Retained for 30 days in Application Insights for debugging and security auditing, after which they are automatically purged.
*   **User Data:** Any uploaded documents or user data stored in the vector database (ChromaDB) are retained only for the duration of the user's active session or account. Upon deletion request, all PII is permanently erased within 7 days, in compliance with GDPR and NDPR "Right to Erasure" requirements.