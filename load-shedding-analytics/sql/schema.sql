-- schema.sql
-- Defines the structure of the load_shedding.db SQLite database.

DROP TABLE IF EXISTS load_shedding_daily;

CREATE TABLE load_shedding_daily (
    date        TEXT PRIMARY KEY,      -- YYYY-MM-DD
    year        INTEGER NOT NULL,
    month       INTEGER NOT NULL,
    stage       INTEGER NOT NULL CHECK (stage BETWEEN 0 AND 8),
    hours_shed  REAL NOT NULL,
    season      TEXT NOT NULL CHECK (season IN ('winter', 'summer')),
    -- Illustrative estimate: assumes a small business loses roughly R850 in
    -- revenue per hour without power (till systems, card machines, stock
    -- spoilage, lost foot traffic). This is a documented, adjustable
    -- assumption, not a claimed real figure - see README for reasoning.
    est_business_cost_zar REAL NOT NULL
);
