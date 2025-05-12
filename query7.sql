--listar usuarios que utilizaram a showshow mais de 3 vezes
SELECT usuario.nome
FROM usuario
JOIN pedido ON usuario.id_usuario = pedido.id_usuario
GROUP BY usuario.nome
HAVING COUNT(DISTINCT pedido.id_pedido) > 3;
