import unittest
from flask import request  # Import do Flask (caso esteja usando)
import requests  # Biblioteca para requisições HTTP
from professores import *

class TestProduct(unittest.TestCase):
    def test001(self):
        self.assertTrue(True)

# 10 testes 
    

    # Teste 001: Verificar se a rota /profesores está funcionando!
    def teste001(self):
        r = requests.get('http://127.0.0.1:5000/api/professores')
        if r.status_code == 200:
            print("Teste 1 passou")
            self.assertTrue(True)
        else:
            self.fail("Erro na url")
        return r.json()
        
    # teste 002: verificar se estar retornando um valor json.

    def teste002(self):
        r = requests.get('http://127.0.0.1:5000/api/professores')
        if r.headers['Content-Type'] == 'application/json':
            print("Teste 2 passou")
            self.assertTrue(True)
        else:
            self.fail("Erro no tipo de retorno")
        

    # teste 003: GeT com id - Validar se estar retornando professores com uma id valida

    def teste003(self):
        r = requests.get('http://127.0.0.1:5000/api/professores/1') 
        
        try:
            dados = r.json()
            if "id" in dados:
                self.assertEqual(dados["id"], 1, "Erro ID não encontrado")
            else:
               
                self.fail("Resposta não contém id")
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")

        
    # teste 004: GET com id - Validar se estar retornando professores com um id especifico que não existe
    def teste004(self):    
        r = requests.get('http://127.0.0.1:5000/api/professores/4')
        
        
        try:
            dados = r.json()
   
            self.assertTrue('mensagem' in dados, "Resposta não contém mensagem de erro esperada")
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")

    # teste 005: POST - Validar se está adicionando professores
    def teste005(self):
        r = requests.post('http://127.0.0.1:5000/professores/', json={
                                                                                "nome": "Joao",
                                                                                "data_nascimento": "2005-10-03",
                                                                                "disciplina": "Chemistry",
                                                                                "salario": 2500,
                                                                                "Observações": "None"
                                                                            })
        if r.status_code != 200:
            self.fail(f"Erro ao adicionar professor. Status: {r.status_code}, Resposta: {r.text}")

        try:
            dados = r.json()  
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")
            
        id = dados.get("id")
    
        if not id:
            self.fail("Erro: ID do aluno não retornado corretamente")

        r2 = requests.get(f'http://127.0.0.1:5000/api/professores/{id}')
        dados2 = r2.json()
        self.assertEqual(dados2['id'], id, "Erro ao adicionar professor")
        return dados2
    
    # teste 006: PUT - Validar se está editando uma professores
    def teste006(self):
        dados2 = self.teste005()
        #print(dados2)
        
        r = requests.put(f'http://127.0.0.1:5000/professores/{professorPorId}',
                                json={"nome": "Lucio",
            "data_nascimento": "1995-10-03",
            "disciplina": "Cience",
            "salario": 1500,
            "Observações": "None"})

        dados3 = self.teste001()
        print("dados3:", dados3) 
        
        if dados3 is None:
            self.fail("Erro: teste001() não retornou dados válidos")
            if isinstance(dados3, list): 

                for listaprofessor in dados3:
                    if listaprofessor['id'] == dados2['id']: 
                     self.assertEqual(listaprofessor['nome'], 'Lucio', "Erro ao editar do professor")
                    break
                else:
                    self.fail("Erro: Professor não encontrado na lista após edição")
        else:
            self.fail("Erro: dados3 não contém uma lista de professores")


    # teste 007: DELETE - Validar se está excluindo uma professores
    def teste007(self):
    
                            
        novo_professor = self.teste005()
        professorPorId = novo_professor["id"]

        requests.delete(f"http://127.0.0.1:5000/api/professores/{professorPorId}")

        r2 = requests.get(f"http://127.0.0.1:5000/api/professores/{professorPorId}")
        self.assertEqual(r2.status_code, 404, "Erro: Professor ainda existe após deleção")


if __name__ == '__main__':
    unittest.main()
