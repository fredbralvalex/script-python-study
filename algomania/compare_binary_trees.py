#[1,2,3],   [1,2,3]
# [1,2,4,5,3],  [1,2,3]
def solution(tree1, tree2):
    if tree1 and tree2 and tree1.value == tree2.value:
        return solution(tree1.left, tree2.left) and solution(tree1.right, tree2.right)
    else:
        if tree1 == None and tree2 == None:
            return True
        else:
            return False