# SCPTI — Sistema de Controle de Pedidos de TI

Sistema de gerenciamento de chamados de suporte técnico desenvolvido em Python com banco de dados MySQL, simulando o funcionamento de um sistema corporativo real.

---

## 🛠️ Tecnologias

- Python 3
- MySQL
- mysql-connector-python

---

## 📋 Funcionalidades

- Cadastro de usuários por departamento
- Abertura de solicitações de suporte
- Encaminhamento de chamados para técnicos com base em impacto e dificuldade
- Conclusão de atendimentos com registro de solução aplicada
- Histórico completo de solicitações finalizadas
- Estatísticas com visualização de chamados por status

---

## 🗄️ Estrutura do Banco de Dados

| Tabela | Descrição |
|---|---|
| `departamentos` | Departamentos disponíveis no sistema |
| `usuarios` | Usuários que podem abrir chamados |
| `tecnicos` | Técnicos responsáveis pelos atendimentos |
| `solicitacoes` | Chamados abertos, em andamento e finalizados |
| `historico` | Registro de chamados concluídos com solução aplicada |

---

## 🔄 Fluxo do Sistema

1. **Cadastrar usuário** — vincula o usuário a um departamento
2. **Registrar solicitação** — usuário seleciona seu departamento, se identifica e descreve o problema
3. **Encaminhar solicitação** — define impacto e dificuldade, calcula prioridade e atribui um técnico compatível
4. **Concluir solicitação** — técnico descreve a solução e finaliza o chamado
5. **Ver histórico** — exibe todos os chamados finalizados
6. **Ver estatísticas** — exibe chamados por categoria (abertos, em andamento, concluídos)

---

## ⚡ Prioridade de Atendimento

A prioridade é definida com base em uma matriz de impacto × dificuldade, onde o impacto tem peso maior:

| Impacto \ Dificuldade | Fácil | Média | Difícil |
|---|---|---|---|
| Baixo | Baixa | Baixa | Média |
| Médio | Média | Média | Alta |
| Alto | Alta | Alta | Alta |

- **Prioridade Baixa** → técnicos júnior e estagiário
- **Prioridade Média** → técnicos pleno e júnior
- **Prioridade Alta** → técnicos sênior e pleno

---

## 🚀 Como Executar

1. Configure a conexão com o banco em `chamar_banco.py`
2. Execute o script SQL para criar o banco e popular as tabelas
3. Rode o sistema:

```bash
python funções_Rodagem.py
```

---

## 📁 Estrutura dos Arquivos

```
├── chamar_banco.py       # configuração da conexão com o MySQL
├── funções_ação.py       # funções principais do sistema
├── funções_Rodagem.py    # menu e inicialização do sistema
└── banco.sql             # script de criação do banco de dados
```
os-de-TI

---

## 👨‍💻 Autores

- Otávio Felix Da Silva
- Igor Mastrangelo Domingos
- Jonathan Ribeiro
- Maximus Daniel Nascimento
