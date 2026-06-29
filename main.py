from loader import load_file
from memory import memory
from manager import Method, worst_fit, circular_fit, buddy
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--method",
        choices=["worst-fit", "circular-fit", "buddy"],
        required=True
    )
    parser.add_argument(
        "--input",
        required=True
    )
    parser.add_argument(
        "--size",
        type=int,
        required=True
    )
    args = parser.parse_args()

    if args.method == "worst-fit":
        method = Method.WORST_FIT
    elif args.method == "circular-fit":
        method = Method.CIRCULAR_FIT
    elif args.method == "buddy":
        method = Method.BUDDY

    comandos = load_file(args.input)
    mem = memory(args.size)


    match(method):
        case Method.WORST_FIT:
            print(f"Tipo de execução: {method}")
            print(60*"-")
            print(f"Arquivo{8*" "}|    Memória")
            print(60*"-")
            print(f"{15*" "}|    {mem.print_memory()}")
            worst_fit(mem, comandos)
        case Method.CIRCULAR_FIT:
            print(f"Tipo de execução: {method}")
            print(60*"-")
            print(f"Arquivo{8*" "}|    Memória")
            print(60*"-")
            print(f"{15*" "}|    {mem.print_memory()}")
            circular_fit(mem, comandos)
        case Method.BUDDY:
            print(f"Tipo de execução: {method}")
            print(120*"-")
            print(f"Arquivo{8*" "}|    Memória{(85-27)*" "}|    Total de fragmentação interna")
            print(120*"-")
            print(f"{15*" "}|    {mem.print_memory()}")
            buddy(mem, comandos)


if __name__ == "__main__":
    main()

