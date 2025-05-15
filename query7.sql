--listar usuarios que utilizaram a showshow mais de 3 vezes
SELECT pessoa.nome
FROM pessoa
JOIN compra ON pessoa.id_pessoa = compra.id_pessoa
GROUP BY pessoa.nome
HAVING COUNT(DISTINCT compra.id_compra) > 3;

