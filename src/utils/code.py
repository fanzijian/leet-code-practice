class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def DFS(root):
    if not root:
        return None
    queue = [root]
    while queue:
        cur = queue.pop()
        print cur.val
        if cur and cur.right:
            queue.append(cur.right)
        if cur and cur.left:
            queue.append(cur.left)
    return


