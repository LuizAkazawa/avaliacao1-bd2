from typing import Collection
import pymongo # pip install pymongo


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://root:root@cluster0.75axnwx.mongodb.net/"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.collection)
            self.collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)

class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

    def to_dict(self):
        return {
            "nome": self.nome,
            "documento": self.documento
        }


class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Motorista:
    def __init__(self, nota):
        self.nota = nota
        self.corridas = []

    def adicionar_corrida(self, corrida):
        self.corridas.append(corrida)

    def to_dict(self):
        return {
            "nota": self.nota,
            "corridas": [corrida.__dict__ for corrida in self.corridas]
        }
