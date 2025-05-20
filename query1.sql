--listar eventos e quantidade de ingressos vendidos p cada
SELECT DISTINCT evento.nome, COUNT(ingresso.id_ingresso) AS total_ingressos
FROM evento
JOIN ingresso ON evento.id_evento = ingresso.id_evento
GROUP BY evento.nome
ORDER BY COUNT(ingresso.id_ingresso) DESC