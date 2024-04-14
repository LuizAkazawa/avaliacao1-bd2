from bson import ObjectId
from database import Passageiro, Corrida, Motorista
class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nota = float(input("Informe a nota do motorista: "))

        # Criando uma ou mais Corridas
        corridas = []
        while True:

            nome_passageiro = input("Informe o nome do passageiro: ")
            documento_passageiro = input("Informe o documento do passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            passageiro = passageiro.to_dict()

            nota_corrida = input("Informe a nota da corrida: ")
            distancia_corrida = input("Informe a distancia da corrida: ")
            valor_corrida = input("Informe o valor da corrida: ")
            corrida = Corrida(nota_corrida, distancia_corrida, valor_corrida, passageiro)
            corridas.append(corrida)
            mais_corridas = input("Deseja adicionar outra corrida? (s/n): ")
            if mais_corridas.lower() != 's':
                break

        # Criando o Motorista com as corridas
        motorista = Motorista(nota)
        for corrida in corridas:
            motorista.adicionar_corrida(corrida)

        # Convertendo o Motorista para dicionário
        motorista_dict = motorista.to_dict()

        # Criando o Motorista no banco de dados
        self.motorista_model.criar_motorista(motorista_dict)
        print("Motorista criado com sucesso!")

    def read_motorista(self):
        id_motorista = input("Informe o ID do motorista: ")
        filtro = {"_id": ObjectId(id_motorista)}
        motorista = self.motorista_model.ler_motorista(filtro)
        if motorista:
            print("Motorista encontrado:")
            print(f"ID: {motorista['_id']}")
            print(f"Nota: {motorista['nota']}")
            print()
            print("Corridas:")
            for corrida in motorista['corridas']:
                print(f"Nota: {corrida['nota']}", end=" / ")
                print(f"Distância: {corrida['distancia']}km", end=" / ")
                print(f"Valor: R${corrida['valor']}")
                passageiro = corrida['passageiro']
                print("Passageiro:", end=" ")
                print(f"Nome: {passageiro['nome']}", end=" / ")
                print(f"Documento: {passageiro['documento']}", end=" / ")
                print()
                print()
        else:
            print("Motorista não encontrado.")
    def update_motorista(self):
        id_motorista = input("Informe o ID do motorista que deseja atualizar: ")
        filtro = {"_id": ObjectId(id_motorista)}
        motorista = self.motorista_model.ler_motorista(filtro)
        if motorista:
            print("Motorista encontrado. Informe a nova nota:")
            nova_nota = float(input("Nova nota: "))
            novos_dados = {"nota": nova_nota}
            self.motorista_model.atualizar_motorista(filtro, novos_dados)
        else:
            print("Motorista não encontrado.")

    def delete_motorista(self):
        id_motorista = input("Informe o ID do motorista que deseja excluir: ")
        filtro = {"_id": ObjectId(id_motorista)}
        motorista = self.motorista_model.ler_motorista(filtro)
        if motorista:
            confirmacao = input("Tem certeza que deseja excluir este motorista? (s/n): ")
            if confirmacao.lower() == "s":
                self.motorista_model.deletar_motorista(filtro)
                print("Motorista excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
        else:
            print("Motorista não encontrado.")

    def run(self):
        print("Bem-vindo ao CLI do Motorista!")
        print("Comandos disponíveis: create, read, update, delete, quit")
        super().run()