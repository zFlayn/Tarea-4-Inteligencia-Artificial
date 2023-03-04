import random
import time

def create_instance(num_nodos):
  instance={}
  for i in range(1,num_nodos+1):
     #Cuantos nodos adyacentes tiene el nodo i
     cuantos_adyacentes= random.randint(1,num_nodos-1)
     listas_nodos_adyacentes= random.sample(range(1,num_nodos),cuantos_adyacentes)
     while(i in listas_nodos_adyacentes):
         cuantos_adyacentes=random.randint(1,num_nodos-1)
         listas_nodos_adyacentes=random.sample(range(1,num_nodos),cuantos_adyacentes)

     lista_tuplas=[]
     for j in range(0,len(listas_nodos_adyacentes)):
         lista_tuplas.append((listas_nodos_adyacentes[j],random.randint(1,100)))
     instance[i]= lista_tuplas
  return instance

def non_informed_search(start, goal, graph):
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        current_node = path[-1]
        if current_node == goal:
            return path
        for neighbor, weight in graph[current_node]:
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                frontier.append(new_path)
    return None

if __name__ == '__main__':
    num_nodos = 40
    instance = create_instance(num_nodos)
    print("Instancia:")
    print(instance)
    start, end = random.sample(range(1,num_nodos+1), 2)
    print(f"Inicio: {start}, Destino: {end}")
    start_time = time.time()
    path = non_informed_search(start, end, instance)
    end_time = time.time()
    print(f"Camino encontrado: {path}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos.")
