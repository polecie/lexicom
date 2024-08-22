EXPLAIN ANALYZE CREATE TEMPORARY TABLE temp_full_names AS
SELECT
    name,
    REGEXP_REPLACE(name, '\.[^.]+$', '') AS short_name,
    status
FROM full_names;

CREATE INDEX idx_temp_full_names_short_name ON temp_full_names (short_name);

EXPLAIN ANALYZE UPDATE full_names f
SET status = s.status
FROM short_names s
JOIN temp_full_names t ON t.short_name = s.name
WHERE f.name = t.name AND f.status != s.status;

DROP TABLE temp_full_names;
