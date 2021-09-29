def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Andrés", "José", "Luis", "Sofia", "Catalina"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n") #Salto de línea en Python

def run():
    write()

if __name__ == "__main__":
    run()
