custoFabrica = int(input("Poe um valor ae: "))
percDist = custoFabrica * 0.28
percImps = custoFabrica * 0.45



custoConsumidor = custoFabrica + percDist + percImps

print(f"O custo do consumidor é {custoConsumidor:.2f}")