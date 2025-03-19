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
        r = requests.get('http://127.0.0.1:5000/professore/4')
        dados = r.json()
        if self.assertEqual(dados['code'], 404): 
            self.assertTrue(True)

    # teste 005: POST - Validar se está adicionando um professor
    def teste005(self):
        r = requests.post('http://127.0.0.1:5000/professores/', json={
            "nome": "Joao",
            "data_nascimento": "2005-10-03",
            "disciplina": "Chemistry",
            "salario": 2500,
            "Observações": "None"
        })
        dados = r.json()     
        id = dados['professores_adicionada']["id"]["id"]
        #print(id)
        r2 = requests.get(f'http://127.0.0.1:5000/professores?id={id}')
        dados2 = r2.json()
        self.assertEqual(dados2["professores"]["id"], id, "Erro ao adicionar professor")
        return dados2
    
    # teste 006: PUT - Validar se está editando uma professores
    def teste006(self):
        dados2 = self.teste005()
        #print(dados2)
        
        r = requests.put(f'http://127.0.0.1:5000/professores?id={dados2["professores"]["id"]}&nome=Nome(alterado)&disciplina=Portuguese&id=3')

        dados3 = self.teste001()
        #print(dados3) 
        
        for listaprofessoress in dados3["professoress"]:

            if listaprofessoress["id"] == dados2["professores"]["id"]:
                #print(listaprofessoress)
                self.assertEqual(listaprofessoress['nome'], 'Nome(alterado)', "Erro ao editar professor")


    # teste 007: DELETE - Validar se está excluindo uma professores
    def teste007(self):
        novaprofessores = self.teste005()
        listaprofessoress = self.teste001()
        
        for professores in listaprofessoress["professoress"]:
            if professores["id"] == novaprofessores["professores"]["id"]:
                dodos = requests.delete(f"http://127.0.0.1:5000/professores?id={professores['id']}")
                break

        listaprofessoress = self.teste001()

        if novaprofessores["professores"]["id"] not in [t["id"] for t in listaprofessoress["professoress"]]: 
            self.assertTrue(True)
        else:
            self.fail("Erro ao excluir professor")


if __name__ == '__main__':
    unittest.main()
