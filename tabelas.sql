
-- Tabela de Pessoas
CREATE TABLE Pessoa (
    id_pessoa SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    cpf VARCHAR(14) UNIQUE,
    data_nascimento DATE
);

-- Tabela de Locais
CREATE TABLE Local (
    id_local SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(200),
    capacidade INT
);

-- Tabela de Categorias
CREATE TABLE Categoria (
    id_categoria SERIAL PRIMARY KEY,
    nome VARCHAR(50)
);

-- Tabela de Eventos
CREATE TABLE Evento (
    id_evento SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    data DATE,
    hora TIME,
    id_local INT,
    id_organizador INT,
    FOREIGN KEY (id_local) REFERENCES Local(id_local),
    FOREIGN KEY (id_organizador) REFERENCES Pessoa(id_pessoa)
);

-- Tabela de Ingressos
CREATE TABLE Ingresso (
    id_ingresso SERIAL PRIMARY KEY,
    tipo VARCHAR(50),
    preco DECIMAL(10,2),
    id_evento INT,
    id_categoria INT,
    FOREIGN KEY (id_evento) REFERENCES Evento(id_evento),
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

-- Tabela de Compras
CREATE TABLE Compra (
    id_compra SERIAL PRIMARY KEY,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    forma_pagamento VARCHAR(50),
    id_pessoa INT,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);

-- Tabela de Compra_Ingresso (associativa N:N)
CREATE TABLE Compra_Ingresso (
    id_compra INT,
    id_ingresso INT,
    quantidade INT,
    PRIMARY KEY (id_compra, id_ingresso),
    FOREIGN KEY (id_compra) REFERENCES Compra(id_compra),
    FOREIGN KEY (id_ingresso) REFERENCES Ingresso(id_ingresso)
);

-- Tabela de Artistas
CREATE TABLE Artista (
    id_artista SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    genero_musical VARCHAR(50)
);

-- Tabela de Evento_Artista (associativa N:N)
CREATE TABLE Evento_Artista (
    id_evento INT,
    id_artista INT,
    PRIMARY KEY (id_evento, id_artista),
    FOREIGN KEY (id_evento) REFERENCES Evento(id_evento),
    FOREIGN KEY (id_artista) REFERENCES Artista(id_artista)
);
