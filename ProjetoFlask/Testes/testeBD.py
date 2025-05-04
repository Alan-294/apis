import unittest
import sqlite3
import os

class TestBancoSQLite(unittest.TestCase):
    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.db_path = "banco_de_dados.db"
        self.conexao = sqlite3.connect(self.db_path)

    def tearDown(self):
        """Finalização após cada teste."""
        self.conexao.close()

    def test_conexao_banco(self):
        """Teste para verificar se a conexão com o banco de dados é bem-sucedida."""
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT 1")
            resultado = cursor.fetchone()
            self.assertEqual(resultado[0], 1, "Erro ao conectar ao banco de dados")
        except sqlite3.Error as e:
            self.fail(f"Erro ao conectar ao banco de dados: {str(e)}")

    def test_tabelas_existem(self):
        """Teste para verificar se as tabelas necessárias existem no banco de dados."""
        tabelas_esperadas = ["professores", "turmas", "alunos"]
        cursor = self.conexao.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tabelas = [row[0] for row in cursor.fetchall()]
        for tabela in tabelas_esperadas:
            self.assertIn(tabela, tabelas, f"Tabela '{tabela}' não encontrada no banco de dados")

if __name__ == "__main__":
    unittest.main()