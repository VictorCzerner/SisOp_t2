from instruction import instruction
from block import Block


class memory:
    def __init__(self, size):
        self.size = size
        self.blocks = [Block(size=size, start=0, id=None)]


    def allocate(self, i, inst):
        block = self.blocks[i]
        original_start = block.start
        free_memory = block.size - inst.size

        block.size = inst.size
        block.id = inst.id

        if free_memory > 0:
            self.blocks.insert(i + 1, Block(id=None, start=original_start + inst.size, size=free_memory))

    def allocate_buddy(self, index, inst):
        best_block = self.blocks[index]
        while True:
            if best_block.size / 2 >= inst.size:
                best_block.size = best_block.size / 2
                best_block.pos = (best_block.pos * 2) + 1
                new_block = Block(id=None, start=best_block.start + best_block.size, size=best_block.size, pos=best_block.pos + 1)
                self.blocks.insert(index + 1, new_block)
            else:
                break
        best_block.id = inst.id
        best_block.frag = best_block.size - inst.size


    def deallocate(self, inst):
        for block in self.blocks:
            if block.id == inst.id:
                block.id = None
                self.merge_free_blocks(self.blocks.index(block))
                break
    
    def dealocate_buddy(self, inst):
        block = None
        for blc in self.blocks:
            if blc.id == inst.id:
                block = blc
                break

        while True:
            block.id = None
            block.frag = 0
            if block.pos == 0:
                break
            if block.pos % 2 == 1:
                pair = self.blocks[self.blocks.index(block) + 1]
                if pair.id == None:
                    block.size = block.size + pair.size
                    block.pos = block.pos // 2
                    self.blocks.remove(pair)
                else:
                    break
            else:
                pair = self.blocks[self.blocks.index(block) - 1]
                if pair.id == None:
                    pair.size = block.size + pair.size
                    pair.pos = (block.pos // 2) - 1
                    self.blocks.remove(block)
                    block = pair
                else:
                    break  
                     


            
    def merge_free_blocks(self, index):
        if index + 1 <= len(self.blocks):
            if self.blocks[index + 1].id == None:
                self.blocks[index].size = self.blocks[index].size + self.blocks[index + 1].size
                self.blocks.pop(index + 1)
        if index > 0:
            if self.blocks[index - 1].id == None:
                self.blocks[index - 1].size += self.blocks[index].size
                self.blocks.pop(index)

    def print_memory(self):
        text = "|"
        for block in self.blocks:
            if block.id is None:
                text += f" {block.size} |"
        return text
    
    def get_internal_fragmentation(self):
        value = 0
        for block in self.blocks:
            if block.id is not None:
                value += block.frag
        return value
    
