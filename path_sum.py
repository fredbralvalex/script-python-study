class Solution:
    def run(self, root, expected_sum):
        result = []

        if root:
            self.deep_first_search(root, [], 0, expected_sum, result)


        return result

    def deep_first_search(self, node, current_path, sum, expected_sum, result):
        if not node:
            return
        
        sum = sum + node.value
        no_children = not node.left and not node.right
        if no_children and sum == expected_sum:
            result = result + [current_path + [node.value]] 
            return
        
        self.deep_first_search(node.left, current_path + [node.value], sum, expected_sum, result)
        self.deep_first_search(node.right, current_path + [node.value], sum, expected_sum, result)