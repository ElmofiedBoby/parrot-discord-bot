import os

def get_token():  

    filename = ".env"

    with open(filename) as f:
        token = f.readlines()

    token = token[0].split("=")

    return token[1]