import unittest
import requests  

class TestProfessoresAPI(unittest.TestCase):

    BASE_URL = "http://127.0.0.1:5000/api/professores"
    def test_001_verificar_rota_professores(self):
        """Verifica se a rota /professores está funcionando."""
        r = requests.get(self.BASE_URL)
        self.assertEqual(r.status_code, 200, "Erro na URL")

    def test_002_verificar_retorno_json(self):
        """Verifica se a resposta da API está no formato JSON."""
        r = requests.get(self.BASE_URL)
        self.assertEqual(r.headers.get('Content-Type'), 'application/json', "Erro no tipo de retorno")

    def test_003_get_professor_por_id_valido(self):
        """Verifica se um professor com ID válido é retornado corretamente."""
        
        r = requests.get(f"{self.BASE_URL}/1")
        try:
            dados = r.json()
            if 'id' in dados:
                self.assertEqual(dados['id'], 1, "Erro ID não encontrado")
            else:
                self.fail("Resposta não contém 'id'")
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")

    def test_004_get_professor_por_id_invalido(self):
        """Verifica se a API retorna erro ao buscar um ID inexistente."""
        r = requests.get(f"{self.BASE_URL}/99999")  # Um ID que provavelmente não existe
        self.assertEqual(r.status_code, 404, "Erro: deveria retornar 404 para ID inexistente")

        dados = r.json()
        self.assertIn("mensagem", dados, "Resposta não contém mensagem de erro esperada")

    def test_005_post_adicionar_professor(self):
        """Verifica se a API adiciona um novo professor corretamente."""
        novo_professor = {
            "nome": "Carlos",
            "data_nascimento": "1990-05-12",
            "disciplina": "Física",
            "salario": 3000,
            "observacoes": "Nenhuma"
        }

        r = requests.post(self.BASE_URL, json=novo_professor)
        self.assertEqual(r.status_code, 200, f"Erro ao adicionar professor. Resposta: {r.text}")

        dados = r.json()
        self.assertIn("id", dados, "Erro: ID do professor não retornado corretamente")
        return dados["id"]  # Retorna o ID para os próximos testes

    def test_006_put_editar_professor(self):
        """Verifica se a API edita um professor corretamente."""
        professor_id = self.test_005_post_adicionar_professor()

        novos_dados = {
            "nome": "Carlos Editado",
            "data_nascimento": "1990-05-12",
            "disciplina": "Fisica Avançada",
            "salario": 3200,
            "observacoes": "Atualizado"
        }

        r = requests.put(f"{self.BASE_URL}/{professor_id}", json=novos_dados)
        self.assertEqual(r.status_code, 200, f"Erro ao editar professor. Resposta: {r.text}")

        r2 = requests.get(f"{self.BASE_URL}/{professor_id}")
        self.assertEqual(r2.status_code, 200, "Erro ao buscar professor após edição")

        dados_atualizados = r2.json()
        self.assertEqual(dados_atualizados["nome"], "Carlos Editado", "Erro ao atualizar nome do professor")

    def test_007_delete_professor(self):
        """Verifica se a API exclui um professor corretamente."""
        professor_id = self.test_005_post_adicionar_professor()

        r = requests.delete(f"{self.BASE_URL}/{professor_id}")
        self.assertEqual(r.status_code, 200, "Erro ao deletar professor")

        r2 = requests.get(f"{self.BASE_URL}/{professor_id}")
        self.assertEqual(r2.status_code, 404, "Erro: professor ainda existe após deleção")

if __name__ == '__main__':
    unittest.main()
