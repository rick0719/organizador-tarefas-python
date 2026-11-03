"""Organizador de tarefas local usando apenas a biblioteca padrão do Python."""
import argparse
import sqlite3
from pathlib import Path


def conectar(caminho):
    conexao = sqlite3.connect(caminho)
    conexao.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, titulo TEXT NOT NULL, concluida INTEGER NOT NULL DEFAULT 0)")
    return conexao


def adicionar(conexao, titulo):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("O título da tarefa não pode estar vazio.")
    with conexao:
        cursor = conexao.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
    return cursor.lastrowid


def listar(conexao):
    return conexao.execute("SELECT id, titulo, concluida FROM tarefas ORDER BY id").fetchall()


def concluir(conexao, identificador):
    with conexao:
        cursor = conexao.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (identificador,))
    return cursor.rowcount > 0


def main():
    parser = argparse.ArgumentParser(description="Organize suas tarefas no terminal.")
    parser.add_argument("--banco", type=Path, default=Path("tarefas.db"), help="Caminho do banco local (padrão: tarefas.db)")
    comandos = parser.add_subparsers(dest="comando", required=True)
    novo = comandos.add_parser("adicionar", help="Adiciona uma tarefa")
    novo.add_argument("titulo")
    comandos.add_parser("listar", help="Lista as tarefas")
    feito = comandos.add_parser("concluir", help="Marca uma tarefa como concluída")
    feito.add_argument("id", type=int)
    args = parser.parse_args()
    with conectar(args.banco) as conexao:
        if args.comando == "adicionar":
            try:
                identificador = adicionar(conexao, args.titulo)
            except ValueError as erro:
                parser.error(str(erro))
            print(f"Tarefa {identificador} adicionada.")
        elif args.comando == "listar":
            tarefas = listar(conexao)
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            for identificador, titulo, concluida in tarefas:
                print(f"{identificador}. [{'x' if concluida else ' '}] {titulo}")
        elif concluir(conexao, args.id):
            print(f"Tarefa {args.id} concluída.")
        else:
            parser.exit(1, f"Tarefa {args.id} não encontrada.\n")


if __name__ == "__main__":
    main()
