# Mergesort divide o array ao meio de forma recursiva
# Depois os elementos são agrupados de forma ordenada
def mergeSort(arr, debug=True):
    global tcount
    global ccount

    if len(arr) > 1:

         # Divide o array ao meio (L:R)
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        if debug:
            print("split:", L,R)

        # Ordena cada subarray separadamente
        mergeSort(L, debug)
        mergeSort(R, debug)

        i = j = k = 0

        # Far os merge dos arrays de forma ordenada
        while i < len(L) and j < len(R):
            ccount += 1
            tcount += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Completa a cópia pois um dos arrays esvazia primeiro
        while i < len(L):
            tcount += 1
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tcount += 1
            arr[k] = R[j]
            j += 1
            k += 1

        if debug:
            print('merge:', arr)



# pivot: elemento no fim do array
# Coloca os elementos menores antes do pivot
# Coloca os elementos maiores após o pivot
def partition(arr, low, high, debug:False):
    global tcount
    global ccount
    i = (low-1) # indice que representa o menor elemento            
    pivot = arr[high]       

    if debug:
        print('partition:', arr[low:high], 'pivot:', pivot)
    for j in range(low, high):
        # Os elementos menores que o pivot são colocados a esquerda

        ccount +=1
        if arr[j] <= pivot:
            tcount += 1
            # incrementa o indice do menor elemento
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            if debug:
                print(arr[low:i+1], arr[j+1:high], 'pivot:', pivot)

    tcount +=1
    # reposiciona o pivot no fim dos elementos deslocados
    arr[i+1], arr[high] = arr[high], arr[i+1]
    if debug:
        print(arr[i+1],' pivot <=>', arr[high])
        print(arr)
    # retorna o menor elemento
    return (i+1)

# Essa função é chamada de forma recursiva
# low e high são ajustados para definir o subarray
def quickSort(arr, low, high, debug:False):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi é o novo pivot
        pi = partition(arr, low, high, debug)

        # cada subarray é ordenado separadamente
        quickSort(arr, low, pi-1, debug)
        quickSort(arr, pi+1, high, debug)


import random
import time
tcount = ccount = 0
random.seed()
v = random.sample(range(10000),10000)
ini = time.time()
v1 = v.copy()
mergeSort(v1, False)
print("MERGE", time.time() - ini)
print('Trocas:', tcount, 'Comparações:', ccount)
tcount = ccount = 0
ini = time.time()
v1 = v.copy()
quickSort(v1, 0, len(v1)-1, False)
print("QUICK", time.time() - ini)
print('Trocas:', tcount, 'Comparações:', ccount)