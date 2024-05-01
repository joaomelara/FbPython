dias = int(input("quale os dias?"))
anos = (dias//365)
meses = (dias%365)//30
diast = (dias%365)%30

print(f"Anos: {anos}\nMeses: {meses}\nDias: {diast}")