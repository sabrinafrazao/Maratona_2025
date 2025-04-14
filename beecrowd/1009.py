n = input()

salario = float(input())

total_vendas = float(input())

comissao = 0.15*total_vendas

novo_salario = comissao + salario

print(f"TOTAL = R$ {novo_salario:.2f}")