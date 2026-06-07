from loader import load_file
from memory import memory


def main():
    comandos = load_file("entradas/exemplo_enunciado.txt")
    print(comandos)
    mem = memory(60)
    mem.circular_fit(comandos)
    print(mem)


if __name__ == "__main__":
    main()


