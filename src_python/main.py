from equipamento import Equipamento
from sensor_temperatura import SensorTemperatura

def main():
    print("--- Iniciando Simulação do Laboratório ---\n")
    
    # 1. Instanciando um Equipamento genérico de bancada
    fonte_bancada = Equipamento("EQ-01", "Fonte Regulada CC", "Minipa 3005")
    fonte_bancada.ligar()
    
    print("\n-------------------------------------------")
    
    # 2. Instanciando e testando o Sensor de Temperatura (Herança)
    sensor_forno = SensorTemperatura("SE-02", "Sensor Interno do Forno", "PT100")
    
    # Tentativa de leitura com o sensor desligado (Deve falhar)
    sensor_forno.ler_temperatura()
    
    # Ligando e efetuando leituras
    sensor_forno.ligar()
    sensor_forno.ler_temperatura()
    sensor_forno.ler_temperatura()
    
    sensor_forno.desligar()

if __name__ == "__main__":
    main()