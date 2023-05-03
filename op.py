
from tqdm import tqdm
import time
import socket

def op():
    print("BEM-VINDO(A)")
    for i in tqdm(range(10)):
        time.sleep(0.5)
        tqdm.write(f'verificando se a Atualizaçãoes {i+1}')
    
    time.sleep(1)

    print("     _               _    _                                  _    _     ")
    print("    | |             | |  | |                                | |  | |    ")
    print("  __| |  ___   __ _ | |_ | |__    ______   _ __ ___    __ _ | |_ | |__  ")
    print(" / _` | / _ \ / _` || __|| '_ \  |______| | '_ ` _ \  / _` || __|| '_ \ ")
    print("| (_| ||  __/| (_| || |_ | | | |          | | | | | || (_| || |_ | | | |")
    print(" \__,_| \___| \__,_| \__||_| |_|          |_| |_| |_| \__,_| \__||_| |_|")

def hostName():
    name = socket.gethostname()
    return name
