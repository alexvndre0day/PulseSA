INSERT INTO planos (nome, preco, duracao) VALUES
('Plano Mensal', 100.00, 1),
('Plano Trimestral', 250.00, 3),
('Plano Anual', 900.00, 12);

-- Inserindo 100 alunos com nomes únicos
INSERT INTO alunos (nome, data_nascimento, telefone, email, plano_id) VALUES
('João Silva', '1990-04-15', '11987654321', 'joao.silva@email.com', 1),
('Maria Oliveira', '1992-06-10', '11987654322', 'maria.oliveira@email.com', 2),
('Carlos Souza', '1993-08-20', '11987654323', 'carlos.souza@email.com', 3),
('Ana Costa', '1989-11-05', '11987654324', 'ana.costa@email.com', 1),
('Lucas Pereira', '1991-02-25', '11987654325', 'lucas.pereira@email.com', 2),
('Juliana Ribeiro', '1994-03-12', '11987654326', 'juliana.ribeiro@email.com', 3),
('Ricardo Almeida', '1988-09-30', '11987654327', 'ricardo.almeida@email.com', 1),
('Fernanda Silva', '1995-07-01', '11987654328', 'fernanda.silva@email.com', 2),
('Eduardo Oliveira', '1990-12-11', '11987654329', 'eduardo.oliveira@email.com', 3),
('Camila Martins', '1992-01-10', '11987654330', 'camila.martins@email.com', 1),
('Gustavo Costa', '1991-05-22', '11987654331', 'gustavo.costa@email.com', 2),
('Patrícia Santos', '1987-03-14', '11987654332', 'patricia.santos@email.com', 3),
('Rafael Souza', '1993-11-08', '11987654333', 'rafael.souza@email.com', 1),
('Beatriz Oliveira', '1990-02-20', '11987654334', 'beatriz.oliveira@email.com', 2),
('Mariana Costa', '1992-09-13', '11987654335', 'mariana.costa@email.com', 3),
('Lucas Alves', '1991-06-18', '11987654336', 'lucas.alves@email.com', 1),
('Juliano Pereira', '1994-05-05', '11987654337', 'juliano.pereira@email.com', 2),
('Claudia Mendes', '1989-10-29', '11987654338', 'claudia.mendes@email.com', 3),
('Felipe Rocha', '1992-12-19', '11987654339', 'felipe.rocha@email.com', 1),
('Sofia Martins', '1991-04-17', '11987654340', 'sofia.martins@email.com', 2),
('Bruno Santana', '1987-08-25', '11987654341', 'bruno.santana@email.com', 1),
('Roberta Lima', '1993-07-10', '11987654342', 'roberta.lima@email.com', 3),
('Eduardo Torres', '1990-11-14', '11987654343', 'eduardo.torres@email.com', 2),
('Lúcia Almeida', '1995-09-17', '11987654344', 'lucia.almeida@email.com', 1),
('Marcos Vieira', '1992-05-03', '11987654345', 'marcos.vieira@email.com', 2),
('Cristina Pires', '1991-08-08', '11987654346', 'cristina.pires@email.com', 3),
('Rogério Silva', '1990-01-12', '11987654347', 'rogerio.silva@email.com', 1),
('Tatiane Oliveira', '1993-10-01', '11987654348', 'tatiane.oliveira@email.com', 2),
('Denis Costa', '1989-04-20', '11987654349', 'denis.costa@email.com', 3),
('Vanessa Souza', '1992-02-15', '11987654350', 'vanessa.souza@email.com', 1),
('Aline Gomes', '1991-12-11', '11987654351', 'aline.gomes@email.com', 2),
('Giovana Lima', '1990-06-25', '11987654352', 'giovana.lima@email.com', 3),
('Carlos Martins', '1994-01-10', '11987654353', 'carlos.martins@email.com', 1),
('Ester Mendes', '1991-03-15', '11987654354', 'ester.mendes@email.com', 2),
('Julio Cesar', '1988-10-25', '11987654355', 'julio.cesar@email.com', 3),
('Daniele Costa', '1993-05-07', '11987654356', 'daniele.costa@email.com', 1),
('Guilherme Pereira', '1991-07-28', '11987654357', 'guilherme.pereira@email.com', 2),
('Luana Ribeiro', '1992-08-16', '11987654358', 'luana.ribeiro@email.com', 3),
('Rita Oliveira', '1990-02-04', '11987654359', 'rita.oliveira@email.com', 1),
('Nina Souza', '1994-09-11', '11987654360', 'nina.souza@email.com', 2),
('Célia Martins', '1991-04-14', '11987654361', 'celia.martins@email.com', 3),
('Diana Rocha', '1990-07-21', '11987654362', 'diana.rocha@email.com', 1),
('André Costa', '1993-02-08', '11987654363', 'andre.costa@email.com', 2),
('Carla Almeida', '1992-10-30', '11987654364', 'carla.almeida@email.com', 3),
('Fernando Souza', '1990-09-17', '11987654365', 'fernando.souza@email.com', 1),
('Daniela Lima', '1993-06-22', '11987654366', 'daniela.lima@email.com', 2),
('Fábio Oliveira', '1992-11-18', '11987654367', 'fabio.oliveira@email.com', 3),
('Raquel Silva', '1991-01-05', '11987654368', 'raquel.silva@email.com', 1),
('Paulo Pereira', '1994-12-24', '11987654369', 'paulo.pereira@email.com', 2),
('Vera Rocha', '1989-07-14', '11987654370', 'vera.rocha@email.com', 3),
('Jéssica Costa', '1991-10-02', '11987654371', 'jessica.costa@email.com', 1),
('Marcelo Santos', '1992-04-16', '11987654372', 'marcelo.santos@email.com', 2),
('Marina Almeida', '1993-11-27', '11987654373', 'marina.almeida@email.com', 3),
('Wagner Dias', '1989-11-02', '11987654374', 'wagner.dias@email.com', 1),
('Regiane Silva', '1994-10-20', '11987654375', 'regiane.silva@email.com', 2),
('Luciana Pires', '1990-09-09', '11987654376', 'luciana.pires@email.com', 3),
('Renato Oliveira', '1993-07-15', '11987654377', 'renato.oliveira@email.com', 1),
('Simone Costa', '1991-06-05', '11987654378', 'simone.costa@email.com', 2),
('José Santos', '1992-12-01', '11987654379', 'jose.santos@email.com', 3),
('Eliane Pereira', '1990-03-30', '11987654380', 'eliane.pereira@email.com', 1),
('Marcio Rocha', '1994-08-17', '11987654381', 'marcio.rocha@email.com', 2),
('Patricia Ribeiro', '1992-05-13', '11987654382', 'patricia.ribeiro@email.com', 3),
('Gerson Lima', '1991-01-19', '11987654383', 'gerson.lima@email.com', 1),
('Marcela Souza', '1993-03-23', '11987654384', 'marcela.souza@email.com', 2),
('Cristiano Costa', '1992-10-04', '11987654385', 'cristiano.costa@email.com', 3),
('Neuza Oliveira', '1991-07-08', '11987654386', 'neuza.oliveira@email.com', 1),
('Márcia Santos', '1990-04-06', '11987654387', 'marcia.santos@email.com', 2),
('Jussara Pires', '1994-11-10', '11987654388', 'jussara.pires@email.com', 3),
('Renata Ribeiro', '1991-12-23', '11987654389', 'renata.ribeiro@email.com', 1),
('Eduardo Lima', '1993-05-25', '11987654390', 'eduardo.lima@email.com', 2),
('Sérgio Costa', '1992-08-11', '11987654391', 'sergio.costa@email.com', 3),
('Tânia Santos', '1990-10-28', '11987654392', 'tania.santos@email.com', 1),
('Carlos Ribeiro', '1994-01-23', '11987654393', 'carlos.ribeiro@email.com', 2),
('Elisabete Rocha', '1991-02-17', '11987654394', 'elisabete.rocha@email.com', 3),
('Joana Lima', '1993-11-09', '11987654395', 'joana.lima@email.com', 1),
('Gisele Costa', '1992-05-12', '11987654396', 'gisele.costa@email.com', 2),
('Sérgio Pereira', '1990-01-15', '11987654397', 'sergio.pereira@email.com', 3),
('Danilo Rocha', '1994-08-25', '11987654398', 'danilo.rocha@email.com', 1),
('Sandra Oliveira', '1993-06-03', '11987654399', 'sandra.oliveira@email.com', 2),
('Fernando Ribeiro', '1992-09-12', '11987654400', 'fernando.ribeiro@email.com', 3),
('Marcos Silva', '1995-04-14', '11987654401', 'marcos.silva@email.com', 1),
('Joana Santos', '1991-03-23', '11987654402', 'joana.santos@email.com', 2),
('Eduardo Costa', '1990-12-05', '11987654403', 'eduardo.costa@email.com', 3),
('Fernanda Almeida', '1994-07-22', '11987654404', 'fernanda.almeida@email.com', 1),
('Ricardo Martins', '1993-08-11', '11987654405', 'ricardo.martins@email.com', 2),
('Beatriz Souza', '1992-11-17', '11987654406', 'beatriz.souza@email.com', 3),
('Gustavo Rocha', '1991-02-03', '11987654407', 'gustavo.rocha@email.com', 1),
('Patrícia Pereira', '1995-09-08', '11987654408', 'patricia.pereira@email.com', 2),
('Lucas Ribeiro', '1990-05-21', '11987654409', 'lucas.ribeiro@email.com', 3),
('Simone Oliveira', '1994-03-14', '11987654410', 'simone.oliveira@email.com', 1),
('Mariana Silva', '1993-06-06', '11987654411', 'mariana.silva@email.com', 2),
('Fábio Costa', '1991-09-02', '11987654412', 'fabio.costa@email.com', 3),
('Raul Santos', '1995-01-29', '11987654413', 'raul.santos@email.com', 1),
('Jéssica Almeida', '1994-12-03', '11987654414', 'jessica.almeida@email.com', 2),
('Aline Rocha', '1992-04-18', '11987654415', 'aline.rocha@email.com', 3),
('Juliana Costa', '1991-11-30', '11987654416', 'juliana.costa@email.com', 1),
('Rodrigo Souza', '1993-10-17', '11987654417', 'rodrigo.souza@email.com', 2),
('Vera Almeida', '1990-08-24', '11987654418', 'vera.almeida@email.com', 3),
('Eduarda Silva', '1994-02-13', '11987654419', 'eduarda.silva@email.com', 1),
('Thiago Pereira', '1991-05-09', '11987654420', 'thiago.pereira@email.com', 2);


-- Inserindo professores
INSERT INTO professores (nome, especialidade, telefone, email) VALUES
('Professor João', 'Musculação', '11987654321', 'joao.professor@email.com'),
('Professor Maria', 'Crossfit', '11987654322', 'maria.professor@email.com'),
('Professor Carlos', 'Pilates', '11987654323', 'carlos.professor@email.com');

-- Inserindo treinos
INSERT INTO treinos (descricao, professor_id) VALUES
('Treino de Musculação', 1),
('Treino de Crossfit', 2),
('Treino de Pilates', 3);

-- Associando alunos aos treinos
INSERT INTO alunos_treinos (aluno_id, treino_id) VALUES
(1, 1),  -- João Silva faz Musculação
(2, 2),  -- Maria Oliveira faz Crossfit
(3, 3),  -- Carlos Souza faz Pilates
(4, 1),  -- Ana Costa faz Musculação
(5, 2);  -- Lucas Pereira faz Crossfit

-- Inserindo pagamentos
INSERT INTO pagamentos (aluno_id, valor) VALUES
(1, 100.00),
(2, 250.00),
(3, 900.00),
(4, 100.00),
(5, 250.00);
