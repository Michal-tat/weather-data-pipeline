{{ config(materialized='table') }}

WITH warstwa_silver AS (
    -- MAGICZNA SZTUCZKA DBT:
    -- Zamiast pisać nazwę tabeli na sztywno, używamy funkcji "ref".
    -- Dzięki temu dbt wie, że najpierw musi zbudować 'stg_pogoda', a dopiero potem ten plik!
    SELECT * FROM {{ ref('stg_pogoda') }}
)

SELECT
    -- Wyciągamy z daty sam Rok i Miesiąc (np. '2022-07')
    STRFTIME(data_i_godzina, '%Y-%m') AS rok_miesiac,
    
    -- Szukamy ekstremów i sumujemy opady. 
    -- ROUND zaokrągla nam wyniki do 1 miejsca po przecinku, żeby tabelka była śliczna.
    ROUND(MAX(temperatura_celsjusz), 1) AS max_temperatura_c,
    ROUND(MIN(temperatura_celsjusz), 1) AS min_temperatura_c,
    ROUND(AVG(temperatura_celsjusz), 1) AS srednia_temperatura_c,
    ROUND(SUM(opady_mm), 1) AS suma_opadow_mm

FROM warstwa_silver
-- Grupujemy po pierwszej kolumnie (rok_miesiac)
GROUP BY 1
-- Sortujemy od najnowszych miesięcy do najstarszych
ORDER BY 1 DESC