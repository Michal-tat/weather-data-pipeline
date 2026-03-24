{{ config(materialized='table') }}

WITH surowe_dane AS (
    -- Pobieramy dane z naszej brzydkiej tabeli, którą stworzył Python
    SELECT * FROM raw_weather
)

SELECT
    -- Używamy magicznej funkcji UNNEST, żeby "rozpakować" te długie listy z JSON-a
    -- i robimy z nich zwykłe kolumny wiersz po wierszu.
    CAST(UNNEST(hourly.time) AS TIMESTAMP) AS data_i_godzina,
    CAST(UNNEST(hourly.temperature_2m) AS DOUBLE) AS temperatura_celsjusz,
    CAST(UNNEST(hourly.precipitation) AS DOUBLE) AS opady_mm

FROM surowe_dane