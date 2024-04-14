class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def criar_motorista(self, motorista):
        try:
            self.db.collection.insert_one(motorista)
            print("Motorista criado com sucesso!")
        except Exception as e:
            print(e)

    def ler_motorista(self, filtro):
        try:
            return self.db.collection.find_one(filtro)
        except Exception as e:
            print(e)

    def atualizar_motorista(self, filtro, novos_dados):
        try:
            self.db.collection.update_one(filtro, {"$set": novos_dados})
            print("Motorista atualizado com sucesso!")
        except Exception as e:
            print(e)

    def deletar_motorista(self, filtro):
        try:
            self.db.collection.delete_one(filtro)
            print("Motorista deletado com sucesso!")
        except Exception as e:
            print(e)

