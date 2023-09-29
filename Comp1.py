import random

# Ejercicio 1: ¿Es un número primo?
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

# Ejercicio 2: Siguiente número primo
def next_prime(n):
    n += 1
    while True:
        if is_prime(n):
            return n
        n += 1

# Ejercicio 3: Mediana de tres valores
def median_of_three(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort()
    return nums[1]

# Ejercicio 4: Contraseña aleatoria
def generate_random_password():
    password_length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(password_length))
    return password

# Ejercicio 5: Calcular la hipotenusa
def compute_hypotenuse(a, b):
    return (a**2 + b**2)**0.5
