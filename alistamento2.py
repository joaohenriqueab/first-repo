"""
VERIFICADOR DE IDADE PARA ALISTAMENTO MILITAR
DATA: DEZEMBRO, 2025
Descrição: Esse programa verifica a idade do usuário e informa se ele deve se alistar para o serviço militar obrigatório no Brasil.
"""

while True:
    try:
        idade = int(input("\nDigite sua idade: "))
        if idade < 0:
            print("Idade não pode ser negativa! Tente novamente.")
        else:
            break # pra sair do loop, se a idade for valida 
    except ValueError:
        print("Por favor, digite apenas números inteiros!")

# Cálculos basicos 
from datetime import date
ano_atual = date.today().year
ano_nascimento = ano_atual - idade
ano_alistamento = ano_nascimento + 18

# mostra o ano de nascimento uma unica vez
print(f'\n você nasceu em {ano_nascimento}.')

if idade > 18:
    anos_atraso = idade - 18
    print("\nVocê já deveria ter se alistado para o serviço militar obrigatório.")
    print(f'Seu alistamento foi em {ano_alistamento}.')
    print(f' você já passou {anos_atraso} ano(s) do prazo de alistamento.')

elif idade == 18: 
    print("\nVocê deve se alistar para o serviço militar obrigatório este ano.")
    print(f'Seu alistamento é em {ano_alistamento}.')

else:  # idade < 18
    anos_faltando = 18 - idade
    print("\nVocê ainda não precisa se alistar para o serviço militar obrigatório.")
    print(f'Seu alistamento será em {ano_alistamento}.')
    print(f'Faltam {anos_faltando} ano(s) para o seu alistamento.')