--listar eventos que ocorreram em locais que ja sediaram mais de 5 eventos
SELECT evento.nome
FROM evento
JOIN local ON evento.id_local = local.id_local
WHERE local.id_local IN (
  SELECT id_local
  FROM evento
  GROUP BY id_local
  HAVING COUNT(*) > 5
);
