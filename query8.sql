-- pegar todos as compras que incluem mais de 2 ingressos
SELECT compra.id_compra
FROM compra
JOIN compra_ingresso ON compra.id_compra = compra_ingresso.id_compra
GROUP BY compra.id_compra
HAVING COUNT(compra_ingresso.id_ingresso) > 2;

