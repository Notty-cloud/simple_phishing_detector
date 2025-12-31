# Project Outline: Email Phishing Detection Dataset Manager

## Core Features

### Minimum Viable Product (MVP)

1. **Load Public Dataset**
   - Why it's essential: Need data to work with
   - What it does: Read a public phishing email dataset (CSV format)
   - Example dataset: PhishTank, Kaggle phishing email datasets

2. **Extract Basic Features**
   - Why it's essential: Core learning objective - understanding what makes emails suspicious
   - What it does: Pull out key information from emails:
     - Email subject length
     - Number of URLs in email
     - Presence of suspicious keywords ("urgent", "verify account", "click here")
     - Sender domain (legitimate vs suspicious)

3. **Store Features in Organized Format**
   - Why it's essential: Creates usable output for future analysis
   - What it does: Save extracted features to a clean CSV or JSON file
   - Structure: One row per email with all features in columns

4. **Basic Statistics Display**
   - Why it's essential: Verify your feature extraction is working
   - What it does: Show simple counts:
     - Total emails processed
     - Number of phishing vs legitimate emails
     - Most common suspicious keywords found

### Nice-to-Have Features (Optional - Add Later)
- Email content word cloud visualization
- Export features to SQLite database instead of CSV
- Compare multiple datasets
- Simple web interface to upload and process new emails

---

## Tech Stack

### Programming Language
- **Language**: Python 3.x
- **Why chosen**: Best for data processing, has great libraries for text analysis

### Key Libraries
- **Pandas**: For reading and organizing data (CSV/Excel handling)
- **Re (Regular Expressions)**: For finding patterns (URLs, emails, keywords)
- **Collections**: For counting and organizing features
- **OS**: For file handling
- **Why chosen**: These are standard Python libraries - beginner-friendly and well-documented

### Data Storage
- **Input**: CSV files (public datasets)
- **Output**: CSV or JSON files (processed features)
- **Why chosen**: Simple file formats, no database server needed initially

### Development Tools
- **Editor**: VS Code or PyCharm
- **Version Control**: Git/GitHub
- **Python Environment**: Virtual environment (venv)

---

## Architecture or Flow

### System Architecture (Simple)
```
Public Dataset (CSV)
        ↓
   Python Script (Feature Extractor)
        ↓
  Processed Features (CSV/JSON)
        ↓
   Display Statistics (Console)
```

### Detailed Processing Flow
```
┌─────────────────────────┐
│  1. Load Dataset        │
│  (Read CSV file)        │
└───────────┬─────────────┘
            ↓
┌─────────────────────────┐
│  2. For Each Email:     │
│  - Extract subject      │
│  - Extract body text    │
│  - Extract sender       │
└───────────┬─────────────┘
            ↓
┌─────────────────────────┐
│  3. Feature Extraction: │
│  - Count URLs           │
│  - Find keywords        │
│  - Measure text length  │
│  - Check sender domain  │
└───────────┬─────────────┘
            ↓
┌─────────────────────────┐
│  4. Store Features      │
│  (Save to new CSV)      │
└───────────┬─────────────┘
            ↓
┌─────────────────────────┐
│  5. Display Summary     │
│  (Print statistics)     │
└─────────────────────────┘
```

### Example User Journey

**Step 1**: User downloads a phishing email dataset (e.g., from Kaggle)
**Step 2**: User places CSV file in `/data/raw/` folder
**Step 3**: User runs command: `python extract_features.py --input data/raw/emails.csv`
**Step 4**: Script processes each email and extracts features
**Step 5**: Script saves results to `/data/processed/email_features.csv`
**Step 6**: User sees summary printed:
```
Processed 1000 emails
Phishing emails: 523
Legitimate emails: 477
Top suspicious keywords: ['urgent', 'verify', 'account', 'click']
```

---

## Project Structure
```
phishing-feature-store/
│
├── README.md
├── Project Description.md
├── Project Outline.md
├── requirements.txt           # Python dependencies
│
├── data/
│   ├── raw/                  # Original datasets go here
│   └── processed/            # Extracted features saved here
│
├── src/
│   ├── load_data.py         # Reads CSV files
│   ├── extract_features.py  # Main feature extraction logic
│   ├── keywords.py          # List of suspicious keywords
│   └── utils.py             # Helper functions
│
├── notebooks/               # For testing (optional)
│   └── exploration.ipynb
│
└── outputs/
    └── statistics.txt       # Summary statistics
```

---

## Development Phases

### Phase 1: Setup & Data Loading (Days 1-3)
**Goal**: Get environment ready and load your first dataset

- Set up GitHub repository
- Create Python virtual environment
- Install required libraries (`pip install pandas`)
- Find and download a small phishing email dataset
- Write script to load CSV file and print first 5 rows
- **Success metric**: Can successfully load and display dataset

### Phase 2: Basic Feature Extraction (Days 4-8)
**Goal**: Extract your first features from emails

- Create function to count URLs in email text
- Create function to detect suspicious keywords
- Create function to calculate text length
- Test each function with sample emails
- **Success metric**: Can extract at least 3 features from one email

### Phase 3: Process Full Dataset (Days 9-12)
**Goal**: Process all emails and save results

- Write loop to process all emails in dataset
- Store extracted features in organized structure
- Save results to new CSV file
- Handle errors (missing data, weird formatting)
- **Success metric**: Can process 100+ emails without crashing

### Phase 4: Statistics & Documentation (Days 13-14)
**Goal**: Make it useful and presentable

- Calculate and display summary statistics
- Add comments to your code
- Write clear README with instructions
- Test with a different dataset
- **Success metric**: Someone else could use your tool

---

## Sample Features to Extract

### Email-Level Features
1. **Subject length** (number of characters)
2. **Body length** (number of words)
3. **Number of URLs** (count of http/https links)
4. **Has suspicious keywords** (Yes/No)
5. **Sender domain** (extract from email address)
6. **All caps percentage** (HOW MANY WORDS IN CAPS)
7. **Exclamation marks count** (!!!)
8. **Has dollar signs** ($ symbols present)

### Suspicious Keywords List (Examples)
```python
suspicious_keywords = [
    'urgent', 'verify', 'confirm', 'account', 
    'suspended', 'click here', 'act now',
    'congratulations', 'winner', 'prize',
    'password', 'security', 'update'
]
```

---

## Learning Goals

By completing this project, you will learn:

1. **Data Processing**: How to read, clean, and transform real-world datasets
2. **Feature Engineering**: Understanding what features help identify phishing
3. **Python Programming**: File I/O, loops, functions, string manipulation
4. **Problem Solving**: Handling messy data and edge cases
5. **Version Control**: Using Git/GitHub for project management
6. **Documentation**: Writing clear project descriptions

---

## Resources & Datasets

### Recommended Datasets (Free & Public)
1. **Kaggle - Email Phishing Dataset**
   - URL: kaggle.com/datasets (search "phishing email")
   - Size: ~1,000-5,000 emails
   - Format: CSV

2. **UCI Machine Learning Repository - SMS Spam**
   - Similar concept, good for practice
   - Smaller and simpler

3. **PhishTank**
   - Real phishing URLs
   - Good for URL-based features

### Helpful Tutorials
- Pandas documentation: pandas.pydata.org
- Python string methods: docs.python.org
- Regular expressions: regexone.com

---

## Success Criteria

Your project is complete when:
- ✅ Can load a dataset with 100+ emails
- ✅ Extracts at least 5 different features per email
- ✅ Saves processed features to a file
- ✅ Displays basic statistics
- ✅ Code is documented and on GitHub
- ✅ README explains how to run the project

---

## Future Enhancements (After 2-4 Weeks)

Once you master the basics, you could:
- Add actual machine learning model (scikit-learn)
- Build a simple web interface with Flask
- Create visualizations with matplotlib
- Implement real feature store concepts (versioning, serving)
- Process emails in real-time