
import os

cmd_for_rc6_resource_consumption = "python3 rc6_resource_consumption.py"
cmd_for_aes_resource_consumption = "python3 aes_resource_consumption.py"
cmd_for_des_resource_consumption = "python3 des_resource_consumption.py"

os.system('cls')
print("\n============ RC6 Algorithm in Blockchain=============")
os.system(cmd_for_rc6_resource_consumption)
print("\n============ AES Algorithm in Blockchain=============")
os.system(cmd_for_aes_resource_consumption)
print("\n============ DES Algorithm in Blockchain=============")
os.system(cmd_for_des_resource_consumption)