create database suporte_ti;
use suporte_ti;

-- tabela de departamentos
create table departamentos (
    id int auto_increment primary key,
    nome varchar(100) not null
);

-- tabela de técnicos
create table tecnicos (
    id int auto_increment primary key,
    nome varchar(150) not null,
    nivel varchar(50) not null
);

-- tabela de usuários
create table usuarios (
    id int auto_increment primary key,
    nome varchar(150) not null,
    departamento_id int not null,
    constraint fk_usuarios_departamento
        foreign key (departamento_id)
        references departamentos(id)
);

-- tabela de solicitações
create table solicitacoes (
    id int auto_increment primary key,
    nome_solicitante varchar(150) not null,
    departamento_id int not null,
    descricao text not null,
    status varchar(50) default 'aberta',
    tecnico_id int,
    prioridade varchar(100),
    num_atendimento int,
    data_criacao datetime default current_timestamp,
    constraint fk_solicitacoes_departamento
        foreign key (departamento_id)
        references departamentos(id),
    constraint fk_solicitacoes_tecnico
        foreign key (tecnico_id)
        references tecnicos(id)
);


-- tabela de histórico
create table historico (
    id int auto_increment primary key,
    solicitacao_id int not null,
    tecnico_id int not null,
    descricao_final text,
    data_finalizacao datetime default current_timestamp,
    constraint fk_historico_solicitacaohistorico
        foreign key (solicitacao_id)
        references solicitacoes(id),
    constraint fk_historico_tecnico
        foreign key (tecnico_id)
        references tecnicos(id)
);

insert into tecnicos (nome, nivel) values
('Carlos Silva', 'junior'),
('Mariana Souza', 'pleno'),
('Rafael Lima', 'senior'),
('Juliana Alves', 'estagiario'),
('Bruno Costa', 'junior'),
('Fernanda Rocha', 'pleno'),
('Gabriel Martins', 'senior'),
('Patricia Gomes', 'junior'),
('Lucas Ferreira', 'pleno'),
('Aline Barbosa', 'estagiario');

insert into departamentos (nome) values
('Recursos Humanos'),
('Financeiro'),
('Comercial'),
('Marketing'),
('Jurídico'),
('Logística'),
('Compras'),
('Operações'),
('Administrativo'),
('Contabilidade');