import pandas as pd
from faker import Faker
import random
import os

# Initialize Faker
fake = Faker()

def generate_email_logs(num_rows=1000):
    data = []
    
    # 1. Define suspicious keywords for the 'Detection' logic
    threat_keywords = ['Urgent', 'Wire Transfer', 'Reset Password', 'Confidential', 'Verify Account']
    
    print(f"Generating {num_rows} log entries...")
    
    for _ in range(num_rows):
        is_threat = random.random() < 0.05 # 5% chance of being a threat
        
        subject = fake.sentence(nb_words=4)
        if is_threat:
            subject = f"{random.choice(threat_keywords)}: {subject}"

        row = {
            'event_id': fake.uuid4(),
            'timestamp': fake.date_time_between(start_date='-30d', end_date='now'),
            'sender_email': fake.email(),
            'recipient_email': fake.company_email(), # Simulating corp/gov email
            'source_ip': fake.ipv4(),
            'subject_line': subject,
            'email_body_length': random.randint(50, 5000)
        }
        data.append(row)

    df = pd.DataFrame(data)
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Save to CSV (Simulating a raw ingestion bucket)
    df.to_csv('data/raw_email_logs.csv', index=False)
    print(f"Success! Saved to data/raw_email_logs.csv")

if __name__ == "__main__":
    generate_email_logs()
