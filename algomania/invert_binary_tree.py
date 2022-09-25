def solution(tree):
    if tree.left is None and tree.right is None:
        return tree

    tree.left, tree.right = tree.right, tree.left

    if tree.left:
        tree.left = solution(tree.left)
    if tree.right:
        tree.right = solution(tree.right)
        
    return tree