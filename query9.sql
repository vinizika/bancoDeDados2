--pegar quantidade de eventos por tipo
SELECT tipo, COUNT(*) AS total
FROM evento
GROUP BY tipo;
