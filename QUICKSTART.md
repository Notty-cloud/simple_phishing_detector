# 🚀 QUICK START GUIDE

## Get Running in 5 Minutes!

### 1️⃣ Install Python Packages
```bash
pip install pandas numpy
```

### 2️⃣ Create Sample Data (for testing)
```bash
cd phishing-feature-store/src
python create_sample_data.py
```

### 3️⃣ Run Feature Extraction
```bash
python extract_features.py
```

### 4️⃣ Check Your Results
Look in the `data/processed/` folder for `email_features.csv`

---

## Using Real Datasets

### Best Datasets for Beginners:

1. **Kaggle - Spam Mails Dataset**
   - URL: https://www.kaggle.com/datasets/venky73/spam-mails-dataset
   - Size: 5,000+ emails
   - Easy format

2. **UCI SMS Spam Collection**
   - URL: https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
   - Size: 5,500+ messages
   - Good for practice

3. **Enron Email Dataset (Advanced)**
   - URL: https://www.kaggle.com/datasets/wcukierski/enron-email-dataset
   - Size: 500,000+ emails
   - More realistic but larger

### After Downloading:
1. Place CSV file in `data/raw/` folder
2. Rename to `emails.csv` (or update filename in script)
3. Run `python extract_features.py`

---

## Troubleshooting

**Q: "Module not found" error**
A: Run `pip install pandas numpy`

**Q: "File not found" error**
A: Make sure CSV is in `data/raw/` folder

**Q: Column name errors**
A: Edit lines 256-257 in `extract_features.py` to match your CSV columns

---

## What Each File Does

- `keywords.py` - List of suspicious words to detect
- `extract_features.py` - Main script that processes emails
- `create_sample_data.py` - Creates test data
- `requirements.txt` - Python packages needed

---

**Need Help?** Check the main README.md for detailed instructions!
