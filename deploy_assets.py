"""Download the large model and data files the dashboard needs (deployment only).

The trained models and processed data are too large for GitHub, so they live in a
Hugging Face model repository. They are downloaded once per server start into the
same paths the project uses locally.
"""
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
REPO_ID = 'HayaSaleh/saudi-property-price-prediction-files'
FILES = [line.strip() for line in (ROOT / 'deploy_files.txt').read_text(encoding='utf-8').splitlines()
         if line.strip()]


@st.cache_resource(show_spinner='Downloading the model and data files (first start only)…')
def ensure_assets():
    missing = [f for f in FILES if not (ROOT / f).exists()]
    if missing:
        from huggingface_hub import snapshot_download
        snapshot_download(REPO_ID, repo_type='model', local_dir=ROOT, allow_patterns=missing)
    still_missing = [f for f in FILES if not (ROOT / f).exists()]
    if still_missing:
        raise FileNotFoundError(f'Could not download: {still_missing}')
    return True
