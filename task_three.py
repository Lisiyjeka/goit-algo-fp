import heapq
import math

class Graph:
    """Клас для представлення зваженого графа"""
    
    def __init__(self):
        self.vertices = {}
    
    def add_edge(self, u, v, weight):
        """Додавання ребра між вершинами u та v з вагою weight"""
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        
        self.vertices[u].append((v, weight))
    
    def dijkstra(self, start):
        """
        Алгоритм Дейкстри з використанням бінарної купи
        
        Повертає відстані та попередні вершини для всіх вершин графа
        """
        # Ініціалізація відстаней (від стартової вершини до всіх інших)
        distances = {vertex: math.inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        distances[start] = 0
        
        # Створення бінарної купи
        heap = [(0, start)]  # (відстань, вершина)
        
        while heap:
            # Вилучення вершини з мінімальною відстанню з купи
            current_dist, current = heapq.heappop(heap)
            
            # Пропуск, якщо знайдено кращий шлях
            if current_dist > distances[current]:
                continue
            
            # Обробка сусідів поточної вершини
            for neighbor, weight in self.vertices[current]:
                distance = current_dist + weight
                
                # Якщо знайдено коротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    # Додавання до купи
                    heapq.heappush(heap, (distance, neighbor))
        
        return distances, previous
    
    def print_shortest_paths(self, start):
        """Виведення найкоротших шляхів від стартової вершини до всіх інших"""
        distances, previous = self.dijkstra(start)
        
        print(f"Найкоротші шляхи з вершини '{start}':")
        print("-" * 50)
        
        for vertex in sorted(self.vertices.keys()):
            if vertex == start:
                continue
                
            if distances[vertex] == math.inf:
                print(f"До '{vertex}': шляху не існує")
            else:
                # Відновлення шляху
                path = []
                current = vertex
                while current is not None:
                    path.append(current)
                    current = previous[current]
                path.reverse()
                
                print(f"До '{vertex}': {' → '.join(path)} (відстань: {distances[vertex]})")


# Ініціалізація та запуск алгоритму Дейкстри
if __name__ == "__main__":
    #  Створення графа
    graph = Graph()
    
    #  Додавання ребер 
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 8)
    graph.add_edge('C', 'E', 10)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'F', 6)
    graph.add_edge('E', 'F', 3)
    
    #  Запуск алгоритму Дейкстри з вершини 'A'
    graph.print_shortest_paths('A')