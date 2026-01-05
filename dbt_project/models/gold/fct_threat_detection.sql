/* GOLD LAYER: Threat Detection Logic.
   Aggregates activity by the anonymous hash to find bad actors.
*/
SELECT
    sender_id_hash,
    COUNT(*) as total_emails_sent,
    -- Flag suspicious subjects
    SUM(CASE
        WHEN subject_line LIKE '%Urgent%' OR subject_line LIKE '%Wire Transfer%'
        THEN 1 ELSE 0
    END) as suspicious_email_count,

    -- Logic: If they sent > 0 suspicious emails, flag them as HIGH RISK
    CASE
        WHEN SUM(CASE WHEN subject_line LIKE '%Urgent%' THEN 1 ELSE 0 END) > 0
        THEN 'HIGH_RISK'
        ELSE 'NORMAL'
    END as threat_level

FROM {{ ref('int_email_logs_masked') }}
GROUP BY sender_id_hash
