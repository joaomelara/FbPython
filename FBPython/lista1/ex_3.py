seg = int(input("quale os secunditos?"))
horas = seg//3600
min = (seg%3600)//60
segundos = (seg%3600)%60

print(f"Segundos: {segundos}\nMinutos: {min}\nHoras: {horas}")
