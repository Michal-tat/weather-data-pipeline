## 🌤️ Weather Data Pipeline (ELT)
This project is a fully automated ELT data pipeline built using the Modern Data Stack. Instead of using heavy cloud tools, this project focuses on being lightweight and fast. It uses a "Medallion" architecture (Bronze -> Silver -> Gold) powered by DuckDB and dbt.

## 🛠️ Architecture & Tech Stack
* **Extract (Python + API):** Downloads historical weather data for Krakow from the free Open-Meteo API and saves it as a raw JSON file (Bronze Layer).
* **Load (DuckDB):** Loads the raw JSON file directly into DuckDB, a fast analytical database.
* **Transform (dbt - Data Build Tool):** * `stg_pogoda` (Silver Layer): Flattens the nested JSON data into a clean, hour-by-hour table.
  * `gold_statystyki_miesieczne` (Gold Layer): Aggregates the data into monthly summaries (max/min temperature, total rain) ready for BI dashboards.

## 🚀 How to Run It

1. Clone the repository and create a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Download data from the API and load it into DuckDB:

```bash
python extract_data.py
python load_data.py
```

3. Run the dbt transformations:

```bash
cd modele_pogodowe
dbt run
```
