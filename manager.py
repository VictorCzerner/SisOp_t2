from instruction import instruction
from enum import Enum

class Method(Enum):
    WORST_FIT = 0
    CIRCULAR_FIT = 1
    BUDDY = 2

def worst_fit(mem, comandos):
    for i in comandos:
        if  i.type == "OUT":
            mem.deallocate(i)
            tab = 15 - len(str(i))
            print(f"{i}{tab*" "}|    {mem.print_memory()}")
        elif i.type == "IN":
            melhorIndice = None
            melhorTam = -1

            for indice, j in enumerate(mem.blocks):
                if j.id == None:
                    if j.size >= i.size:
                        if j.size > melhorTam:
                            melhorTam = j.size
                            melhorIndice = indice
            
            
            if melhorIndice == None:
                tab = 15 - len(str(i))
                print(f"{i}{tab*" "}|    ESPAÇO INSUFICIENTE DE MEMORIA")
            else:
                mem.allocate(melhorIndice, i)
                tab = 15 - len(str(i))
                print(f"{i}{tab*" "}|    {mem.print_memory()}")
                
def circular_fit(mem, comandos):
    for i in comandos:
        if i.type == "OUT":
            mem.deallocate(i)
            tab = 15 - len(str(i))
            print(f"{i}{tab*" "}|    {mem.print_memory()}")
        elif i.type == "IN":
            encontrou = False
            NumBlocos = len(mem.blocks)

            for j in range(NumBlocos):
                indice = (mem.last_visited + j) % NumBlocos
                blocoAtual = mem.blocks[indice]

                if blocoAtual.id is None and blocoAtual.size >= i.size:
                    mem.allocate(indice, i)
                    tab = 15 - len(str(i))
                    print(f"{i}{tab*" "}|    {mem.print_memory()}")
                    mem.last_visited = indice
                    encontrou = True

                    break

            if not encontrou:
                tab = 15 - len(str(i))
                print(f"{i}{tab*" "}|    ESPAÇO INSUFICIENTE DE MEMORIA")
                
def buddy(mem, commands):
    for i in commands:
        if i.type == "OUT":
            mem.dealocate_buddy(i)
            tab = 15 - len(str(i))
            text = f"{i}{tab*" "}|    {mem.print_memory()}"
            tab2 = 85 - len(text) 
            print(f"{text}{tab2*" "}|    {mem.get_internal_fragmentation()}")
        elif i.type == "IN":
            best_block = None
            best_block_idx = None
            for idx, block in enumerate(mem.blocks):
                if block.id != None:
                    continue
                if block.size >= i.size:
                    if best_block == None:
                        best_block = block
                        best_block_idx = idx
                        continue
                    if block.size < best_block.size:
                        best_block = block
                        best_block_idx = idx

            if best_block == None:
                tab = 15 - len(str(i))
                print(f"{i}{tab*" "}|    ESPAÇO INSUFICIENTE DE MEMORIA")
                continue
            
            mem.allocate_buddy(index=best_block_idx, inst=i)
            tab = 15 - len(str(i))
            text = f"{i}{tab*" "}|    {mem.print_memory()}"
            tab2 = 85 - len(text) 
            print(f"{text}{tab2*" "}|    {mem.get_internal_fragmentation()}")
    