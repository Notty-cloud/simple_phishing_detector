"""
Email Phishing Feature Extractor
This script loads email data and extracts features useful for detecting phishing attempts.
"""

import pandas as pd
import re
from collections import Counter
import os
from keywords import get_all_keywords
from logging_config import get_logger

logger = get_logger("extract_features")

class EmailFeatureExtractor:
    """Extract features from email text for phishing detection"""
    
    def __init__(self):
        self.suspicious_keywords = get_all_keywords()
        
    def count_urls(self, text):
        """Count the number of URLs in the email text"""
        if pd.isna(text):
            return 0
        # Pattern to match http:// or https:// URLs
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, str(text))
        return len(urls)
    
    def count_suspicious_keywords(self, text):
        """Count how many suspicious keywords appear in the email"""
        if pd.isna(text):
            return 0
        text_lower = str(text).lower()
        count = 0
        for keyword in self.suspicious_keywords:
            if keyword.lower() in text_lower:
                count += 1
        return count
    
    def find_suspicious_keywords(self, text):
        """Return list of which suspicious keywords were found"""
        if pd.isna(text):
            return []
        text_lower = str(text).lower()
        found = []
        for keyword in self.suspicious_keywords:
            if keyword.lower() in text_lower:
                found.append(keyword)
        return found
    
    def calculate_text_length(self, text):
        """Calculate the length of text in characters"""
        if pd.isna(text):
            return 0
        return len(str(text))
    
    def count_words(self, text):
        """Count the number of words in the text"""
        if pd.isna(text):
            return 0
        words = str(text).split()
        return len(words)
    
    def count_capital_letters(self, text):
        """Count percentage of capital letters (SHOUTING!)"""
        if pd.isna(text):
            return 0
        text_str = str(text)
        if len(text_str) == 0:
            return 0
        capitals = sum(1 for c in text_str if c.isupper())
        return round((capitals / len(text_str)) * 100, 2)
    
    def count_exclamation_marks(self, text):
        """Count exclamation marks (urgency indicator)"""
        if pd.isna(text):
            return 0
        return str(text).count('!')
    
    def has_dollar_signs(self, text):
        """Check if email contains dollar signs"""
        if pd.isna(text):
            return 0
        return 1 if '$' in str(text) else 0
    
    def extract_sender_domain(self, email):
        """Extract domain from email address"""
        if pd.isna(email):
            return "unknown"
        try:
            # Extract domain after @ symbol
            domain = str(email).split('@')[-1]
            return domain.lower()
        except:
            return "unknown"
    
    def extract_all_features(self, row, text_column='text', label_column='label'):
        """Extract all features from a single email"""
        text = row.get(text_column, '')
        
        features = {
            'text_length': self.calculate_text_length(text),
            'word_count': self.count_words(text),
            'url_count': self.count_urls(text),
            'suspicious_keyword_count': self.count_suspicious_keywords(text),
            'capital_letter_percent': self.count_capital_letters(text),
            'exclamation_count': self.count_exclamation_marks(text),
            'has_dollar_signs': self.has_dollar_signs(text),
            'suspicious_keywords_found': ', '.join(self.find_suspicious_keywords(text)[:5])  # Top 5
        }
        
        # Add label if it exists
        if label_column in row:
            features['is_phishing'] = row[label_column]
        
        return features


def load_dataset(file_path):
    """Load the email dataset from CSV file"""
    try:
        logger.info("Loading dataset from: %s", file_path)
        df = pd.read_csv(file_path)
        logger.info("Successfully loaded %d emails", len(df))
        logger.info("Columns found: %s", list(df.columns))
        return df
    except FileNotFoundError:
        logger.error("File not found at %s", file_path)
        logger.error("Please make sure you've downloaded the dataset and placed it in the correct folder.")
        return None
    except Exception as e:
        logger.exception("Error loading dataset: %s", e)
        return None


def process_dataset(df, text_column='text', label_column='label'):
    """Process entire dataset and extract features for all emails"""
    logger.info("Starting feature extraction...")
    
    extractor = EmailFeatureExtractor()
    
    # Create list to store all features
    all_features = []
    
    # Process each email
    for idx, row in df.iterrows():
        features = extractor.extract_all_features(row, text_column, label_column)
        all_features.append(features)
        
        # Show progress every 100 emails
        if (idx + 1) % 100 == 0:
            logger.info("Processed %d/%d emails...", idx + 1, len(df))
    
    # Convert to DataFrame
    features_df = pd.DataFrame(all_features)
    
    logger.info("Completed feature extraction. Extracted features from %d emails", len(features_df))
    return features_df


def save_features(features_df, output_path):
    """Save extracted features to CSV file"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        features_df.to_csv(output_path, index=False)
        logger.info("Features saved to: %s", output_path)
        return True
    except Exception as e:
        logger.exception("Error saving features: %s", e)
        return False


def display_statistics(features_df):
    """Display summary statistics of extracted features"""
    logger.info("DATASET STATISTICS")
    logger.info("Total emails processed: %d", len(features_df))
    
    # Check if we have labels
    if 'is_phishing' in features_df.columns:
        phishing_count = features_df['is_phishing'].sum()
        legitimate_count = len(features_df) - phishing_count
        logger.info("Phishing emails: %d", phishing_count)
        logger.info("Legitimate emails: %d", legitimate_count)
    
    # Feature statistics
    logger.info("Feature Statistics: avg_text_length=%0.0f, avg_word_count=%0.0f, avg_urls=%0.2f, avg_suspicious_keywords=%0.2f, avg_caps=%%0.2f",
                features_df['text_length'].mean(),
                features_df['word_count'].mean(),
                features_df['url_count'].mean(),
                features_df['suspicious_keyword_count'].mean(),
                features_df['capital_letter_percent'].mean())
    
    # Most common suspicious keywords
    all_keywords = []
    for keywords_str in features_df['suspicious_keywords_found']:
        if pd.notna(keywords_str) and keywords_str:
            all_keywords.extend(keywords_str.split(', '))
    
    if all_keywords:
        keyword_counts = Counter(all_keywords)
        logger.info("Top 10 Suspicious Keywords Found:")
        for keyword, count in keyword_counts.most_common(10):
            logger.info("  '%s': %d times", keyword, count)
    
    print("\n" + "="*50)


def main():
    """Main function to run the feature extraction pipeline"""
    logger.info("EMAIL PHISHING FEATURE EXTRACTOR")
    
    # Define file paths
    input_file = 'data/raw/emails.csv'  # Change this to your dataset filename
    output_file = 'data/processed/email_features.csv'
    
    # IMPORTANT: Adjust these column names to match your dataset
    # Common variations: 'text', 'email', 'message', 'content', 'body'
    # Common label variations: 'label', 'spam', 'class', 'category'
    text_column = 'text'      # Column containing email text
    label_column = 'label'    # Column containing spam/phishing label
    
    logger.info("Looking for dataset at: %s", input_file)
    logger.info("Text column: '%s'", text_column)
    logger.info("Label column: '%s'", label_column)
    
    # Step 1: Load dataset
    df = load_dataset(input_file)
    if df is None:
        logger.error("Please check your dataset path and try again.")
        return
    
    # Step 2: Show sample of raw data
    logger.info("Sample of raw data:\n%s", df.head(3).to_string(index=False))
    
    # Step 3: Process dataset
    features_df = process_dataset(df, text_column, label_column)
    
    # Step 4: Save features
    save_features(features_df, output_file)
    
    # Step 5: Display statistics
    display_statistics(features_df)
    
    # Step 6: Show sample of extracted features
    logger.info("Sample of extracted features:\n%s", features_df.head(3).to_string(index=False))
    logger.info("Feature extraction complete. Check the output file at: %s", output_file)


if __name__ == "__main__":
    main()
