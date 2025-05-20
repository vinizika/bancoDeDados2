-- listar eventos que ocorreram depois do dia 6 de janeiro de 2025
SELECT evento.nome, evento.data
FROM evento
WHERE data > '2025-06-01';