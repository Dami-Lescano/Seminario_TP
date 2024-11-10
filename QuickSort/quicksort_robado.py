import random
import math


def quick_sort(array, low, high):
  if low < high:
    # Dividir y acomodar pivote
    pi = partition(array, low, high)
  
    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)
 
def partition(array, low, high): 
  global calculos
  # Pivote el de la derecha
  pivot = array[high]
  
  # Apuntador del último elemento más pequeño
  i = low - 1
 
  for j in range(low, high):
    if array[j] <= pivot:
      # Avanzar apuntador
      i = i + 1
      # Intercambiar elementos
      calculos += 1
      (array[i], array[j]) = (array[j], array[i])
  
  # Al final intercambiar el pivote
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  
  # Regresa la posición final del pivote
  return i + 1

calculos = 0
arr = [random.randint(0, 1000) for _ in range(4000)]#list(range(0,100))#[random.randint(0, 1000) for _ in range(100)]#[4,6,2,5,8,9,5,10]
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)



print("calculos en 500 elementos: " + str(calculos))

esperado = 4000 * math.log(4000, 10)
print("calculos esperados: " + str(esperado))


