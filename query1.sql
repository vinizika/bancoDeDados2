--listar eventos e quantidade de ingressos vendidos p cada
SELECT evento.nome, SUM(compra_ingresso.quantidade) AS total_ingressos
FROM evento
JOIN ingresso ON evento.id_evento = ingresso.id_evento
JOIN compra_ingresso ON ingresso.id = compra_ingresso.id_ingresso
GROUP BY evento.nome;
