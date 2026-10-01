# Saudi Property Transaction Price Prediction: Dashboard

Interactive Streamlit dashboard for a data science capstone project on 1.39 million Saudi Ministry of
Justice property sales (2020–2025). The final model is a Ridge stack of tuned XGBoost and CatBoost,
selected on 2024 data and evaluated on 2025 sales: its mean absolute error is 22.69% lower than a
historical-median baseline.

Pages: Home · Dataset Overview · Exploratory Analysis · Model Performance · Price Prediction · Methodology.

**Team:** Haya Alharthi, Dana Alrabea, Mshari Yehya, Omar Alhejaili.

## Deployment

This repository contains the dashboard code and small result tables. The trained models and processed
data are too large for GitHub; they are stored in the Hugging Face model repository
[HayaSaleh/saudi-property-price-prediction-files](https://huggingface.co/HayaSaleh/saudi-property-price-prediction-files)
and downloaded automatically on first start (`deploy_assets.py`, file list in `deploy_files.txt`).

Run locally:

```bash
pip install -r requirements.txt
python -m streamlit run demo/app.py
```

On Streamlit Community Cloud, set the main file to `demo/app.py` and Python to 3.10.

## Data source

Ministry of Justice, Kingdom of Saudi Arabia, real estate transactions open data, obtained through the
[Saudi Real Estate Open Data](https://github.com/civillizard/Saudi-Real-Estate-Data) repository
(KSA Open Data License).

Estimates are for demonstration and decision support only; they are not a professional valuation.
