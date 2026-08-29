class Solution:
    def generateTrees(self, n: int):
        
        def generate(start, end):
            if start > end:
                return [None]

            result = []
            for root_val in range(start, end + 1):
                left_trees = generate(start, root_val - 1)
                right_trees = generate(root_val + 1, end)
                for left in left_trees:
                    for right in right_trees:

                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right

                        result.append(root)

            return result

        return generate(1, n)