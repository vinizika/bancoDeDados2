# Nome e R.A:
Julian Ryu Takeda 22.224.030-1 <br>
Manuella Filipe Peres 22.224.029-3 <br>
Vinicius de Castro Duarte 22.224.020-2

# Descrição do projeto
Para o desenvolvimento do projeto, utilizamos a plataforma de banco de dados em nuvem Supabase, conforme demonstrado durante as aulas.<br>
A geração de dados aleatórios para inserção no banco foi feita com o auxílio da linguagem Python.<br><br>
O projeto simula um sistema de banco de dados para um site de venda de ingressos, contendo informações como o tipo de evento, data e horário, a quantidade de ingressos disponíveis, os artistas que irão se apresentar, os locais dos shows, entre outros dados essenciais para o processo de comercialização de ingressos.<br><br>
Todos esses dados foram criados por meio de consultas SQL integradas a um script em Python, o qual gerou informações fictícias tanto sobre os eventos quanto sobre os compradores.<br>
Entre os dados gerados estão: nome e sobrenome dos usuários, artistas, gêneros musicais, localizações, descrições e títulos dos eventos.<br>
Dessa forma, todas as tabelas se relacionam entre si, possibilitando que o sistema funcione de maneira completa e coerente.<br><br>
Durante a modelagem relacional, sempre tivemos em mente o produto final.<br>
Assim, buscamos garantir que todas as informações estivessem facilmente acessíveis, evitando estruturas complexas que exigissem muitos 'joins'.<br>
Também seguimos os princípios da Terceira Forma Normal (3FN), alinhando o projeto às boas práticas abordadas na disciplina.

# Códigos
## Main.py
Esse código serve para randomizar a entrada de dados e também, no final, a validação dos mesmos.<br>

### Como eles funcionam?
O código se inicia deletando todos os dados disponíveis nas tabelas. Em seguida, inserimos as informações em uma ordem lógica e otimizada. Por último, validamos os dados que foram inseridos, tendo certeza que tudo ocorreu bem. 

## tabelas.sql
Esse é o programa onde serão criadas as tabelas dentro do banco de dados. Todas as tabelas e colunas já serão criadas automaticamente.

<h2>Queries</h2>
Querys em SQL utilizadas para o desenvolvimento do projeto:<br>
01. Listar eventos e quantidade de ingressos vendidos para cada.<br>
02. Listar eventos que possuem capacidade maior que 5000.<br>
03. Listar usuários e forma de pagamento utilizado na sua compra.<br>
04. Listar eventos ocorrendo na cidade de São Paulo.<br>
05. Listar eventos que ocorreram depois do dia 6 de janeiro de 2025.<br>
06. Listar locais que ja ocorreram tipos de eventos diferentes.<br>
07. Listar usuários que utilizaram a ShowShow (site de compras de ingresso proposta) mais de 3 vezes.<br>
08. Listar todas as compras que incluem mais de 2 ingressos.<br>
09. Listar quantidade de eventos por tipo.<br>
10. Listar quantidade de eventos que aconteceram em São Paulo com mais de 3000 pessoas.<br>
11. Listar usuários que nunca compraram nenhum ingresso.<br>
12. Listar eventos que ocorreram em locais que ja sediaram mais de 5 eventos.<br>
13. Listar nome dos artistas que participaram de eventos realizados em locais com capacidade superior a 5000.<br>
14. Listar artistas que ja fizeram show mais de 2 vezes no mesmo lugar.<br>
15. Listar eventos que tiveram mais de 3 artistas diferentes.<br>

# Descrição de como executar o projeto
## Pré-requisitos:<br>
- Ter uma conta válida no supabase;<br>
- Ter um projeto vazio e válido criado;<br>
- Ter em mãos o SUPABASE_URL e o SUPABASE_KEY do projeto (dashboard -> settings -> Data API)<br>

## Primeiros passos:<br>
- Execute no terminal do computador (cmd) o comando: <strong>pip install supabase</strong> (nos computadores da FEI a conexão com a API não funciona por restrições de software entre as conexões)<br>
- Modifique as informações URL e KEY, no início do projeto, para as do seu database.<br>

## Passo a passo
- Execute o arquivo tabelas.sql dentro do SQL Editor, no supabase. Esse arquivo contém a criação de todas as nossas tabelas e colunas inseridas nelas. <br>
- Após a sua execução, execute o código em Python dentro da IDE preferida (como VSCODE). Acompanhe a execução através do terminal.
- Confirme, nas últimas execuções, a validação dos dados. O programa exibe, através do terminal, se os dados estão de acordo com o necessário ou não.
- Com as informações já dentro do banco de dados, vá até o SQL Editor munido das 15 queries feitas por nós e disponibilizadas no github.
- Execute query por query e confira o resultado. Perceba que todas as queries já estão ajustadas para a lógica utilizada na inserção dos dados.

# MR E MER
![image](https://github.com/user-attachments/assets/2d1e5bea-9315-47c3-8466-f22a56da4f1d)
![image](https://github.com/user-attachments/assets/5a48f861-9041-4a77-b8cb-0da4c2750e61)




