class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.alive = True


class ThroneInheritance(object):
    def __init__(self, kingName):
        self.root = Node(kingName)
        self.allNode = {kingName: self.root}

    def birth(self, parentName, childName):
        parent = self.allNode[parentName]
        parent.children.append(Node(childName))
        self.allNode[childName] = parent.children[-1]

    def death(self, name):
        self.allNode[name].alive = False

    def getInheritanceOrder(self):
        res = []
        self.dfs(self.root, res)
        return res

    def dfs(self, node, res):
        if node.alive:
            res.append(node.name)
        for child in node.children:
            self.dfs(child, res)


# Your ThroneInheritance object will be instantiated and called as such:
ops = ["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death",
       "getInheritanceOrder"]
vals = [["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"],
        ["bob", "asha"], [], ["bob"], []]

kingName = vals[0][0]
parentName = vals[1][0]

obj = ThroneInheritance(kingName)
for i in range(1, len(ops)):
    if ops[i] == "birth":
        parentName = vals[i][0]
        childName = vals[i][1]
        obj.birth(parentName, childName)
    elif ops[i] == "death":
        name = vals[i][0]
        obj.death(name)
    elif ops[i] == "getInheritanceOrder":
        print(obj.getInheritanceOrder())
