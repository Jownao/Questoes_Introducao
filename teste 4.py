import os
total_segs= int(input("Por favor, entre com a PORRA dos números q vc quer CARALHO.\n\n"))



horas = total_segs // 3600
dias = horas//86400

segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

if (horas >= 24):

	dias = int(horas / 24)
	horas = int(horas % 24)

os.system('cls')
print(f'a porra do teu tempo foi {dias} dias , {horas} horas , {minutos} minutos, {segs_restantes_final} segundos')
