import heapq

# Функция алгоритма Дейкстры для поиска кратчайшего пути в графе
def dijkstra(graph, start):
    # Инициализация словаря с изначально бесконечными расстояниями до каждого узла
    distances = {node: float('inf') for node in graph}
    # Устанавливаем расстояние до начального узла равным нулю
    distances[start] = 0

    # Инициализация очереди с приоритетами, в которую добавляется начальный узел с приоритетом 0
    queue = [(0, start)]

    # Цикл выполняется, пока в очереди есть узлы
    while queue:
        # Извлекаем узел с наименьшим приоритетом (т.е. с наименьшим расстоянием до начального узла)
        current_distance, current_node = heapq.heappop(queue)

        # Если текущее расстояние больше уже найденного минимального, пропускаем оставшуюся часть цикла
        if current_distance > distances[current_node]:
            continue

        # Для каждого соседнего узла текущего узла проверяем, можно ли уменьшить расстояние, 
        # проходя через текущий узел
        for neighbor, weight in graph[current_node].items():
            # Расстояние до соседнего узла через текущий узел
            distance = current_distance + weight

            # Если новое расстояние меньше уже найденного, обновляем его и добавляем соседний узел 
            # в очередь с новым приоритетом
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # Возвращаем словарь с минимальными расстояниями до каждого узла
    return distances
