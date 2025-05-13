--pegar usuarios que nunca compraram nenhum ingresso
SELECT usuario.nome
FROM usuario
LEFT JOIN pedido ON usuario.id_usuario = pedido.id_usuario
LEFT JOIN ingresso ON pedido.id_pedido = ingresso.id_pedido
WHERE ingresso.id_ingresso IS NULL;
