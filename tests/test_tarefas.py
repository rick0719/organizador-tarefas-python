"""Testes das operações principais do organizador de tarefas."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from tarefas import adicionar, concluir, conectar, listar


class TesteTarefas(unittest.TestCase):
    def setUp(self):
        self.conexao = conectar(":memory:")

    def tearDown(self):
        self.conexao.close()

    def test_adicionar_e_listar(self):
        identificador = adicionar(self.conexao, "  Estudar Python  ")
        self.assertEqual(listar(self.conexao), [(identificador, "Estudar Python", 0)])

    def test_concluir(self):
        identificador = adicionar(self.conexao, "Estudar")
        self.assertTrue(concluir(self.conexao, identificador))
        self.assertEqual(listar(self.conexao)[0][2], 1)

    def test_concluir_inexistente(self):
        self.assertFalse(concluir(self.conexao, 999))

    def test_titulo_vazio(self):
        with self.assertRaises(ValueError):
            adicionar(self.conexao, "   ")
        self.assertEqual(listar(self.conexao), [])


if __name__ == "__main__":
    unittest.main()
