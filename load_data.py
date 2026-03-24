import duckdb

def load_json_to_duckdb():
    print("🦆 Odpalam silnik DuckDB...")
    
    # 1. Tworzymy plik bazy danych w naszym folderze 'data'
    # Jeśli plik nie istnieje, DuckDB sam go stworzy.
    db_path = 'data/pogoda.duckdb'
    conn = duckdb.connect(db_path)
    
    print("🏗️ Wrzucam surowy JSON do bazy...")
    
    # 2. Piszemy zapytanie SQL. 
    # Używamy magicznej funkcji read_json_auto, która sama domyśla się struktury JSON-a!
    # CREATE OR REPLACE sprawia, że jak odpalisz skrypt 10 razy, to nie wywali błędu, tylko nadpisze tabelę.
    query = """
    CREATE OR REPLACE TABLE raw_weather AS 
    SELECT * FROM read_json_auto('data/pogoda_krakow_surowa.json');
    """
    
    # Wykonujemy zapytanie
    conn.execute(query)
    
    # 3. Sprawdzamy co się stało (taki mały test dla nas)
    print("🔍 Sprawdzam kolumny w nowej tabeli:")
    
    # Wyciągamy WSZYSTKIE wyniki zapytania do zwykłej listy (fetchall)
    wynik = conn.execute("DESCRIBE raw_weather").fetchall()
    
    # Przelatujemy przez listę i drukujemy wiersz po wierszu
    for wiersz in wynik:
        print(wiersz)
    
    print(f"\n✅ Sukces! Baza danych została utworzona w pliku: {db_path}")
    
    # Zamykamy połączenie, żeby plik się zapisał na dysku
    conn.close()

if __name__ == "__main__":
    load_json_to_duckdb()