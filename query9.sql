--pegar quantidade de eventos por tipo de setor
SELECT categoria.nome AS tipo, COUNT(DISTINCT evento.id_evento) AS total
FROM evento
JOIN ingresso ON evento.id_evento = ingresso.id_evento
JOIN categoria ON ingresso.id_categoria = categoria.id_categoria
GROUP BY categoria.nome;


