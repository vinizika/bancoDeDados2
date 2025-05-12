--listar eventos ocorrendo em sp
SELECT evento.nome, local.nome, local.endereco
FROM evento
JOIN local ON evento.id_local = local.id_local
WHERE local.endereco LIKE '%São Paulo%';
