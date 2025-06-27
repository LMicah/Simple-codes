import sys
import requests 


def main():
     escolha, quantidade = getchoice()
     preco = getprice(escolha, quantidade)
     print(f"${preco:,.4f}")



def getchoice():
     moedas = []
     resposta = requests.get("https://rest.coincap.io/v3/assets?apiKey=") #<------ your coincap api key goes here
     dados = resposta.json()
     moedas = [moeda["id"] for moeda in dados["data"]]

     if len(sys.argv) == 3:   
        moeda = sys.argv[1].lower()
        if moeda in moedas:
            try:
                quantidade = float(sys.argv[2])
                return moeda, quantidade
            except ValueError:
                sys.exit("Amount must be a number.")
        else:
            sys.exit("Coin must be in the coin API database.")
     else:
        sys.exit("Program should have two arguments: the coin name and the amount.")



def getprice(x, y):
     try:
          resposta = requests.get("https://rest.coincap.io/v3/assets?apiKey=") #<------- your coincap api key also goes here
          dados = resposta.json()
     except requests.RequestException:
          sys.exit()

     for moeda in dados["data"]:
          if moeda["id"] == x:
                    return (float(moeda["priceUsd"]) * float(y))
     else:
          sys.exit("coin not found")
    
if __name__ == "__main__":
    main()
