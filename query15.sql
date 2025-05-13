--listar eventos que tiveram mais de 3 artistas diferentes
SELECT evento.nome
FROM evento
JOIN evento_artista ON evento.id_evento = evento_artista.id_evento
GROUP BY evento.nome
HAVING COUNT(DISTINCT evento_artista.id_artista) > 3;
