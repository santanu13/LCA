Find the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree (BST) efficiently by leveraging the BST property:

For a node cur:

If p.val < cur.val and q.val < cur.val, then LCA lies in the left subtree.

If p.val > cur.val and q.val > cur.val, then LCA lies in the right subtree.

Otherwise, cur is the LCA.
