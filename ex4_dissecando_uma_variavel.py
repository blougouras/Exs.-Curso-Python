x = input('Digite algo: ')

print(type(x))
print('É numérico?', x.isnumeric())
print('É alfanumérico?', x.isalnum())
print('É alfabético? ', x.isalpha())
print('Está em maiúsculo?', x.isupper())
print('Está em minúsculo?', x.islower())
print('Só tem espaços?', x.isspace())