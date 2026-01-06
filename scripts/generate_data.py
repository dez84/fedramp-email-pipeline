import pandas as pd
from faker import Faker
import random
import os

# Initialize Faker
fake = Faker()

def generate_gov_audit_logs(num_rows=2000):
    data = []
    
    # Government-style subject lines (mix of standard & threats)
    gov_keywords = ['FOUO', 'CONFIDENTIAL', 'DoD Policy Update', 'Travel Authorization', 'Timesheet']
    threat_keywords = ['URGENT WIRE TRANSFER', 'RESET PASSWORD NOW', 'TOP SECRET DISCLOSURE', 'VERIFY ACCOUNT']
    
    print(f"Generating {num_rows} government audit logs...")
    
    for _ in range(num_rows):
        is_threat = random.random() < 0.05 # 5% chance of being a threat/phishing attempt
        
        # Simulate government email domains
        sender_domain = random.choice(['mail.mil', 'army.mil', 'navy.mil', 'gmail.com', 'yahoo.com'])
        sender = f"{fake.first_name().lower()}.{fake.last_name().lower()}@{sender_domain}"
        
        recipient = f"{fake.last_name().lower()}@agency.gov"
        
        if is_threat:
            subject = f"ACTION REQUIRED: {random.choice(threat_keywords)}"
        else:
            subject = f"{random.choice(gov_keywords)}: {fake.sentence(nb_words=3)}"

        row = {
            'event_id': fake.uuid4(),
            'timestamp': fake.date_time_between(start_date='-30d', end_date='now'),
            'sender_email': sender,
            'recipient_email': recipient,
            'source_ip': fake.ipv4(),
            'subject_line': subject,
            'email_body_length': random.randint(50, 5000),
            'classification_level': 'UNCLASSIFIED' if not is_threat else 'UNKNOWN'
        }
        data.append(row)

    df = pd.DataFrame(data)
    
    # Ensure data directory exists
    os.makedirs('../data', exist_ok=True)
    
    # Save to CSV in the main data folder
    df.to_csv('../data/raw_email_logs.csv', index=False)
    print(f"Success! Generated {num_rows} logs to ../data/raw_email_logs.csv")

if __name__ == "__main__":
    generate_gov_audit_logs()
