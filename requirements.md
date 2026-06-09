# Project Requirements

This document lists the environment and libraries necessary to run the web application and, optionally, to explore or retrain the Machine Learning models.

## Base Environment
* **Python**: Version 3.8 or higher.

## Application Execution (app.py)
To properly run the Streamlit interface and generate car price predictions, the following libraries are strictly required:

* `streamlit`
* `pandas`
* `joblib`

*(Note: the `json` and `urllib.request` modules are part of the Python Standard Library, so they are already integrated and do not require any installation via pip).*

**Quick installation command:**
```bash
pip install streamlit pandas joblib