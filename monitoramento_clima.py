import requests

class CidadeClima:
    def __init__(self, nome, temperatura, umidade, condicao):
        self.nome = nome
        self.temperatura = temperatura
        self.umidade = umidade
        self.condicao = condicao

    def __str__(self):
        return f"Cidade: {self.nome} | Temp: {self.temperatura}°C | Umidade: {self.umidade}% | Clima: {self.condicao}"

def main():
    cidades = ['São Paulo', 'London', 'Tokyo', 'New York', 'Paris']
    chave_api = "4d034d5a6b90064571dd976a5c6499b5"
    relatorio_clima = []

    for cidade in cidades:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"
        
        try:
            resposta = requests.get(url)
            
            if resposta.status_code == 200:
                dados = resposta.json()
                
                nome = dados["name"]
                temperatura = dados["main"]["temp"]
                umidade = dados["main"]["humidity"]
                condicao = dados["weather"][0]["description"]
                
                obj_clima = CidadeClima(nome, temperatura, umidade, condicao)
                relatorio_clima.append(obj_clima)
            else:
                print(f"Não foi possível encontrar a cidade ou ocorreu um erro: {cidade}")
                
        except requests.exceptions.RequestException:
            print(f"Erro de conexão ao buscar a cidade: {cidade}")
        except Exception:
            print(f"Ocorreu um erro inesperado com a cidade: {cidade}")

    print("\n--- Relatório de Clima ---")
    for item in relatorio_clima:
        print(item)

if __name__ == "__main__":
    main()
