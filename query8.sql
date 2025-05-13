-- pegar todos as compras que incluem mais de 2 ingressos
SELECT pedido.id_pedido
FROM pedido
JOIN ingresso ON pedido.id_pedido = ingresso.id_pedido
GROUP BY pedido.id_pedido
HAVING COUNT(ingresso.id_ingresso) > 2;
