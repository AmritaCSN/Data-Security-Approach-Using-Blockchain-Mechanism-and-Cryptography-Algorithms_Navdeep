from Block import Block


class Blockchain():
    def __init__(self):
            block_0 = self.create_genesis_block()
            self.chain = [block_0]
   
    def create_genesis_block(self):
        data = 'Genenis Block' # empty string
        genesis_block = Block('0', data) # initial hash is zero
        return genesis_block

    def create_new_block(self, encrypted_text):
    
        previous_block = self.chain[-1]
        new_block = Block(previous_block.hash, encrypted_text)
        return new_block
