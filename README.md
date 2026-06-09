# Predicting Used Car Prices Using Machine Learning

## Project Creators
* **Antonio Venturini** - [LinkedIn Profile](https://www.linkedin.com/in/antonio-venturini-a34912138/)
* **Diego Vespa** - [LinkedIn Profile](https://www.linkedin.com/in/diego-vespa-55b970335/)
* **Roberto Karol Compagnone** - [LinkedIn Profile](https://www.linkedin.com/in/roberto-karol-compagnone-a05312414/)
* **Luigi Scalisi** - [LinkedIn Profile](https://www.linkedin.com/in/luigi-scalisi-8495ba286/)

## Project Overview
The primary objective of this project is to develop a robust predictive system capable of estimating the fair market value of a used car. By taking specific vehicle characteristics as input—such as manufacturer, model, year of registration, mileage, fuel type, and transmission—the system leverages a Machine Learning algorithm to deliver reliable, real-time price valuations.

To explore the core modeling process, please see the [Random Forest Notebook](random_forest.ipynb).

## Data Source
The dataset used to train the predictive model is sourced from Kaggle and consists of a comprehensive archive of real-world car advertisements scraped from Craigslist, reflecting the United States automotive market.
* **Dataset Link:** [Craigslist Cars & Trucks Data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data/data)

## Project Phases
The end-to-end development lifecycle is structured into three macro-phases:

### 1. Data Cleaning & Preprocessing
* **Feature Elimination:** Removed redundant or irrelevant columns that do not contribute to predictive power (e.g., `id`, `url`, unstructured text descriptions, and GPS coordinates).
* **Anomaly & Outlier Management:** Handled missing values and removed unrealistic data points or outliers (e.g., fraudulent listings with near-zero prices or impossible mileage parameters).
* **Feature Standardization:** Prepared features for modeling, including converting imperial units (miles) to metric (kilometers) where appropriate to ensure consistency.

### 2. Model Training & Optimization (Machine Learning)
* **Feature Engineering:** Applied encoding schemes (such as ordinal encoding) to transform non-numeric categorical variables (manufacturer, fuel type, transmission) into model-ready formats.
* **Data Splitting:** Partitioned the processed dataset into distinct training and testing subsets to ensure rigorous model validation.
* **Algorithm Selection & Tuning:** Trained and optimized regression models (including LightGBM and Random Forest) to accurately forecast the target variable (`price`).

### 3. Deployment & Valuation Interface
* **Dashboard Development:** Built a clean, intuitive, and interactive user interface using the **Streamlit** framework.
* **Real-time Inference:** Users can input their vehicle's specific attributes via dynamic forms to query the trained model and receive an instantaneous, data-driven price estimation.

## Data Dictionary
The finalized dataset utilized for model training comprises the following features:

* **`manufacturer`**: The automotive brand or maker of the vehicle (e.g., *Ford, Acura, Buick*).
* **`model`**: The specific model name of the car (e.g., *F-150, MDX, F-250 Super Duty*).
* **`year`**: The production or initial registration year of the vehicle.
* **`condition`**: The overall physical and mechanical state of the vehicle (e.g., *excellent, good*). Unreported values are categorized under *Unknown*.
* **`cylinders`**: The engine configuration denoted by the number of cylinders (e.g., *8 cylinders, 6 cylinders*).
* **`fuel`**: The fuel or power source type (e.g., *gas*, *diesel*, *electric*).
* **`odometer`**: The total distance traveled by the vehicle (mileage).
* **`title_status`**: The legal and bureaucratic status of the vehicle's title (e.g., a *clean* title indicates the vehicle is fully legal, with no history of being written off or severe salvage issues).
* **`transmission`**: The type of gearbox or transmission system (e.g., *automatic, manual, other*).
* **`drive`**: The drivetrain configuration (*fwd* = front-wheel drive, *rwd* = rear-wheel drive, *4wd* = four-wheel drive / all-wheel drive).
* **`size`**: The market-standard size classification of the vehicle (e.g., *full-size, mid-size, compact*).
* **`type`**: The body style or vehicle segment (e.g., *SUV, truck, pickup, sedan*).
* **`paint_color`**: The exterior color of the vehicle's bodywork.

## Application User Manual
The `app.py` file serves as the main application script, housing the operational logic and interface architecture for the predictive model. The graphical dashboard is powered by **Streamlit**.

### 1. Prerequisites and System Environment
Before launching the application, you must ensure that the trained model artifacts and encoders are present in the project's root directory. These files are vital for processing user inputs and executing real-time predictions:
* **`final_lightgbm_model.pkl`**: The optimized predictive model.
* **`final_ordinal_encoder.pkl`**: The trained categorical encoder.

⚠️ **Technical Requirements:** For a detailed breakdown of the required environment, including the mandatory Python version and specific package dependencies (such as Streamlit, LightGBM, and Pandas), please refer to the dedicated **[requirements.md](requirements.md)** file.

### 2. Launching the Application
Once the model files are in place and your environment is configured according to the requirements guide, navigate to the project directory using your terminal and execute the following command:

```bash
streamlit run app.py

