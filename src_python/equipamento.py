class Equipamento:
    def __init__(self, id_equipamento: str, nome: str, modelo: str):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.modelo = modelo
        self.status_operacional = False

    def ligar(self) -> bool:
        self.status_operacional = True
        print(f"[{self.nome}] Equipamento ligado com sucesso.")
        return self.status_operacional

    def desligar(self) -> bool:
        self.status_operacional = False
        print(f"[{self.nome}] Equipamento desligado.")
        return self.status_operacional