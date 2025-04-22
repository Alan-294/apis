import unittest
from flask import request  # Import do Flask (caso esteja usando)
import requests  # Biblioteca para requisições HTTP

class TestProduct(unittest.TestCase):
    def test001(self):
        self.assertTrue(True)

                    ########################
                    #### Teste Turmas #####
                    ########################

    # Teste 001: Verificar se a rota /turma está funcionando
    def teste001(self):
        r = requests.get('http://127.0.0.1:5000/api/turma')
        if r.status_code == 200:
            self.assertTrue(True)
        else:
            self.fail("Erro na url")
        return r.json()
        
    # teste 002: verificar se estar retornando um valor json.

    def teste002(self):
        r = requests.get('http://127.0.0.1:5000/api/turma')
        if r.headers['Content-Type'] == 'application/json':
            self.assertTrue(True)
        else:
            self.fail("Erro no tipo de retorno")
        

    # teste 003: GeT com id - Validar se estar retornando turma com uma id valida

    def teste003(self):
        r = requests.get('http://127.0.0.1:5000/api/turma?id=1') 
        dados = r.json()
        self.assertEqual(dados["turma"]["id"], 1, "Erro ID não encontrado")

        
    # teste 004: GET com id - Validar se estar retornando turma com um id especifico que não existe
    def teste004(self):    
        r = requests.get('http://127.0.0.1:5000/api/turma?id=-1')
        dados = r.json()
        if self.assertEqual(dados['code'], 404): 
            self.assertTrue(True)

    # teste 005: POST - Validar se está adicionando uma turma
    def teste005(self):
        # Dados a serem enviados no corpo da requisição
        payload = {
            "nome": "ads2",
            "turno": "noite",
            "professor_id": 2
        }
        # Envia a requisição POST com os dados no corpo
        r = requests.post('http://127.0.0.1:5000/api/turma', json=payload)
        
        # Verifica o status da resposta
        self.assertEqual(r.status_code, 200, "Erro: Status code inesperado")
        
        # Verifica o conteúdo da resposta
        dados = r.json()
        self.assertIn("turma_adicionada", dados, "Erro: Resposta não contém 'turma_adicionada'")
        id = dados['turma_adicionada']['id']
        
        # Verifica se a turma foi adicionada corretamente
        r2 = requests.get(f'http://127.0.0.1:5000/api/turma?id={id}')
        dados2 = r2.json()
        self.assertEqual(dados2['turma']['id'], id, "Erro ao adicionar turma")
        return dados2
    
    # teste 006: PUT - Validar se está editando uma turma
    def teste006(self):
        # Adiciona uma nova turma
        dados2 = self.teste005()
        
        # Atualiza a turma adicionada
        payload = {
            "nome": "Nome(alterado)",
            "turno": "Noite",
            "professor_id": 1,
            "ativo": True
        }
        requests.put(f"http://127.0.0.1:5000/api/turma?id={dados2['turma']['id']}", json=payload)

        # Obtém todas as turmas
        dados3 = self.teste001()
        
        # Itera sobre a lista de turmas para verificar a atualização
        for listaTurmas in dados3:  # `dados3` é uma lista, não um dicionário
            if listaTurmas['id'] == dados2['turma']['id']:
                self.assertEqual(listaTurmas['nome'], 'Nome(alterado)', "Erro ao editar turma")


    def teste007(self):
        # Setup - cria uma turma de teste
        test_turma = self.teste005()
        turma_id = test_turma['turma']['id']
        
        # Verifica se a turma existe antes da exclusão
        initial_turmas = self.teste001()
        self.assertIn(turma_id, [t['id'] for t in initial_turmas], 
                    "Turma deveria existir antes da exclusão")
        
        # Deleta a turma
        delete_url = f"http://127.0.0.1:5000/api/turma?id={turma_id}"
        response = requests.delete(delete_url)
        
        # Verifica se a exclusão foi bem-sucedida
        self.assertEqual(response.status_code, 200, 
                        "DELETE request deveria retornar status 200")
        
        # Verifica se a turma não existe mais
        updated_turmas = self.teste001()
        self.assertNotIn(turma_id, [t['id'] for t in updated_turmas], 
                        "Turma deveria ser removida após exclusão")
        


if __name__ == '__main__':
    unittest.main()
    
