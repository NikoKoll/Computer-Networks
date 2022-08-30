from curses import BUTTON1_RELEASED
from importlib.resources import path
from itertools import count
from operator import index
from os import TMP_MAX
from queue import PriorityQueue
import re
from sys import path_hooks
from textwrap import indent
import csv
import os

class DGraph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(graph, start_vertex):

        path1=[]

        D = {v+1:float('inf') for v in range(graph.v-1)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        print('\nBhma bhma dhmiourgias pinaka')

        count=0
        while not pq.empty():
            count=count+1
            (dist, current_vertex) = pq.get()
            graph.visited.append(current_vertex)

            for neighbor in range(graph.v):
                if graph.edges[current_vertex][neighbor] != -1:
                    distance = graph.edges[current_vertex][neighbor]
                    if neighbor not in graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
                            path1.append(current_vertex)
                            path1.append(neighbor)
                            print(D)
        
        path1.reverse()
        
        fast1=[]
        fast2=[]
        for i in range(len(path1)):
            if i%2==0:
                fast1.append(path1[i])
            else :
                fast2.append(path1[i])

        res = []
        res2 = []
        for id ,i in enumerate(fast1):
            if i not in res:
                res.append(i)
                res2.append(fast2[id])

        for i in range(len(res)-1):
            for j in range(0, len(res)-i-1):
                if res[j] > res[j + 1]:
                    res[j], res[j + 1] = res[j + 1], res[j]
                    res2[j], res2[j + 1] = res2[j + 1], res2[j]

        print('\nH sintomoterh diadromh gia kathe komvo me bash ton komvo ekiniseis(apo - pros)')
        for i,j in enumerate(res):
            print(j, '-', res2[i])

        return D

class BGraph:
    def __init__(self2, num_of_vertices):
        self2.v = num_of_vertices
        self2.visited = []

    def add_edge(self, u, v, weight):
        self.visited.append([u, v, weight])
        self.visited.append([v, u, weight])

    def bellman_ford(graph, start_vertex):

        path1=[]

        D = {v+1:float('inf') for v in range(graph.v-1)}

        D[start_vertex] = 0

        print('\nBhma bhma dhmiourgias pinaka')

        for _ in range(graph.v):
            for u, v, weight in graph.visited:
                if D[u] != float("Inf") and D[u] + weight < D[v]:
                    D[v] = D[u] + weight
                    path1.append(u)
                    path1.append(v)
                    print(D)

        for u, v, weight in graph.visited:
            if D[u] != float("Inf") and D[u] + weight < D[v]:
                print("Graph contains negative weight cycle")
                return

        path1.reverse()
        
        fast1=[]
        fast2=[]
        for i in range(len(path1)):
            if i%2==0:
                fast1.append(path1[i])
            else :
                fast2.append(path1[i])

        res = []
        res2 = []
        for id ,i in enumerate(fast1):
            if i not in res:
                res.append(i)
                res2.append(fast2[id])

        for i in range(len(res)-1):
            for j in range(0, len(res)-i-1):
                if res[j] > res[j + 1]:
                    res[j], res[j + 1] = res[j + 1], res[j]
                    res2[j], res2[j + 1] = res2[j + 1], res2[j]
        
        print('\nH sintomoterh diadromh gia kathe komvo me bash ton komvo ekiniseis(apo - pros)')
        for i,j in enumerate(res):
            print(j, '-', res2[i])

        return D

def main():

    headers = ["Satrting Node", "Ending Node", "Weight"]
    list=[["1", "2", "null"], ["1", "4", "null"], ["2", "3", "null"], ["2", "4", "null"], ["3", "5", "null"], ["3", "6", "null"], ["4", "5", "null"], ["5", "6", "null"]]
    newlist=[]
    try:
        for i, j, f in list:
            print(i, '-',j)
            tmp = int(input('Bale to kostos tou parpanou komvou: '))
            newlist.append([i,j,tmp])
    except ValueError:
        print ("Lathos eisagogi to programma termatizei")
        return

    with open("nodes.csv", "w") as nd:
        node = csv.writer(nd)
        node.writerow(headers)
        node.writerows(newlist)

    try:
        arxikos_komvos = int(input('\nBale ton arxiko komvo: '))
        while True:
            if(arxikos_komvos <=0 and arxikos_komvos<=6):
                arxikos_komvos = int(input('Lathos arithmos Xana dokimase: '))
            else:
                break
    except ValueError:
        print ("Lathos eisagogi to programma termatizei")
        return

    algoritmos = (input('\nBale ton algoritmo pou tha xrisimopioithei (D=  link-state (Dijkstra, \nB= distance vector (Bellman-Ford), DB= kai gia ta duo): '))
    while True:
        if(algoritmos == 'D' or algoritmos == 'B' or algoritmos == 'DB'):
            break
        else:
            algoritmos = (input('Lathos algoritmos xana dokimase: '))

    g = DGraph(7)
    b = BGraph(7)
    with open('nodes.csv') as file_obj:
        heading = next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            g.add_edge(int(row[0]), int(row[1]), int(row[2]))
            b.add_edge(int(row[0]), int(row[1]), int(row[2]))
    
    os.system('clear')

    if(algoritmos == 'D'):
        D = g.dijkstra(arxikos_komvos)
        print('Ta elaxista kostoi ana komvo me basei tou dosmeno komvou ekiniseis einai gia ton algorithmo Dijkstra')
        print(D)
    elif(algoritmos == 'B'):
        B= b.bellman_ford(arxikos_komvos)
        print('Ta elaxista kostoi ana komvo me basei tou dosmeno komvou ekiniseis einai gia ton algorithmo Bellman Ford')
        print(B)
    else:
        D = g.dijkstra(arxikos_komvos)
        print('Ta elaxista kostoi ana komvo me basei tou dosmeno komvou ekiniseis einai gia ton algorithmo Dijkstra')
        print(D)
        B= b.bellman_ford(arxikos_komvos)
        print('Ta elaxista kostoi ana komvo me basei tou dosmeno komvou ekiniseis einai gia ton algorithmo Bellman Ford')
        print(B)

main()