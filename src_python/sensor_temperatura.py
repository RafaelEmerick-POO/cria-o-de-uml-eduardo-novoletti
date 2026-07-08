from equipamento import Equipamento

class SensorTemperatura(Equipamento):
    def __init__(self, id_equipamento: str, nome: str, modelo: str, unidade_medida: str = "°C"):
        # Chamada do construtor da classe pai (Equipamento)
        super().__init__(id_equipamento, nome, modelo)
        self.unidade_medida = unidade_medida
        self.temperatura_atual = 20.0  # Temperatura base simulada

    def ler_temperatura(self) -> float:
        if not self.status_operacional:
            print(f"[{self.nome}] Erro: Não é possível ler a temperatura com o sensor desligado.")
            return 0.0
        
        # Simulação de alteração de temperatura para teste
        self.temperatura_atual += 0.5
        print(f"[{self.nome}] Leitura atual: {self.temperatura_atual}{self.unidade_medida}")
        return self.temperatura_atual