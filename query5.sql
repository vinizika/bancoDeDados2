--listar locais que ja ocorreram tipos de eventos diferentes
SELECT local.nome, count(evento.id_evento) as eventos
FROM local
JOIN evento ON local.id_local = evento.id_local
GROUP BY local.nome
HAVING count(evento.id_evento) > 1