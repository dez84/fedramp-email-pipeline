/* SILVER LAYER: PII Anonymization.
   We hash emails using MD5 so we can analyze patterns
   without seeing the actual identities (FedRAMP Requirement).
*/
SELECT
    event_id,
    timestamp,
    MD5(sender_email) as sender_id_hash,
    MD5(recipient_email) as recipient_id_hash,
    source_ip,
    subject_line,
    email_body_length
FROM {{ ref('stg_email_logs') }}
