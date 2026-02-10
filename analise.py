import pandas as pd

# Dados extraídos do seu relatório
dados = {
    'Mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Gastos_2024': [461768.77, 413682.94, 373433.47, 427637.10, 486656.39, 485789.80, 572276.05, 578317.35, 378257.65, 456680.01, 353478.45, 377265.35],
    'Gastos_2025': [318810.73, 389165.53, 259089.87, 385302.13, 243202.38, 331909.22, 416177.79, 352542.34, 307894.58, 443460.09, 393175.52, 357671.10],
    'KM_2025': [291489, 336905, 331596, 310867, 353161, 343503, 360179, 390361, 340528, 370871, 360680, 389878]
}

df = pd.DataFrame(dados)

# Cálculos
df['Economia_R$'] = df['Gastos_2024'] - df['Gastos_2025']
df['Custo_por_Mil_KM'] = df['Gastos_2025'] / (df['KM_2025'] / 1000)

print("--- ANÁLISE PROFISSIONAL DE MANUTENÇÃO ---")
print(f"Economia Total: R$ {df['Economia_R$'].sum():,.2f}")
print("\nKPI: Custo por Mil KM por Mês:")
print(df[['Mes', 'Custo_por_Mil_KM']].round(3))