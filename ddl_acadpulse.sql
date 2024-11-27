
-- 1. Criar o Banco de Dados
CREATE DATABASE sistema_academia;

-- 2. Usar o Banco de Dados
USE sistema_academia;

-- 3. Tabela de Planos
CREATE TABLE planos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL,
    duracao INT NOT NULL
);

-- 4. Tabela de Alunos
CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    telefone VARCHAR(15),
    email VARCHAR(100) UNIQUE,
    plano_id INT,
    ativo BOOLEAN DEFAULT TRUE,
    data_matricula DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plano_id) REFERENCES planos(id)
);

-- 5. Tabela de Professores
CREATE TABLE professores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade ENUM('Musculação', 'Crossfit', 'Pilates', 'Outro') NOT NULL,
    telefone VARCHAR(15),
    email VARCHAR(100) UNIQUE
);

-- 6. Tabela de Treinos
CREATE TABLE treinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    professor_id INT,
    FOREIGN KEY (professor_id) REFERENCES professores(id)
);

-- 7. Tabela Associativa Alunos_Treinos
CREATE TABLE alunos_treinos (
    aluno_id INT,
    treino_id INT,
    PRIMARY KEY (aluno_id, treino_id),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (treino_id) REFERENCES treinos(id)
);

-- 8. Tabela de Pagamentos
CREATE TABLE pagamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    valor NUMERIC(10, 2) NOT NULL,
    data_pagamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);
