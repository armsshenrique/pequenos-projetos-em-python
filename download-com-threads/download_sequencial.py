import wget
import time
import threading

host = "http://arquivos.afonsomiguel.com/"
tempoinicial = time.time()
threadsnumber = 0

def download(n):
    wget.download(host + f"arquivo_{n}.jpg", f"arquivo_{n}.jpg")


while True:
    if threading.active_count() < 2:
        print("Tempo: ", time.time() - tempoinicial)
        break

while (threadsnumber<10):
    threading.Thread(target=download, args=[t]).start()
    t = t + 1