from instruction import instruction
from manager import worst_fit, circular_fit

class memory:
    def __init__(self, size):
        self.size = size
        self.blocks = [{"start": 0, "size": size, "owner": None}]
        self.pointer = 0   # used by circular-fit

    def print_free_blocks(self):
        text = "|"
        for block in self.blocks:
            if block["owner"] is None:
                text += f" {block['size']} |"
        print(text)

    def occupy(self, i, inst: instruction):
        block = self.blocks[i]
        original_start = block["start"]
        remainder = block["size"] - inst.size

        block["size"] = inst.size
        block["owner"] = inst.id

        if remainder > 0:
            self.blocks.insert(i + 1, {
                "start": original_start + inst.size,
                "size": remainder,
                "owner": None,
            })

    def release(self, inst: instruction):
        for block in self.blocks:
            if block["owner"] == inst.id:
                block["owner"] = None
                break
        self.coalesce()

    def coalesce(self):
        i = 0
        while i < len(self.blocks) - 1:
            current = self.blocks[i]
            next_block = self.blocks[i + 1]
            if current["owner"] is None and next_block["owner"] is None:
                current["size"] += next_block["size"]
                self.blocks.pop(i + 1)        # merge, do NOT advance i
            else:
                i += 1

    def worst_fit(self, comandos):
        worst_fit(self, comandos)

    def circular_fit(self, comandos):
        circular_fit(self, comandos)

    def __str__(self):
        text = ""
        for block in self.blocks:
            if block["owner"] is None:
                owner = "free"
            else:
                owner = block["owner"]
            text += f"[{owner}: start={block['start']} size={block['size']}] "
        return text
    


    __repr__ = __str__
