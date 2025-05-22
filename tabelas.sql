-- Tabela de Pessoas
CREATE TABLE Pessoa (
    id_pessoa SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    cpf VARCHAR(14),
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
    FOREIGN KEY (id_local) REFERENCES Local(id_local)
);

-- Tabela de Compras
CREATE TABLE Compra (
    id_compra SERIAL PRIMARY KEY,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    forma_pagamento VARCHAR(50),
    id_pessoa INT,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);

-- Tabela de Ingressos
CREATE TABLE Ingresso (
    id_ingresso SERIAL PRIMARY KEY,
    tipo VARCHAR(50),
    preco DECIMAL(10,2),
    id_evento INT,
    id_categoria INT,
    id_compra INT,
    FOREIGN KEY (id_evento) REFERENCES Evento(id_evento),
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria),
    FOREIGN KEY (id_compra) REFERENCES Compra(id_compra)
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

-- Tabela de Evento_Pessoa (associativa N:N)
CREATE TABLE Evento_Pessoa (
    data_organizacao DATE,
    id_evento INT,
    id_organizador INT,
    PRIMARY KEY (id_evento, id_organizador),
    FOREIGN KEY (id_evento) REFERENCES Evento(id_evento),
    FOREIGN KEY (id_organizador) REFERENCES Pessoa(id_pessoa)
);
