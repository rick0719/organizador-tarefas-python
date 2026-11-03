# Organizador de tarefas em Python

Projeto de estudo: uma aplicação simples de linha de comando que cadastra, lista e conclui tarefas, salvando os dados localmente em SQLite. Criado com apoio da Zapia para estudo e evolução do portfólio.

## O que o projeto pratica

- Python: funções, argumentos de linha de comando e tratamento de erros.
- Banco de dados: criação, inserção, consulta e atualização em SQLite.
- Testes automatizados com `unittest`.

## Requisitos

Python 3.9 ou mais recente. Não é necessário instalar bibliotecas externas.

## Como usar

Na pasta do projeto, execute:

```bash
python src/tarefas.py adicionar "Estudar Python"
python src/tarefas.py listar
python src/tarefas.py concluir 1
```

O arquivo `tarefas.db` é criado na pasta atual. Não compartilhe nele informações confidenciais. Para usar outro arquivo, informe `--banco` antes do comando:

```bash
python src/tarefas.py --banco estudos.db listar
```

## Executar os testes

```bash
python -m unittest discover -s tests -v
```

## Estrutura

```text
organizador-tarefas/
├── src/tarefas.py       # Aplicação e operações no banco
├── tests/test_tarefas.py # Testes automatizados
├── .gitignore           # Arquivos locais que não devem ir ao repositório
└── README.md            # Documentação
```

## Próximos passos

Como exercícios, experimente implementar exclusão de tarefas, filtro por status e testes da interface de linha de comando. Projeto educacional; ainda não possui interface gráfica ou sistema de usuários.
