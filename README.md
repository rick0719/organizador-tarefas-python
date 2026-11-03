# Organizador de tarefas em Python

Projeto de estudo que cadastra, lista e conclui tarefas pelo terminal e armazena dados localmente em SQLite.

## Tecnologias e requisitos

Python 3.9 ou superior. Usa SQLite, argparse e unittest da biblioteca padrão.

## Como usar

Na pasta do projeto, execute:

```bash
python src/tarefas.py adicionar "Estudar Python"
python src/tarefas.py listar
python src/tarefas.py concluir 1
```

O banco `tarefas.db` é criado na pasta atual. Para usar outro arquivo:

```bash
python src/tarefas.py --banco estudos.db listar
```

## Testes

```bash
python -m unittest discover -s tests -v
```

Os testes usam um banco em memória para verificar inclusão, listagem, conclusão, ID inexistente e título vazio.

## Organização

- `src/tarefas.py`: aplicação de terminal e operações no banco.
- `tests/test_tarefas.py`: testes das funções.
- `.gitignore`: arquivos locais ignorados pelo Git.

## Decisões e limitações

O SQLite dispensa servidor externo; as consultas são parametrizadas. Não há interface gráfica, edição, exclusão, filtros ou múltiplos usuários. Evite armazenar dados sensíveis no banco.

## Próximos passos

Adicionar edição, exclusão, filtros e testes da interface de linha de comando.

## Contato

Ricardo da Silva Pereira  
Celular: +55 (11) 95934-1288  
[WhatsApp](https://wa.me/5511959341288)
