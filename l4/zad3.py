from binarytree import Node

tree = Node("A")
tree.left = Node("B")
tree.right = Node("C")
tree.left.left = Node("D")
tree.left.right = Node("E")
tree.left.left.left = Node("F")


print(
    f"Najkrótsza ścieżka od korzenia do liścia to {tree.min_leaf_depth}.\n",
    f"Liście na tej wysokości to {tree.levels[tree.min_leaf_depth]}\n",
    sep="",
)

print("Wierzchołki na każdym z poziomów:")
for i, level in enumerate(tree.levels):
    print(f"{i}: {len(level)}")

print(f"Wierzchołki ogólnie: {tree.size}")

tree.pprint()
