--nome dos artistas que participaram de eventos realizados em locais com capacidade superior a 5000
SELECT DISTINCT artista.nome
FROM artista
JOIN evento_artista ON artista.id_artista = evento_artista.id_artista
JOIN evento ON evento_artista.id_evento = evento.id_evento
JOIN local ON evento.id_local = local.id_local
WHERE local.capacidade > 5000;
