class Node:
    value = 0
    left = None
    right = None

def deep_first_search(node, value_to_find):
    if node is None:
        return False
    
    if node.value == value_to_find:
        return True
    
    return deep_first_search(node.left, value_to_find) or \
        deep_first_search(node.right, value_to_find)

maze=[]

def find_next_position(position, visited_position):
    return 0,0

def item_value(position):
    return maze[position[0], position[1]]

def deep_first_search(position, visited_position, value_to_find):
    if item_value(position) == value_to_find:
        return True

    next_position = find_next_position(position, visited_position)
    if next_position:
        return deep_first_search(next_position, visited_position + [position], value_to_find)