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
02. Listar eventos que possuem capacidade maior que 100000.<br>
03. Listar usuários e forma de pagamento utilizado na sua compra.<br>
04. Listar eventos que ocorreram depois do dia 6 de janeiro de 2025.<br>
05. Listar locais que ja ocorreram tipos de eventos diferentes.<br>
06. Listar usuários que utilizaram a ShowShow mais de 3 vezes.<br>
07. Listar quantidade de eventos por tipo de setor.<br>
08. Listar usuários que nunca compraram nenhum ingresso. Se todos tiverem ingresso, é avisado.<br>
09. Listar os nomes dos artistas que se apresentaram em eventos realizados em locais com capacidade superior a 100.000 pessoas, informando também a maior capacidade de local em que cada artista já se apresentou.<br>
10. Listar artistas que ja fizeram show mais de 1 vez no mesmo lugar.<br>

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
- Com as informações já dentro do banco de dados, vá até o SQL Editor munido das 10 queries feitas por nós e disponibilizadas no github.
- Execute query por query e confira o resultado. Perceba que todas as queries já estão ajustadas para a lógica utilizada na inserção dos dados.

# MR E MER

![image](https://github.com/user-attachments/assets/fbcd49c6-b5e5-4f19-a9c4-9e0d4ab527ae)
![image](https://github.com/user-attachments/assets/6fa1a3c6-683d-4370-95d2-40cb6225b840)







