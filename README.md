# 🌤️ Weather Data Pipeline (ELT)

Ten projekt to w pełni zautomatyzowany rurociąg danych (pipeline) w architekturze ELT, zbudowany w oparciu o **Modern Data Stack**. Zamiast ciężkich rozwiązań chmurowych, projekt stawia na lekkość, szybkość i architekturę "Medalionową" (Bronze -> Silver -> Gold) z wykorzystaniem DuckDB i dbt.

## 🛠️ Architektura i Technologie
* **Extract (Python + API):** Pobieranie historycznych danych pogodowych dla Krakowa z darmowego API Open-Meteo i zapis do surowego pliku JSON (Warstwa Bronze).
* **Load (DuckDB):** Załadowanie surowego pliku JSON bezpośrednio do nowoczesnej, analitycznej bazy danych DuckDB.
* **Transform (dbt - Data Build Tool):** * `stg_pogoda` (Warstwa Silver): Rozpakowanie (unnest) zagnieżdżonego JSON-a na płaską tabelę ułożoną godzina po godzinie.
  * `gold_statystyki_miesieczne` (Warstwa Gold): Agregacja danych do poziomu miesięcznych podsumowań (max/min temperatura, suma opadów), gotowych pod dashboardy BI.

## 🚀 Jak to uruchomić?

1. Sklonuj repozytorium i stwórz środowisko wirtualne:
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

2. Pobierz dane z API i załaduj do bazy DuckDB:

python extract_data.py
python load_data.py

3. Uruchom transformacje dbt:

cd modele_pogodowe
dbt run