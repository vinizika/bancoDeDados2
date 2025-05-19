--listar artistas que ja fizeram show mais de 2 vezes no mesmo lugar
SELECT artista.nome
FROM artista
JOIN evento_artista ON artista.id_artista = evento_artista.id_artista
JOIN evento ON evento_artista.id_evento = evento.id_evento
GROUP BY artista.nome, evento.id_local
HAVING COUNT(*) > 1;
