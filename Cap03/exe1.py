import math


def is_prime_number(num):
    if num <= 1:
        return False
    #O +1 é para incluir o limite superior na verificação, pois a função range do Python é exclusiva no final (para ir até 10, o range precisa ir até 11)
    for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        return False # Encontrou um divisor, então não é primo
    return True

def validarEntradaDoUsuario(entrada):
    if is_prime_number(entrada_do_usuario):
        print(f"The number {entrada_do_usuario} is prime.")
    else:
        print(f"The number {entrada_do_usuario} is not prime.")


#Início do programa:   
print("****Prime Number Checker****")
try:
    entrada_do_usuario = int(input("Enter an integer: "))
    validarEntradaDoUsuario(entrada_do_usuario)
except ValueError:
    print("Invalid input. Please enter a valid integer number. To check the number is prime it needs to be more than 1.")
    entrada_do_usuario = int(input("Enter an integer: "))
    validarEntradaDoUsuario(entrada_do_usuario)
    




