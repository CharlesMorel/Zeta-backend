import numpy as np
def z_decrypt(e_data):
    KEY=3
    e_data=[w for w in e_data]

    # Change each character to unicode value with KEY
    e_data=[ord(i)-KEY for i in e_data]
    # Reverse tab
    e_data=e_data[::-1]
    # Change unicode value to character with KEY
    e_data=[chr(i-KEY) for i in e_data]
    # Roll tab with KEY
    e_data=np.roll(e_data, -KEY)

    return e_data

def z_encrypt(data):
    KEY=3
    e_data=[w for w in str(data)]

    # Roll tab with KEY
    e_data=np.roll(e_data, KEY)
    # Change each character to unicode value with KEY
    e_data=[ord(i)+KEY for i in e_data]
    # Reverse tab 
    e_data=e_data[::-1]
    # Change unicode value to character with KEY
    e_data=[chr(i+KEY) for i in e_data]

    return e_data

