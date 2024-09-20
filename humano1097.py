print("\n--------------------------------\n")
print("Act 9 clase humano")
print("Emmanuel Salcido Mat: 22308051281097")
# Zona de clases
class Humano1097:
    # Zona de atributos
    peso=0
    genero=""
    estatura=0
    color_de_pelo=""
    ojos=""

    # Zona de funciones dentro de la clase
    def correr1097(self,n):
        print(f"{n} esta corriendo")

    def caminar1097(self,c):
        print(f"{c} esta caminando")

    def saltar1097(self,s):
        print(f"{s} esta saltando")

    def viajar1097(self,v):
        print(f"{v} esta viajando")

# Zona de creacion de objetos

emmanuel=Humano1097()
clara=Humano1097()

# Zona de usando objeto
print("\n--------------------------------\n")
print("-----Resultado para Emmanuel--")

emmanuel.peso=70
emmanuel.genero="Masculino"
emmanuel.estatura=1.70
emmanuel.color_de_pelo="Negro"
emmanuel.ojos="Cafes"

print(f"Peso : {emmanuel.peso}kg")
print(f"Genero: {emmanuel.genero}")
print(f"Estatura : {emmanuel.estatura}")
print(f"Color de pelo : {emmanuel.color_de_pelo}")
print(f"Color de ojos : {emmanuel.ojos}")
emmanuel.correr1097("Emmanuel")
emmanuel.caminar1097("Emmanuel")
emmanuel.saltar1097("Emmanuel")
emmanuel.viajar1097("Emmanuel")
print("\n--------------------------------\n")
print("-----Reultados para Clara-----")

clara.peso=60
clara.estatura=1.60
clara.color_de_pelo="Cafe"
clara.ojos="Cafes"

print(f"Peso : {clara.peso}kg")
print(f"Estatura : {clara.estatura}")
print(f"Color de pelo : {clara.color_de_pelo}")
print(f"Color de ojos : {clara.ojos}")
clara.correr1097("Clara")
clara.caminar1097("Clara")
clara.viajar1097("Clara")
print("\n--------------------------------\n")