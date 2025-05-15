--pegar usuarios que nunca id_compraram nenhum ingresso
SELECT pessoa.nome
FROM pessoa
LEFT JOIN compra ON pessoa.id_pessoa = compra.id_pessoa
LEFT JOIN compra_ingresso ON compra.id_compra = compra_ingresso.id_compra
WHERE compra_ingresso.id_ingresso IS NULL;

