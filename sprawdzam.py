import duckdb

print("🦆 Łączę się z bazą DuckDB...")
conn = duckdb.connect('data/pogoda.duckdb')

print("\n🏆 WARSTWA GOLD: Statystyki Miesięczne dla Krakowa 🏆")
wynik = conn.execute("SELECT * FROM gold_statystyki_miesieczne LIMIT 12").fetchall()

# Nagłówki
print(f"{'Miesiąc':<10} | {'Max Temp (°C)':<15} | {'Min Temp (°C)':<15} | {'Średnia (°C)':<15} | {'Suma opadów (mm)'}")
print("-" * 80)

for wiersz in wynik:
    print(f"{str(wiersz[0]):<10} | {str(wiersz[1]):<15} | {str(wiersz[2]):<15} | {str(wiersz[3]):<15} | {str(wiersz[4])}")