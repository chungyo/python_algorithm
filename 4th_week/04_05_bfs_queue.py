# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
from collections import deque

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# 1. 시작 노드를 큐에 넣는다
# 2. 현재 큐의 노드를 빼서 visited에 추가한다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가
# 4. 큐가 비워질 때까지 반복

def bfs_queue(adj_graph, start_node):
    queue = deque([start_node]) # queue[1]
    visited_node = []

    while queue:
        current_node = queue.popleft() # current_node = 1
        visited_node.append(current_node) # visited = [1]
        for adj_node in adj_graph[current_node]: # adj_node -> 2일때 , 그다음 3일때 ->
            if adj_node not in visited: # 2가 visited에 없으니
                queue.append(adj_node) # queue 뒤에 2를 넣어줌 => queue[2] -> queue[2,3] -> queue[2,3,4]

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!