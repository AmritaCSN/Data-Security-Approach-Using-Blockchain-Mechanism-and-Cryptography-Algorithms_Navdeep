
from Blockchain import Blockchain
from hashlib import sha256
from des_new import DESCipher
import time


def des_resource_consumption():
    #print("Msg Len\tenc_time\tdec_time")
    print("Msg Len\tenc_time\tblock_creation_time\tdec_time")
    new_chain = Blockchain()
    key='12387654'
    if(len(key)%8 != 0):
        padding = (8-len(key)%8) * '0'
        key += padding
    

    # for i in range(0, 20, 1):
    #     message = 'a'*(2**i)
    for i in range(1):
        message = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

        des_algo=DESCipher(key)

        enc_start_time=time.time()
        encrypted_data=des_algo.encrypt(message)
        enc_time = time.time()-enc_start_time

        block_creation_start_time = time.time()
        new_block = new_chain.create_new_block(encrypted_data)
        new_chain.chain.append(new_block)
        block_creation_time = time.time() - block_creation_start_time
        
        # now we extract the data and check the time
      
        dec_start = time.time()
        
        encrypted_data = new_chain.chain[-1].data # the most recently added block has our encrypted data.
        # also accessing it through the blockchain to take in account the time
        # rather than directly doing new_block.data
        decrypted_data = des_algo.decrypt(encrypted_data)
        dec_time = time.time() - dec_start

        print(f"{len(message)}\t{enc_time:.12f}\t{block_creation_time:.12f}\t{dec_time:.12f}")
        #print(f"{len(message)}\t{enc_time:.28f}\t{block_creation_time:.16f}")
        # print(encrypted_data)
        # print(f"{len(message)}\t{enc_time:.28f}\t{dec_time:.20f}")
        # print(f"{len(message)}")
        # print(f"{enc_time:.20f}")
        # print(f"{dec_time:.20f}")
        # print(f"{block_creation_time:.12f}")
    
    print("\n\nBlock No.\tBlock Data")
    for i in range(len(new_chain.chain)):
        print(f"\t{i+1}\t{new_chain.chain[i].data}")



if __name__ == '__main__':
    des_resource_consumption()