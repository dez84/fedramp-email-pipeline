/* BRONZE LAYER: Raw ingestion from the seed file. */
SELECT * FROM {{ ref('raw_email_logs') }}
