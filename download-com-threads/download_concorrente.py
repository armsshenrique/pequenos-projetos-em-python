import wget
import time
from threading import Thread
from threading import active_count

url = "http://arquivos.afonsomiguel.com/"
inicio = time.time()
t = 0


def download(n):
    wget.download(url + f"arquivo_{n}.jpg", f"arquivo_{n}.jpg")


while t < 10:
    Thread(target=download, args=[t]).start()
    t = t + 1

while True:
    if active_count() < 2:
        print("Tempo: ", time.time() - inicio)
        break
