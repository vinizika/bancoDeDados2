--listar eventos que a capacidade é maior que 5000

SELECT evento.nome, local.nome, local.capacidade
FROM evento
JOIN local ON evento.id_local = local.id_local
WHERE local.capacidade > 5000;
