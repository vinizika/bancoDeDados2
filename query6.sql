--listar locais que ja ocorreram tipos de eventos diferentes
SELECT local.nome
FROM local
JOIN evento ON local.id_local = evento.id_local
GROUP BY local.nome
HAVING COUNT(DISTINCT evento.tipo) > 1;
