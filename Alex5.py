import requests


dia = input(f'Informe a data no formato "MM-DD-AAAA": ')
url = requests.get(f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?%40dataCotacao={dia}&%24format=json")
dicio = url.json()

print(f"A cotação para compra é de {dicio['value'][0]['cotacaoCompra']}")
print(f"A cotação para venda é de {dicio['value'][0]['cotacaoVenda']}")