# Organizador de tarefas em Python

Projeto de estudo: uma aplicação simples de linha de comando que cadastra, lista e conclui tarefas, salvando os dados localmente em SQLite. Criado com apoio da Zapia para estudo e evolução do portfólio.

## O que o projeto pratica

- Python: funções, argumentos de linha de comando e tratamento de erros.
- Banco de dados: criação, inserção, consulta e atualização em SQLite.
- Testes automatizados com `unittest`.

## Requisitos

Python 3.9 ou mais recente. Não é necessário instalar bibliotecas externas.

# Organizador de tarefas em Python

Aplicação de linha de comando para cadastrar, consultar e concluir tarefas, mantendo os dados em um banco SQLite local. Projeto de estudo para praticar Python, SQL básico e testes automatizados.

## Problema e objetivo

Uma lista de tarefas simples precisa continuar disponível entre execuções sem exigir um servidor ou serviço externo. O programa armazena tarefas em SQLite e permite manipulá-las pelo terminal.

## Funcionalidades

- Adiciona tarefas com título não vazio.
- Lista tarefas em ordem de cadastro, indicando se foram concluídas.
- Marca como concluída uma tarefa pelo identificador.
- Permite escolher o caminho do banco com `--banco` (padrão: `tarefas.db`).
- Usa apenas a biblioteca padrão do Python, incluindo `sqlite3`, `argparse` e `unittest`.

## Tecnologias

- Python 3.9 ou superior
- SQLite (via módulo `sqlite3`)
- `unittest` para testes

## Requisitos e instalação

Não há dependências externas. Instale Python 3.9+ e clone o repositório:

```bash
git clone https://github.com/rick0719/organizador-tarefas-python.git
cd organizador-tarefas-python
```

## Exemplos de uso

Os comandos abaixo executam a partir da raiz do projeto. O arquivo `tarefas.db` será criado localmente caso ainda não exista.

```bash
python src/tarefas.py adicionar "Estudar Python"
python src/tarefas.py listar
python src/tarefas.py concluir 1
python src/tarefas.py --banco /tmp/minhas-tarefas.db adicionar "Revisar testes"
```

A saída da listagem apresenta `[ ]` para pendente e `[x]` para concluída. Um título vazio é rejeitado; um identificador inexistente retorna erro.

## Testes

Execute a suíte incluída, sem dependências adicionais:

```bash
python -m unittest discover -s tests -v
```

Os testes usam banco SQLite em memória e cobrem inclusão/listagem, conclusão, ID inexistente e título vazio; não alteram o banco local do usuário.

## Estrutura

```text
.
├── src/
│   └── tarefas.py       # operações SQLite e interface de linha de comando
├── tests/
│   └── test_tarefas.py  # testes automatizados com unittest
├── .gitignore
└── README.md
```

## Decisões técnicas

- SQLite local evita configurar servidor e mantém os dados entre execuções.
- Consultas usam parâmetros SQL (`?`) para valores fornecidos pelo usuário.
- As operações de banco ficam em funções separadas da interface de argumentos, o que facilita testá-las.
- Os testes usam `:memory:` para isolamento e rapidez.

## Limitações e próximos passos

Esta é uma aplicação didática de terminal, não um sistema multiusuário. Não há edição nem exclusão de tarefas, categorias, datas-limite, busca ou interface gráfica; a listagem é simples e não possui filtro. Possíveis evoluções incluem edição/exclusão, filtros e validação de IDs diretamente na interface.

## Créditos e uso de IA

Projeto de estudo desenvolvido com apoio da Zapia. A assistência de IA foi usada para apoiar a organização e documentação do projeto; o código e as instruções devem ser conferidos e compreendidos pelo estudante. Este repositório não representa experiência profissional nem métricas de uso.## Como usar

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
