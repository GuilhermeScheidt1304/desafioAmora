# Simulador de correção de entradas e parcelas - AMORA

print("------ AMORA ------")
print("Seja bem vindo ao nosso Simulador de Compras!\n")

# Entradas Obrigatórias

valor_imovel = float(input("Digite o valor do imóvel:"))
percentual_entrada = int(input("Digite o percentual de entrada: (ex.: 5)"))
anos_contrato = int(input("Digite a duração do contrato em anos: (ex.: 3)"))

# Calcular taxa de juros

taxa_juros = float(input("Digite a taxa de juros anual (entre 5% e 12%)"))
while taxa_juros < 5 or taxa_juros > 12:
    taxa_juros = float(
        input("Taxa de juros inválida!!! Digite uma taxa de juros entre 5% e 12%: "))

# Calculos Iniciais

valor_entrada = valor_imovel * (percentual_entrada / 100)
total_a_guardar = valor_imovel * 0.15
parcela_mensal = total_a_guardar / (anos_contrato * 12)

# Valores iniciais informados pelo usuário

print(f"\n--- Valores Iniciais ---")
print(f"Valor da entrada: R$ {valor_entrada:,.2f}")
print(f"Valor a guardar: R$ {total_a_guardar:,.2f}")
print(f"Parcela mensal base: R$ {parcela_mensal:,.2f}\n")

# Informandos valores corrigidos anualmente

print("--- Valores corrigidos por ano ---")
for ano in range(1, anos_contrato + 1):
    parcela_anoN_igpm = parcela_mensal * (1 + 0.06)**(ano-1)
    parcela_anoN_juros = parcela_mensal * (1 + taxa_juros/100)**(ano-1)
    
    print(f"Ano {ano}:")
    print(f"Parcela mensal corrigida pelo IGPM: R$ {parcela_anoN_igpm:,.2f}")
    print(f"Parcela mensal corrigida pela taxa de juros informada pelo usuário: R$ {parcela_anoN_juros:,.2f}")

