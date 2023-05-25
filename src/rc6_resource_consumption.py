

from Blockchain import Blockchain
from RC6Encryption import RC6Encryption
from hashlib import sha256
import textwrap
import time


def rc6_resource_consumption():
    new_chain = Blockchain()
    key='12349876'
    # message='a'*(2**10)
    if(len(key)%16 != 0):
        padding = (16-len(key)%16) * '0'
        key += padding
    key=key.encode('UTF-8')
    #print("Msg Len\tenc_time\tdec_time")
    print("Msg Len\tenc_time\tblock_creation_time\tdec_time")
    # for i in range(0, 20, 1):
    #     message = 'a'*(2**i)

    message = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    rc6_algo = RC6Encryption(sha256(key).digest())

    message_chunks=textwrap.wrap(message, 16)
    if(len(message_chunks[-1])<16):
        padding = (16-len(message_chunks[-1]))*'0'
        message_chunks[-1] += padding

    enc_time = 0
    dec_time = 0
    block_creation_time = 0
    
    for chunk in message_chunks:
        chunk=chunk.encode('UTF-8')
        enc_start_time=time.time()
        encrypted_data = rc6_algo.blocks_to_data(rc6_algo.encrypt(chunk))
        enc_time += time.time()-enc_start_time

        block_creation_start_time = time.time()
        new_block = new_chain.create_new_block(encrypted_data)
        new_chain.chain.append(new_block)
        block_creation_time += time.time() - block_creation_start_time
        
        dec_start_time=time.time()
        encrypted_data = new_chain.chain[-1].data
        decrypted_data = rc6_algo.blocks_to_data(rc6_algo.decrypt(encrypted_data))
        dec_time += time.time() - dec_start_time

    print(f"{len(message)}\t{enc_time:.12f}\t{block_creation_time:.12f}\t\t{dec_time:.12f}")
    # print(f"{len(message)}\t{enc_time:.28f}\t{block_creation_time:.16f}")
    # print(f"{len(message)}\t{enc_time:.20f}\t{dec_time:.20f}")
    # print(f"{len(message)}")
    # print(f"{enc_time:.20f}")
    # print(f"{dec_time:.20f}")
    # print(f"{block_creation_time:.12f}")

    print("\n\nBlock No.\tBlock Data")
    for i in range(len(new_chain.chain)):
        print(f"\t{i+1}\t{new_chain.chain[i].data}")
    # new_chain.chain[100].data




if __name__ == '__main__':
    rc6_resource_consumption()