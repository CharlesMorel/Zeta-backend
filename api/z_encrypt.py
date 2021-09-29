import numpy as np
def z_encrypt(data):
    KEY=31
    e_data=[w for w in str(data)]

    e_data=np.roll(e_data, KEY)
    e_data=[ord(i)+KEY for i in e_data] 
    e_data=e_data[::-1]
    e_data=[chr(i+KEY) for i in e_data]
    

    return e_data

def z_decrypt(e_data):
    KEY=31
    e_data=[w for w in e_data]
    e_data=[ord(i)-KEY for i in e_data]
    e_data=e_data[::-1]
    e_data=[chr(i-KEY) for i in e_data]
    e_data=np.roll(e_data, -KEY)
    
    return e_data