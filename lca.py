
class TreeNode:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
        
        
class BinarySearchTree:
    def __init__(self):
        self.root=None
        
    def insert_into_bst(self, val):
        
        self.root = self.recursive_insert_into_bst(self.root, val)
        
    def recursive_insert_into_bst(self, node, val):
        
        ''' Final Insertion into Tree after all the recuresive call ends '''
        if not node:
            return TreeNode(val)
        
        elif val < node.val:
            ''' Check all the traversing '''
            node.left = self.recursive_insert_into_bst(node.left, val)
            
        else:
            node.right = self.recursive_insert_into_bst(node.right, val)
        
        return node
            
        
    def find(self, val):
        
        return self.recursive_find(self.root, val)
    
    def recursive_find(self, node, val):
        
        if not node is None:
            
            if node.val == val:
                return node

            elif val < node.val:
                return self.recursive_find(node.left, val)

            return self.recursive_find(node.right, val)
        else:
            return None
        
    # Find Lowest Common Ancestor
    def find_lca(self, p, q):
        return self._lowest_common_ancestor(self.root, p, q)

    def _lowest_common_ancestor(self, node, p, q):
        
        if not node is None and not p is None and not q is None:
            
            while node:
                if p.val < node.val and q.val < node.val:
                    node = node.left
                elif p.val > node.val and q.val > node.val:
                    node = node.right
                else:
                    return node
            
        return None
    
    def print_all_nodes(self):
        def in_order(node):
            if node:
                in_order(node.left)         # Step 1: Go left
                print(node.val, end=" ")   # Step 2: Visit node
                in_order(node.right)       # Step 3: Go right

        print("All nodes in BST (in-order):")
        in_order(self.root)                # Start from root
        print()
        
if __name__ == "__main__":
    
    nodes=[6,2,8,0,4,7,9,3,5]
    
    obj = BinarySearchTree()
    
    for each in nodes:
        obj.insert_into_bst(each)
        
    # Define nodes for which to find LCA
    p_val = 7
    q_val = 9
    p = obj.find(p_val)
    q = obj.find(q_val)

    # Find and print LCA
    lca_node = obj.find_lca(p, q)
    
    if lca_node:
        print(f"The Lowest Common Ancestor of {p_val} and {q_val} is: {lca_node.val}")
    else:
        print("LCA not found.")
        
    obj.print_all_nodes()
