--listar usuarios que utilizaram a showshow mais de 3 vezes
SELECT pessoa.nome, COUNT(DISTINCT compra.id_compra) as quantidade_compras
FROM pessoa
JOIN compra ON pessoa.id_pessoa = compra.id_pessoa
GROUP BY pessoa.nome
HAVING COUNT(DISTINCT compra.id_compra) > 3
ORDER BY COUNT(DISTINCT compra.id_compra) DESC