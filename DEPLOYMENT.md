# Deployment Guide (Public URL)

This project includes a Streamlit web app in `app.py`.

## Option A: Streamlit Community Cloud (Recommended)

1. Push this project to a GitHub repository.
2. Go to [https://share.streamlit.io](https://share.streamlit.io).
3. Click **New app**.
4. Select:
   - Repository: your repo
   - Branch: your default branch
   - Main file path: `app.py`
5. Click **Deploy**.
6. Streamlit will provide a public URL, typically:
   - `https://<app-name>.streamlit.app`

### Notes
- Ensure `requirements.txt` is committed.
- Ensure processed CSV files exist in `data/processed/` or configure your own data source path.

## Option B: Render

1. Push this project to GitHub.
2. Go to [https://render.com](https://render.com) -> **New Web Service**.
3. Connect the repository.
4. Use settings:
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
5. Deploy.
6. Render gives a public URL:
   - `https://<service-name>.onrender.com`

## Local Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open browser:
- [http://localhost:8501](http://localhost:8501)

## Troubleshooting

- If app shows missing data:
  - run `python main.py` to regenerate `data/processed/`
- If deployment fails:
  - verify `requirements.txt` includes `streamlit` and `plotly`
  - verify `app.py` exists at repo root
