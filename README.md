# Controle Financeiro

Sistema de controle financeiro desenvolvido em Python e MySQL para registrar e gerenciar lançamentos financeiros.

## Tecnologias utilizadas

- Python
- MySQL
- mysql-connector-python
- python-dotenv

## Funcionalidades

- Adicionar lançamentos financeiros
- Listar lançamentos cadastrados
- Consultar o saldo financeiro
- Editar lançamentos
- Excluir lançamentos
- Validação de dados informados pelo usuário
- Armazenamento dos dados em banco de dados MySQL

## Banco de dados

O projeto utiliza o MySQL para armazenar os lançamentos financeiros.

A tabela `lancamentos` possui os seguintes campos:

- `ID` — identificador do lançamento
- `descricao` — descrição do lançamento
- `valor` — valor financeiro
- `tipo` — receita ou despesa
- `categoria` — categoria do lançamento
- `data` — data e hora do lançamento