from instruction import instruction


def worst_fit(mem, comandos):
    for i in comandos:
        if  i.type == "OUT":
            mem.release(i)
        elif i.type == "IN":
            melhorIndice = None
            melhorTam = -1

            for indice, j in enumerate(mem.blocks):
                if j["owner"] == None:
                    if j["size"] >= i.size:
                        if j["size"] > melhorTam:
                            melhorTam = j["size"]
                            melhorIndice = indice
            
            
            if melhorIndice == None:
                print("ESPAÇO INSUFICIENTE DE MEMORIA")
            else:
                print(i, mem)
                mem.occupy(melhorIndice, i)
                
def circular_fit(mem, comandos):
    for i in comandos:
        if i.type == "OUT":
            mem.release(i)
            print(i, mem)
        elif i.type == "IN":
            encontrou = False
            NumBlocos = len(mem.blocks)

            for j in range(NumBlocos):
                indice = (mem.pointer + j) % NumBlocos
                blocoAtual = mem.blocks[indice]

                if blocoAtual["owner"] is None and blocoAtual["size"] >= i.size:
                    mem.occupy(indice, i)
                    print(f"{mem.pointer} | {i} | {mem}")
                    mem.pointer = indice
                    encontrou = True

                    break

            if not encontrou:
                print("ESPAÇO INSUFICIENTE DE MEMORIA")
                
