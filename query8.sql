--pegar usuarios que nunca compraram nenhum ingresso
WITH nao_compraram AS (
  SELECT p.nome
  FROM Pessoa p
  WHERE NOT EXISTS (
    SELECT 1
    FROM Compra c
    JOIN Ingresso i ON i.id_compra = c.id_compra
    WHERE c.id_pessoa = p.id_pessoa
  )
)
SELECT nome
FROM nao_compraram

UNION ALL

SELECT 'Todos os usuários compraram ao menos 1 ingresso' AS nome
WHERE NOT EXISTS (
  SELECT 1
  FROM nao_compraram
);