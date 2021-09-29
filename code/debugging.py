def run(num):
    divisors = lambda num: [i for i in range(1, num + 1) if num % i == 0]

    while True:
        try:
            num = int(input("Ingresa un número: "))
            if num < 0:
                raise Exception("Debes ingresar un número positivo")
            print(divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un número")
        except Exception:
            print("Debes ingresar un número positivo")

if __name__ == "__main__":
    run()

