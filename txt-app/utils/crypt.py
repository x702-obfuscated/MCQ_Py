import os, sys

suppress = True

def gen_key(length):
    return os.urandom(length)

def xor_crypt(data,key):
    return bytes(a ^ b for a,b in zip(data,key))

def enxor(file_in, file_out, key_file):
    with open(file_in, "rb") as file:
        data = file.read()

    key = gen_key(len(data))

    with open(key_file, "wb") as file:
        file.write(key)

    encrypted_data = xor_crypt(data, key)

    with open(file_out, "wb") as file:
        file.write(encrypted_data)

    if not suppress:
        print(f"File encrypted and saved to {file_out}")
        print(f"Key saved to {key_file}")

def dexor(file_in, file_out, key_file):
    with open(file_in, "rb") as file:
        data = file.read()

    with open(key_file, "rb") as file:
        key = file.read()

    decrypted_data = xor_crypt(data, key)

    with open(file_out, "wb") as file:
        file.write(decrypted_data)
    
    if not suppress:
        print(f"File decrypted and saved to {file_out}")


