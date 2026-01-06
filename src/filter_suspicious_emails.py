#!/usr/bin/env python3
"""Filter and display rows that contain suspicious keywords.

This reads a CSV of features and outputs only rows where suspicious
keywords were detected (either `suspicious_keywords_found` non-empty
or `suspicious_keyword_count` > 0).

Usage:
  python src/filter_suspicious_emails.py data/processed/email_features.csv --output data/processed/suspicious_emails.csv --head
"""
from pathlib import Path
import pandas as pd
from logging_config import get_logger

logger = get_logger("filter_suspicious_emails")


def filter_suspicious(df: pd.DataFrame) -> pd.DataFrame:
    cols = df.columns
    mask = pd.Series(False, index=df.index)
    if "suspicious_keywords_found" in cols:
        s = df["suspicious_keywords_found"].fillna("").astype(str).str.strip()
        mask = mask | (s != "")
    if "suspicious_keyword_count" in cols:
        mask = mask | (df["suspicious_keyword_count"].fillna(0) != 0)
    return df.loc[mask]


def main():
    # Default path to the processed CSV inside the repository
    inp = Path(__file__).resolve().parents[1] / "data" / "processed" / "email_features.csv"
    if not inp.exists():
        raise SystemExit(f"Input file not found: {inp}")

    df = pd.read_csv(inp)

    # prepare columns
    s = df.get("suspicious_keywords_found", pd.Series([""] * len(df))).fillna("").astype(str).str.strip()
    counts = df.get("suspicious_keyword_count", pd.Series([0] * len(df))).fillna(0)

    mask = (s != "") | (counts != 0)
    filtered = df.loc[mask]

    total = len(df)
    n = len(filtered)
    logger.info("Found %d suspicious rows out of %d total rows", n, total)
    # Save filtered rows to a new CSV in the processed folder
    outp = Path(__file__).resolve().parents[1] / "data" / "processed" / "suspicious_keywords.csv"
    filtered.to_csv(outp, index=False)
    logger.info("Saved filtered rows to: %s", outp)

    # Print the suspicious keywords column values (or count if keywords column empty)
    for idx in filtered.index:
        val = s.loc[idx]
        if val != "":
            logger.info(val)
        else:
            logger.info("suspicious_keyword_count=%d", int(counts.loc[idx]))


if __name__ == "__main__":
    main()
