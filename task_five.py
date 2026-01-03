import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph




def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()


def generate_color(start_color, n):
    """Генерує список  кольорів від темних до світлих відтінків"""
    colors = []
    
    r = int(start_color[1:3], 16)
    g = int(start_color[3:5], 16)
    b = int(start_color[5:7], 16)
    
    for i in range(n):
        factor = i / (n) 
        new_r = min(255, int(r + (255 - r) * factor))
        new_g = min(255, int(g + (255 - g) * factor))
        new_b = min(255, int(b + (255 - b) * factor))
        
        color = f"#{new_r:02x}{new_g:02x}{new_b:02x}"
        colors.append(color)
    
    return colors


def bfs_traversal(root):
    """Обхід дерева в ширину з використанням черги"""
    if not root:
        return []
    
    visited_order = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        visited_order.append(current)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return visited_order


def dfs_traversal(root):
    """Обхід дерева в глибину з використанням стеку"""
    if not root:
        return []
    
    visited_order = []
    stack = [root]
    
    while stack:
        current = stack.pop()
        visited_order.append(current)
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return visited_order


def apply_colors_to_tree(visited_nodes, start_color):
    """Застосовує кольори до вузлів дерева за порядком обходу"""
    color_gradient = generate_color(start_color, len(visited_nodes))
    
    for i, node in enumerate(visited_nodes):
        node.color = color_gradient[i]


def create_sample_tree():
    """Створює тестове дерево"""
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(7)
    return root


if __name__ == "__main__":
    # Створюємо дерево для BFS
    tree_bfs = create_sample_tree()
    bfs_nodes = bfs_traversal(tree_bfs)
    apply_colors_to_tree(bfs_nodes, "#1296F0")
    draw_tree(tree_bfs, "BFS обхід дерева")
    
    # Створюємо дерево для DFS
    tree_dfs = create_sample_tree()
    dfs_nodes = dfs_traversal(tree_dfs)
    apply_colors_to_tree(dfs_nodes, "#1296F0")
    draw_tree(tree_dfs, "DFS обхід дерева")