from datetime import datetime
DATA_DE_VENCIMENTO_ORIGINAL = input(
    "Esta é sua data de vencimento, 01/10/2019, digite a sua nova data: ")
VALOR_ORIGINAL = float(input('Este é o valor da mensalidade: R$ 1.000,00: '))
NOVA_DATA_DE_VENCIMENTO = input(
    "Nova data de vencimento 15/09/2019, Nova data de vencimento: ")
VALOR_de_Desconto = int(input('Valor de desconto: '))

vence = datetime.strptime(DATA_DE_VENCIMENTO_ORIGINAL, "%d/%m/%Y")
vence1 = datetime.strptime(NOVA_DATA_DE_VENCIMENTO, "%d/%m/%Y")
datapg = abs(vence1-vence).days

valor = VALOR_ORIGINAL

nvalor = valor - (valor * ((VALOR_de_Desconto / 100 / 30) * datapg))

print(f"{nvalor:.2f}")