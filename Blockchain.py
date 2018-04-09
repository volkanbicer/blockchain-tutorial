
from time import time
import hashlib
import json
from Block import Block
from Transaction import Transaction

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.new_block(previous_hash = 1, proof = 100)

    def new_block(self, proof, previous_hash = None,):
        block = Block(
            index = len(self.chain) + 1,
            timestamp = time(),
            transactions = self.current_transactions,
            proof= proof,
            previous_hash= previous_hash
        )
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append(Transaction(sender, recipient, amount))
        return self.lastBlock.index + 1

    @staticmethod
    def hash(block):
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()

    @property
    def lastBlock(self):
        return self.chain[-1]


    def proof_of_work(self, last_proof):
        proof = 0
        while self.validate_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def validate_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None

        # Only looking for chains longer than neighbours
        max_length = len(self.chain)

        # Grap and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid_chain
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]

            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")

            # Check the has of block is correct
            if block.previous_hash == self.hash(last_block):
                return False

            # Check the pow is correct
            if not self.validate_proof(last_block.proof, block.proof):
                return False

            last_block = block
            current_index += 1

        return True
