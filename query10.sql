--pegar quantidade de eventos que aconteceram em sp com mais de 3000 pessoas
SELECT evento.nome
FROM evento
JOIN local ON evento.id_local = local.id_local
WHERE local.cidade = 'São Paulo' AND local.capacidade > 3000;
