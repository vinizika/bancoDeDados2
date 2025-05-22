-- artistas que participaram de eventos em locais com capacidade superior a 100000, retornando o valor da maior capacidade
SELECT DISTINCT artista.nome, MAX(local.capacidade) as maior_capacidade
FROM artista
JOIN evento_artista ON artista.id_artista = evento_artista.id_artista
JOIN evento ON evento_artista.id_evento = evento.id_evento
JOIN local ON evento.id_local = local.id_local
WHERE local.capacidade > 100000
GROUP BY artista.nome
ORDER BY MAX(local.capacidade) DESC
