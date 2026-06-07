from loader import load_file
from memory import memory


def main():
    commands = load_file("entradas/exemplo_enunciado.txt")
    print(commands)
    mem = memory(16)
    mem.occupy(0, commands[0])
    mem.print_free_blocks()
    print(mem)
    mem.occupy(1, commands[1])
    mem.print_free_blocks()
    print(mem)
    mem.occupy(2, commands[2])
    mem.print_free_blocks()
    print(mem)
    mem.release(commands[3])
    mem.print_free_blocks()
    print(mem)
    mem.release(commands[3])
    mem.print_free_blocks()
    print(mem)


if __name__ == "__main__":
    main()


