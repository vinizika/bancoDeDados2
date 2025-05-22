--listar artistas que ja fizeram show mais de 1 vez no mesmo lugar
SELECT 
    artista.nome AS nome_artista,
    local.nome AS nome_local,
    COUNT(*) AS quantidade_eventos
FROM artista
JOIN evento_artista ON artista.id_artista = evento_artista.id_artista
JOIN evento ON evento_artista.id_evento = evento.id_evento
JOIN local ON evento.id_local = local.id_local
GROUP BY artista.nome, local.nome
HAVING COUNT(*) > 1;
