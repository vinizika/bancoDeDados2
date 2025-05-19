--listar locais que ja ocorreram tipos de eventos diferentes
SELECT local.nome
FROM local
JOIN evento ON local.id_local = evento.id_local
JOIN ingresso ON evento.id_evento = ingresso.id_evento
GROUP BY local.nome
HAVING COUNT(DISTINCT ingresso.tipo) > 1;

