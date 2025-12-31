"""
Create a sample email dataset for testing
Run this if you don't have a dataset yet!
"""

import pandas as pd
import os

# Sample phishing emails (simplified examples)
phishing_emails = [
    "URGENT! Your account has been suspended. Click here to verify immediately: http://fake-bank.com/verify",
    "Congratulations! You've won $1,000,000! Claim your prize now by clicking this link: http://scam-lottery.com",
    "SECURITY ALERT: Unusual activity detected. Confirm your identity here: http://phishing-site.com/login",
    "Your password will expire in 24 hours! Update now: http://fake-service.com/update-password",
    "ACT NOW! Limited time offer! Free iPhone! Click here: http://fake-offer.com",
    "Your bank account has been locked due to suspicious activity. Verify here: http://fake-bank-site.com",
    "WINNER NOTIFICATION: You have been selected for a cash prize of $5000! http://lottery-scam.com",
    "URGENT: Your credit card has been charged $999. If this wasn't you, click here: http://phishing.com",
    "Your social security number has been compromised! Verify immediately: http://fake-government.com",
    "Congratulations! Click here to claim your inheritance of $2,000,000: http://scam.com/inheritance"
]

# Sample legitimate emails
legitimate_emails = [
    "Hi, just wanted to follow up on our meeting yesterday. Let me know if you have any questions.",
    "Your order #12345 has shipped and will arrive in 3-5 business days. Track your package here.",
    "Reminder: Team meeting tomorrow at 10 AM in Conference Room B. Please bring your project updates.",
    "Thank you for your purchase! Your receipt is attached. We hope you enjoy your new product.",
    "Hi John, can we schedule a call next week to discuss the quarterly report? Let me know your availability.",
    "Your monthly statement is now available. You can view it by logging into your account.",
    "Weekly newsletter: Here are the top 5 articles from our blog this week. Happy reading!",
    "Meeting notes from today's discussion are attached. Please review and add any comments.",
    "Your flight booking is confirmed. Flight details: AA123 on Dec 15, 2:30 PM. Have a great trip!",
    "Thanks for signing up! Welcome to our community. Here's a quick guide to get you started."
]

def create_sample_dataset():
    """Create a sample CSV file with example emails"""
    
    # Combine emails with labels
    emails = phishing_emails + legitimate_emails
    labels = [1] * len(phishing_emails) + [0] * len(legitimate_emails)  # 1 = phishing, 0 = legitimate
    
    # Create DataFrame
    df = pd.DataFrame({
        'text': emails,
        'label': labels
    })
    
    # Shuffle the data
    df = df.sample(frac=1).reset_index(drop=True)
    
    # Create directory if it doesn't exist
    os.makedirs('data/raw', exist_ok=True)
    
    # Save to CSV
    output_path = 'data/raw/emails.csv'
    df.to_csv(output_path, index=False)
    
    print("="*50)
    print("SAMPLE DATASET CREATED")
    print("="*50)
    print(f"\n✓ Created {len(df)} sample emails")
    print(f"  - Phishing emails: {len(phishing_emails)}")
    print(f"  - Legitimate emails: {len(legitimate_emails)}")
    print(f"\n✓ Saved to: {output_path}")
    print("\nYou can now run extract_features.py to process this dataset!")
    print("="*50)
    
    return df

if __name__ == "__main__":
    df = create_sample_dataset()
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
