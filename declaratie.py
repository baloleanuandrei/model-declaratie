nume_angajat:str = input("Care este bossancean numele tau? ")
prenume_angajat:str = input("Care este prenumele tau? ")
adresa:str = input("Care este adresa ta? ")
motivul:str = input("Care este motivul? ")
data:int = input("In ce data suntem astazi? ")
eroare:str = "Trebuie introduse date "
if nume_angajat and prenume_angajat and adresa and motivul and data:
    print("Declaratia este pentru" + " " + nume_angajat + " " + prenume_angajat)
    print("Adresa este " + " " + adresa)
    print("Motivul este " + " " + motivul)
    print("Data declaratiei " + " " + data)
else:
    print(eroare)
