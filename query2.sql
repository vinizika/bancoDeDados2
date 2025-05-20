--listar eventos que a capacidade é maior que 100000

SELECT distinct evento.nome, local.capacidade
FROM evento
JOIN local ON evento.id_local = local.id_local
WHERE local.capacidade > 100000
ORDER BY local.capacidade DESC