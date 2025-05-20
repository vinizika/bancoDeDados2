--listar artistas que ja fizeram show mais de 1 vez no mesmo lugar
SELECT distinct artista.nome
FROM artista
JOIN evento_artista ON artista.id_artista = evento_artista.id_artista
JOIN evento ON evento_artista.id_evento = evento.id_evento
GROUP BY artista.nome, evento.id_local
HAVING COUNT(*) > 1;
