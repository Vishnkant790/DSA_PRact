class Solution:
    def generateTrees(self, n: int):
        
        def generate(start, end):
            # Empty subtree
            if start > end:
                return [None]

            result = []

            # Every value can be root
            for root_val in range(start, end + 1):

                # Generate all possible left subtrees
                left_trees = generate(start, root_val - 1)

                # Generate all possible right subtrees
                right_trees = generate(root_val + 1, end)

                # Combine every left with every right
                for left in left_trees:
                    for right in right_trees:

                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right

                        result.append(root)

            return result

        return generate(1, n)