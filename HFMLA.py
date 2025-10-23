meniu = ['papanasi']*10 + ['ceafa']*3 + ['guias']*6
preturi = [['papanasi', 7], ['ceafa', 10], ['guias', 5]]
studenti = ['Liviu', 'Ion', 'George', 'Ana', 'Florica'] 
comenzi = ['guias', 'ceafa', 'ceafa', 'papanasi', 'ceafa'] 
tavi = ['tava']*7 
istoricul_comenzilor = []

portii = {}

while len(studenti) > 0:
    meniu.remove(comenzi[0])
    if comenzi[0] in portii.keys():
        portii[comenzi[0]] += 1
    else:
        portii[comenzi[0]] = 1
    comanda = f"{studenti.pop(0)} a comandat {comenzi.pop(0)}."
    istoricul_comenzilor.append(comanda)
    print(comanda)
    tavi.pop()
print()

istoricul_portiilor = 'Nu s-a comandat nimic.'
for key in portii.keys():
    if 'nimic' in istoricul_portiilor:
        istoricul_portiilor = 'S-a comandat'
    istoricul_portiilor += f' {portii[key]} {key},'
istoricul_portiilor= istoricul_portiilor

print(f"Mai sunt {len(tavi)} tavi.")

for item in preturi:
    print(f"Mai este {item[0]}: {item[0] in meniu}.")

total = 0
for item in preturi:
    if item[0] in portii.keys():
        total += portii[item[0]]*item[1]
print(f"\nCantina a incasat: {total} lei.")

print(f"Produse care costa maxim 7 lei: {list(pret for pret in preturi if pret[1] <= 7)}\n")
