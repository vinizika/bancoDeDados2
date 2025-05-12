-- listar eventos que ocorreram depois do dia 6 de janeiro de 2025
SELECT ingresso.*
FROM ingresso
JOIN evento ON ingresso.id_evento = evento.id_evento
WHERE evento.data > '2025-06-01';
