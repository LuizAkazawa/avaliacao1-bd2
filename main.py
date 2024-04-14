from database import Database, Passageiro, Corrida, Motorista
from motoristadao import MotoristaDAO
from writeAJson import writeAJson
from cli import MotoristaCLI

db = Database(database="Aplicativo", collection="motoristas")

motorista_dao = MotoristaDAO(db)

motorista_cli = MotoristaCLI(motorista_dao)
motorista_cli.run()

'''
SCHEMA:

{
  "$jsonSchema": {
    "bsonType": "object",
    "required": ["nota", "corridas"],
    "properties": {
      "nota": {
        "bsonType": ["double"],
        "description": "Nota do motorista"
      },
      "corridas": {
        "bsonType": "array",
        "description": "Lista de corridas do motorista",
        "items": {
          "bsonType": "object",
          "properties": {
            "nota": {
              "bsonType": ["double"],
              "description": "Nota da corrida"
            },
            "distancia": {
              "bsonType": "double",
              "description": "Distância da corrida"
            },
            "valor": {
              "bsonType": ["double"],
              "description": "Valor da corrida"
            },
            "passageiro": {
              "bsonType": "object",
              "description": "Dados do passageiro",
              "properties": {
                "nome": {
                  "bsonType": "string",
                  "description": "Nome do passageiro"
                },
                "documento": {
                  "bsonType": "string",
                  "description": "Documento do passageiro"
                }
              }
            }
          }
        }
      }
    }
  }
}


'''
