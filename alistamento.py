idade = int(input('Digite sua idade: '))

ano_que_nasceu = 2025 - idade
anos_para_maioridade = 18 - idade

print(f'Você nasceu em {ano_que_nasceu}.')

if idade > 18:
    
    anos_atraso = idade - 18
    ano_alistamento = ano_que_nasceu + 18
    print('Você é maior de idade.')
    print('Se for homem, você já deveria ter se alistado (para mulheres é opcional).')
    print(f'Você deveria ter se alistado em {ano_alistamento}.')
    print(f'Já se passaram {anos_atraso} ano(s) da idade obrigatória.') 

elif idade == 18:
    
    print('Você é maior de idade.')
    print(' Se for homem, você deve se alistar imediatamente este ano (2025)!')
    print('Para mulheres, o alistamento é opcional.')

else:
    
    anos_faltam = 18 - idade
    ano_alistamento = ano_que_nasceu + 18
    print('Você é menor de idade.')
    print('Fique tranquilo, ainda não precisa se alistar.')
    print(f'Faltam {anos_faltam} ano(s) para você completar 18 anos.')
    print(f'Você deverá se alistar em {ano_alistamento} (se for homem).')