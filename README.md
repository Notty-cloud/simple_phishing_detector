# Simple Phishing Detector

Lightweight repository for extracting phishing-related features from email text and filtering suspicious emails.

Contents
- `src/create_sample_data.py` — (existing) helper to create sample email data.
- `src/extract_features.py` — extracts features into `data/processed/email_features.csv`.
- `src/keywords.py` — (existing) suspicious keyword lists and helpers.
- `src/filter_suspicious_emails.py` — filters rows containing suspicious keywords and writes `data/processed/suspicious_keywords.csv`.
- `src/logging_config.py` — centralized logging helper (creates `logs/` and per-module log files).

Quickstart

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create or place your raw emails at `data/raw/emails.csv` (columns: `text`, optional `label`).

3. Extract features:

```bash
python src/extract_features.py
# output: data/processed/email_features.csv
```

4. Filter suspicious emails (script also runs automatically and writes a CSV):

```bash
python src/filter_suspicious_emails.py
# output: data/processed/suspicious_keywords.csv
```

Logging
- Log files are written to `logs/` using per-module log filenames, e.g. `logs/extract_features.log` and `logs/filter_suspicious_emails.log`.

Notes
- `extract_features.py` uses `src/keywords.py` to detect suspicious keywords. Adjust `text_column` and `label_column` variables inside the script if your CSV uses different column names.
- The filter script looks for `suspicious_keywords_found` and `suspicious_keyword_count` columns in `data/processed/email_features.csv`.

License & Next steps
- Add a LICENSE file if you plan to publish this repository publicly.
- I can open a PR, create a release tag, or add CI if you want — tell me which.
# Email Phishing Feature Extractor

A beginner-friendly Python project that extracts features from email datasets to identify potential phishing attempts.

## 🎯 What This Does

This tool:
- Loads email datasets (CSV format)
- Extracts useful features like URL counts, suspicious keywords, text length
- Saves processed features for analysis
- Displays statistics about the dataset

## 📁 Project Structure

```
phishing-feature-store/
├── data/
│   ├── raw/              # Put your CSV dataset here
│   └── processed/        # Extracted features saved here
├── src/
│   ├── extract_features.py   # Main script
│   ├── keywords.py           # Suspicious keyword list
│   └── create_sample_data.py # Creates test dataset
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

### Step 1: Install Requirements

```bash
pip install pandas numpy
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

### Step 2: Get a Dataset

**Option A: Use Sample Data (Fastest)**
```bash
python create_sample_data.py
```
This creates a small test dataset with 20 emails.

**Option B: Download Real Dataset (Recommended)**

1. Go to Kaggle: https://www.kaggle.com/datasets/venky73/spam-mails-dataset
2. Download the CSV file
3. Place it in `data/raw/` folder
4. Rename it to `emails.csv` (or update the filename in `extract_features.py`)

### Step 3: Run Feature Extraction

```bash
python extract_features.py
```

### Step 4: Check Results

Look for the output file at: `data/processed/email_features.csv`

## 📊 Features Extracted

The script extracts these features from each email:

| Feature | Description |
|---------|-------------|
| `text_length` | Number of characters in email |
| `word_count` | Number of words in email |
| `url_count` | How many URLs/links found |
| `suspicious_keyword_count` | Count of phishing keywords |
| `capital_letter_percent` | Percentage of CAPITAL LETTERS |
| `exclamation_count` | Number of ! marks |
| `has_dollar_signs` | Contains $ symbol (1=yes, 0=no) |
| `suspicious_keywords_found` | List of specific keywords detected |
| `is_phishing` | Label (1=phishing, 0=legitimate) |

## 🔧 Customizing for Your Dataset

If your CSV has different column names, edit `extract_features.py`:

```python
# Line 256-257 - Update these to match your dataset
text_column = 'text'      # Your email content column
label_column = 'label'    # Your label column (spam/ham, 0/1, etc.)
```

Common column name variations:
- Text: `text`, `email`, `message`, `content`, `body`, `email_text`
- Label: `label`, `spam`, `class`, `category`, `type`, `is_spam`

## 📈 Example Output

```
==================================================
DATASET STATISTICS
==================================================

Total emails processed: 1000
Phishing emails: 523
Legitimate emails: 477

--- Feature Statistics ---
Average text length: 245 characters
Average word count: 42 words
Average URLs per email: 1.3
Average suspicious keywords: 2.1
Average capital letter %: 8.5%

--- Top 10 Suspicious Keywords Found ---
  'urgent': 156 times
  'verify': 134 times
  'click here': 98 times
  'account': 87 times
  'confirm': 72 times
```

## 🧪 Testing the Code

Want to test if everything works?

1. Run the sample data creator:
```bash
python create_sample_data.py
```

2. Run feature extraction:
```bash
python extract_features.py
```

3. You should see statistics and a new CSV file in `data/processed/`

## 🐛 Troubleshooting

**Problem: "File not found" error**
- Make sure your CSV file is in `data/raw/` folder
- Check that the filename matches in `extract_features.py`

**Problem: "KeyError: 'text'" or column not found**
- Your CSV has different column names
- Update `text_column` and `label_column` variables (see Customizing section above)

**Problem: Script runs but no output**
- Check if `data/processed/` folder was created
- Look for error messages in the console

## 📚 Learning Resources

- **Pandas Tutorial**: https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- **Regular Expressions**: https://regexone.com/
- **Feature Engineering**: https://www.kaggle.com/learn/feature-engineering

## 🎓 What's Next?

Once you're comfortable with this:
1. Add more sophisticated features (email sender reputation, link analysis)
2. Build a simple machine learning model using scikit-learn
3. Create visualizations with matplotlib
4. Build a web interface with Flask

## 📝 License

This is a learning project - feel free to use and modify as needed!

## 🤝 Contributing

This is a beginner project! Feel free to:
- Add more suspicious keywords
- Create new feature extraction functions
- Improve the documentation
- Share your datasets (if publicly available)

## ⚠️ Important Notes

- This is for learning purposes - not production-ready
- Real phishing detection requires machine learning models
- Always respect privacy when working with email data
- Use only public datasets for learning

---

**Happy Learning! 🚀**

Questions? Check the code comments or reach out for help!
