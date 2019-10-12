class Relationship:
    def __init__(self):
        self.people = {}
        self.relation_hash = {}

    def pre_process(self, realtion_array):
        for ele in realtion_array:
            node = (ele[0], ele[1])
            if node in self.relation_hash:
                self.relation_hash[node].append(ele[2])
            else:
                self.relation_hash[node] = [ele[2]]

        for ele in realtion_array:
            if ele[0] in self.people:
                self.people[ele[0]].add(ele[1])
            else:
                self.people[ele[0]] = set()
                self.people[ele[0]].add(ele[1])

    def build_relation(self, start, end, realtion_array):
        self.pre_process(realtion_array)
        path = []
        res = []
        start_node = Node(start)
        start_node.relationship = self.people[start]
        # nodes = self.people[start]
        path.append(start)
        for person in start_node.relationship:
            person_node = Node(person)
            person_node.relationship = self.people[person]
            for relation in self.relation_hash[(start, person)]:
                path.append(relation)
                self.dfs(person_node, end, path, res)
                path.pop()
        return res

    def dfs(self, person_node, end, path, res):
        path.append(person_node.name)

        # base case
        if person_node.name == end:
            res.append(path[:])
        # general case
        for child in person_node.relationship:
            child_node = Node(child)
            if child in self.people:
                child_node.relationship = self.people[child]
            else:
                child_node.relationship = []
            for relation in self.relation_hash[(person_node.name, child)]:
                path.append(relation)
                self.dfs(child_node, end, path, res)
                path.pop()
        path.pop()
#
class Node:
    def __init__(self, name):
        self.name = name
        self.relationship = [] # list of [name, relation]

class Relationship2:
    def __init__(self):
        self.people = {}
        self.relation_hash = {}

    def pre_process(self, realtion_array):
        for ele in realtion_array:
            node = (ele[0], ele[1])
            if node in self.relation_hash:
                self.relation_hash[node].append(ele[2])
            else:
                self.relation_hash[node] = [ele[2]]

        for ele in realtion_array:
            if ele[0] in self.people:
                self.people[ele[0]].add(ele[1])
            else:
                self.people[ele[0]] = set()
                self.people[ele[0]].add(ele[1])

    def build_relation(self, start, end, realtion_array):
        self.pre_process(realtion_array)
        path = []
        res = []
        start_node = Node(start)
        start_node.relationship = self.people[start]
        # nodes = self.people[start]
        path.append(start)
        for person in start_node.relationship:
            person_node = Node(person)
            person_node.relationship = self.people[person]
            for relation in self.relation_hash[(start, person)]:
                path.append(relation)
                self.dfs(person_node, end, path, res)
                path.pop()
        return res

    def dfs(self, person_node, end, path, res):
        path.append(person_node.name)

        # base case
        if person_node.name == end:
            res.append(path[:])
        # general case
        for child in person_node.relationship:
            child_node = Node(child)
            if child in self.people:
                child_node.relationship = self.people[child]
            else:
                child_node.relationship = []
            for relation in self.relation_hash[(person_node.name, child)]:
                path.append(relation)
                self.dfs(child_node, end, path, res)
                path.pop()
        path.pop()

# realtion_array = [['a', 'b', 'brother'], ['b', 'c', 'dad'], ['d', 'e', 'friend'], ['a', 'e', 'friend'], ['e', 'c', 'brother'],
#             ['e', 'c', 'friend'], ['b', 'e', 'friend']]


r = Relationship()
realtion_array = [['a', 'b', 'mom'], ['b', 'c', 'bro'], ['b', 'c', 'fri'], ['c', 'f', 'dad']]

start = 'a'
end = 'f'
print(r.build_relation(start, end, realtion_array))
