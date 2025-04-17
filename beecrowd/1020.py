idade = int(input())

# Calcula quantos anos completos existem nos dias fornecidos
ano = idade // 365

# Atualiza o valor da idade para o restante dos dias após remover os anos completos
idade = idade % 365

# Calcula quantos meses completos existem no restante dos dias
mes = idade // 30

# Atualiza o valor da idade para o restante dos dias após remover os meses completos
idade = idade % 30

#O que sobrou são os dias restantes (menos de um mês)
dias = idade

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")
