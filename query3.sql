--listar usuarios e forma de pagamento utilizado
SELECT pessoa.nome, compra.forma_pagamento
FROM pessoa
JOIN compra ON pessoa.id_pessoa = compra.id_pessoa;
