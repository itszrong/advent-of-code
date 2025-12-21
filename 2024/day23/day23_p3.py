from collections import deque, defaultdict
import re

def main():
    with open("day23/save_ex.txt", "r") as f:
        contents = f.read()

    print(len(contents.split('\n')))

    class UnionFind:
        def __init__(self, size):
            self.parent = [i for i in range(size)]
            self.size = [1] * size
            self.max_size = 1
            self.root_of_max = 0

        def find(self, i):
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

        def union(self, i, j):
            root_i = self.find(i)
            root_j = self.find(j)

            if root_i != root_j:
                if self.size[root_i] < self.size[root_j]:
                    root_i, root_j = root_j, root_i

                self.parent[root_j] = root_i
                self.size[root_i] += self.size[root_j]
                if self.size[root_i] > self.max_size:
                    self.max_size = self.size[root_i]
                    self.root_of_max = root_i
                return True
            return False

    
    uf_map = {}
    counter = 0
    elements_list = []
    for line in contents.splitlines():
        elements = re.findall(r'\w+', line)
        for element in elements:
            if element not in uf_map:
                uf_map[element] = counter
                counter += 1

        elements_list.append(elements)

    uf = UnionFind(counter)

    for elements in elements_list:
        for i in range(len(elements)-1):
            uf.union(uf_map[elements[i]], uf_map[elements[i+1]])

    print(uf.root_of_max)
    largest_root = uf.find(uf.root_of_max)
    id_to_label = {idx: label for label, idx in uf_map.items()}
    largest_elements = [
        id_to_label[i]
        for i in range(counter)
        if uf.find(i) == largest_root
    ]
    largest_elements.sort()
    print(','.join(largest_elements))

if __name__ == "__main__":
    main()
