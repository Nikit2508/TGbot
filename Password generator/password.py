import random


def generator(len_pass = 8):
    simbolls = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ''
    for i in range(len_pass):
        password += random.choice(simbolls)
    return password