import random
letters = ["A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#","$","%","¨","&","*","(",")"]
print("faz o L")
nr_letters = int(input("quantas letras vc quer companheiro?\n"))
nr_numbers = int(input("quantos numeros vc quer companheiro?\n"))
nr_symbols = int(input("quantos simbulos vc quer companheiro?\n"))

passwork_list = []

for char in range(1, nr_letters + 1):
  passwork_list.append(random.choice(symbols))

for char in range (1, nr_numbers + 1):
  passwork_list += random.choice(numbers)
   
for char in range (1, nr_symbols + 1):
  passwork_list += random.choice(symbols)
  
print(passwork_list)
random.shuffle(passwork_list)
print(passwork_list)

passwork = ""
for char in passwork_list:
  passwork += char 

print(f"sua senha e essa meu companheiro:{passwork}")