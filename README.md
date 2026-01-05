# FedRAMP-Ready Email Threat Detection Pipeline

## Project Overview
This project simulates the data infrastructure required for a **FedRAMP High** authorization environment. It ingests raw email traffic logs, applies **PII Anonymization (Hashing)** to comply with privacy controls (NIST 800-53), and aggregates data for threat detection analysis.

## Architecture (Medallion Pattern)
* **Bronze Layer (`stg_email_logs`):** Raw ingestion of email metadata (Sender, Recipient, IP, Subject).
* **Silver Layer (`int_email_logs_masked`):** Implements **SHA-256/MD5 hashing** on PII fields. This ensures data scientists can analyze behavioral patterns without exposing the identities of government employees.
* **Gold Layer (`fct_threat_detection`):** Aggregates data by `sender_hash` to identify phishing patterns (e.g., high volume of "Urgent" subject lines).

## Technologies Used
* **Infrastructure:** Ubuntu Linux VPS (Linode), Docker (PostgreSQL Container).
* **Transformation:** dbt Core (Data Build Tool).
* **Ingestion:** Python (Faker library for synthetic data).
* **Orchestration:** Unix / Bash.

## How to Run
1.  **Generate Data:** `python3 scripts/generate_data.py`
2.  **Load Data:** `dbt seed`
3.  **Run Pipeline:** `dbt run`
4.  **Test Assumptions:** `dbt test`
