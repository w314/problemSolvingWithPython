import hashlib
from datetime import datetime
from pytz import timezone

# Block class
class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = self.__get_timestamp__()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    # calculates hash, blueprint provided by udacity    
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (self.data + str(self.timestamp)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    # get timestamp of current GMT time
    def __get_timestamp__(self):
        gmt = timezone('GMT')
        now = datetime.now(gmt)
        timestamp = datetime.timestamp(now)
        return timestamp

    # prints out block data    
    def print_block(self):
        print('\ntimestamp: ', self.timestamp)
        print('data: ', self.data)
        print('previous block\'s hash: ', self.previous_hash)
        print('current block\'s hash: ', self.hash)
    

# Blockchain class
class Blockchain:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    # adds block to blockchain    
    def add_block(self, data):
        
        # if the chain is empty
        if not self.head:
            block = Block(data, None)
            self.head = block
            self.tail = block
            return
        
        # if there are already other blocks in the chain     
        block = Block(data, self.tail.hash)
        self.tail.next = block
        self.tail = block
    
    # prints blocks in blockchain
    def print_blockchain(self):
        
        # if chain is empty
        if not self.head:
            print('BlockChain is empty')
            return
    
        block = self.head
        while block:
            block.print_block()
            block = block.next
        
        

# TESTING BLOCKCHAIN
print('\nTESTING BLOCKCHAIN')

print('\nTest Case 1')
print('testing printing empty blockchain')
block_chain = Blockchain()
block_chain.print_blockchain()
# return 'BlockChain is empty'

print('\nTest Case 2')
print('testing adding block to empty block chain')
block_chain.add_block('block_0')
block_chain.print_blockchain()
# returns blockchain with one block where data is: 'block_0', previous hash is 'None'

print('\nTest Case 3')
print('testing adding block to non-empty block chain')
block_chain.add_block('block_1')
block_chain.add_block('block_2')
block_chain.print_blockchain()
# returns blockchain with 3 blocks with 'block_0', 'block_1', 'block_2' as data
# and block2 and block3 has previous hash the hash of the previous block