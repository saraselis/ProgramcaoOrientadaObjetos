#!/usr/bin/env python
# coding: utf-8

# 

# # Atividade 06 - POO
# Projete e implemente o sistema que faz controle de estoque de uma dessas plataformas de venda online, guardando a disposição dos itens nos locais de armazenamento, tipos de pagamento e preço de frete para a entrega.

# * Banco onde vamos gerir o estoque dos produtos

# In[1]:


from pymongo import MongoClient


# In[2]:


cliente = MongoClient('mongodb://localhost:27017/')

db = cliente.sistema

produtos = db.produtos


# In[3]:


produtos


# * Biblioteca que vamos utilizar pra abrir o modelo pra realizar a predicao das futuras vendas

# In[4]:


import joblib


# * Logs para acompanhar o sistema

# In[5]:


import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# * Excções personalizadas do sistema

# In[6]:


class ModeloZoado(Exception):
    '''
        Excecao estourada quando não se consegue importar o
            modelo para prever as vendas.
    '''
    def __init__(self):
        super().__init__("Seu modelo por algum motivo não pode ser importado!")


# In[7]:


class Generica(Exception):
    '''
        Excecao estourada em casos genericos nao previstos pelo sistema.
    '''
    def __init__(self):
        super().__init__("Ocorreu um erro, estamos verificando!")


# * Classe generica para instanciar os produtos

# In[8]:


class Produto:
    '''
        Instância um produto a ser trabalhado no sistema de estoque.
    '''
    def __init__(self, _id: int, nome: str, lugar: str, tipo_pagamento: str, preco_frete: float,
                 preco_produto: float, quantidade: int):
        self._id = _id
        self._nome = nome
        self._lugar = lugar
        self._tipo_pagamento = tipo_pagamento
        self._preco_frete = preco_frete
        self._preco_produto = preco_produto
        self._quantidade = quantidade

    @property
    def nome(self) -> str:
        ''' Retorna o nome do produto. '''
        return self._nome
    
    @nome.setter
    def nome(self, new_name: str):
        '''
            Altera o nome do produto
            :new_name: novo nome
        '''
        self._nome = new_name
        
    @property
    def lugar(self) -> str: 
        ''' Retorna o lugar onde o produto será colocado. '''
        return self._lugar
    
    @lugar.setter
    def lugar(self, new_lugar: str):
        '''
            Altera o lugar do produto
            :new_lugar: novo lugar
        '''
        self._lugar = new_lugar
        
    @property
    def tipo_pagamento(self) -> str:
        ''' Retorna o tipo de pagamento aceito por aquele produto. '''
        return self._tipo_pagamento
    
    @tipo_pagamento.setter
    def tipo_pagamento(self, new_pag: str):
        '''
            Altera o tipo de pagamento do produto.
            :new_pag: novo pagamento
        '''
        self._tipo_pagamento = new_pag
        
    @property
    def preco_frete(self) -> float:
        ''' Retorna o preco do frete daquele produto. '''
        return self._preco_frete
    
    @preco_frete.setter
    def preco_frete(self, new_frete: float):
        '''
            Altera o preco de frete do produto.
            :new_frete: novo frete
        '''
        self._preco_frete = new_frete
        
    @property
    def preco_produto(self) -> float:
        ''' Retorna o preco do produto. '''
        return self._preco_produto
    
    @preco_produto.setter
    def preco_produto(self, new_preco: float):
        '''
            Altera o preco do produto.
            :new_preco: novo preco
        '''
        self._preco_produto = new_preco
        
    @property
    def quantidade(self) -> int:       
        ''' Retorna a quantidade daquele produto. '''
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, new_qtd: int):
        '''
            Altera a quantidade do produto.
            :new_qtd: nova quantidade
        '''
        self._quantidade = new_qtd
    
    def _decorator(foo):
        ''' Decorador para a funcao de predict. '''
        def mostra(self) :
            print("Siga Rexa compras nas redes sociais e não perca as melhores ofertas!")
            foo(self)
        return mostra
    
    @_decorator
    def predict(self) -> str:
        ''' 
            Realiza predição de venda baseado na quantidade do produto e no preco deles. 
            
            O modelo foi treinado utilizando o preco do produto e a quantidade em estoque para
                prever a venda deste produto.
        '''
        try:
            logging.info('Iniciando a predicao')
            modelo = joblib.load('estoque.joblib')
        
        except FileNotFoundError as error:
            logging.warning('Excecao estourada')
            mensagem = "Não pudemos finalizar sua compra :( mas já estamos verificando!"
            raise ModeloZoado
        
        except Exception as error:
            logging.warning('Excecao estourada')
            mensagem = "Não pudemos finalizar sua compra :( mas vamos verificar o que ocorreu!"
            raise Generico
            
        else:
            estoque = self._quantidade
            preco = self._preco_produto
            input_ = [[estoque, preco]]
            venda = modelo.predict(input_)[0]
            logging.info('Predicao finalizada')
            mensagem = f"A previsão de vendas do produto {self._nome} é de {int(venda)} unidades, então corra já e garanta a sua!"
        
        finally:
            logging.info('Processo finalizado')
            print("Obrigada por comprar conosco")
            print(mensagem)
        return mensagem
    
    def __str__(self) -> str:
        return "O produto foi instanciado"


# In[9]:


tv = Produto(3, 'tv da sony', 'Setor A', 'Boleto', 19.0, 10.8, 2)


# In[10]:


print(tv)


# In[11]:


tv._id, tv.nome, tv.lugar, tv.tipo_pagamento, tv.preco_frete, tv.preco_produto, tv.quantidade


# In[12]:


tv.predict()


# In[13]:


class Sistema():
    ''' Instancia um sistema de gencia de estoque. '''
    def __init__(self, nome_sistema: str):
        self._nome_sistema = nome_sistema 
        
    @property
    def nome_sistema(self) -> str:
        ''' Retorna o nome do sistema. '''
        return self._nome_sistema
    
    @nome_sistema.setter
    def nome_sistema(self, new_nome: str):
        '''
            Altera o nome do sistema.
            :new_name: novo nome
        '''
        self._nome_sistema = new_nome
        
    def coloca_produto(self, prod: Produto) -> str: 
        '''
            Insere o produto no banco de dados.
            
            Params
            :prod: Produto a ser inserido
        '''
        
        produto = produtos.insert_one(prod.__dict__).inserted_id
        
        logging.info('Produto inserido no banco')
        
        return f'Produto: {prod._nome} inserido!'
        
    def mostra_prod(self, prod: Produto) -> dict:
        '''
            Mostra o produto no banco de dados.
            
            Params
            :prod: Produto a ser mostrado
        '''
        logging.info('Mostrando dados do banco')
        return produtos.find_one({"_id": prod._id})
    
    def retira_produto(self, prod: Produto):
        '''
            Retira o produto no banco de dados.
            
            Params
            :prod: Produto a ser retirado
        '''
        produtos.delete_one({"_id": prod._id})
        logging.info('Produto excluido no banco')
    
    def atualiza_produto(self, prod: Produto, attr, new_attr):
        '''
            Atualiza o produto no banco de dados.
            
            Params
            :prod: Produto a ser atualizado
        '''
        produtos.update_one({'_id': prod._id}, {'$set': {attr: new_attr}})
        logging.info('Produto atualizado')
    
    @staticmethod
    def mostra_todos() -> dict:
        ''' Mostra os produtos no banco de dados. '''
        logging.info('Mostrando dados do banco')
        return produtos.find()
        
    def __str__(self) -> str:
        return "O sistema foi instanciado"


# In[14]:


sis = Sistema('sistemoso')


# In[15]:


print(sis)


# In[16]:


sis.nome_sistema


# In[17]:


sis.coloca_produto(tv)


# In[18]:


sis.mostra_prod(tv)


# In[19]:


sis.atualiza_produto(tv, '_nome', 'Tevelisao')


# In[20]:


sis.mostra_prod(tv)


# In[21]:


sis.retira_produto(tv)


# In[22]:


sis.mostra_todos()


# In[ ]:




