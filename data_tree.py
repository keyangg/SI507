# read data from zep.csv
# assembly data in tree structure
from ete3 import Tree, TreeStyle, TextFace, add_face_to_node
from collections import defaultdict

def build_tree(nodes):
    root = None
    for i in nodes:
        if i[0] == -1:
            root = i
    if not root:
        raise ValueError('no root!')
    data = defaultdict(list)
    for i in nodes:
        if i[0] != -1:
            data[i[1]] = []
            data[i[0]].append(i[1])
    return data, root[1]

def dict_tree_to_str(tree, root):
    if not tree[root]:
        return f'{root}'
    subtrees = [dict_tree_to_str(tree, st) for st in tree[root]]
    return f'({",".join(subtrees)}){root}'
#read csv file To be implemented
# tree_csv = [[-1, 1], [1, 2], [1, 3], [2, 4], [3, 5], [3, 6], [5, 7]]
# tree_dict, root = build_tree(tree_csv)
# t = Tree(dict_tree_to_str(tree_dict, root)+';',  format=1)

ts = TreeStyle()
ts.show_leaf_name = False
def my_layout(node): # https://github.com/etetoolkit/ete/issues/219
    F = TextFace(node.name, tight_text=True)
    add_face_to_node(F, node, column=0, position="branch-right")
ts.layout_fn = my_layout

t.render("mytree.png", w=183, units="mm", tree_style=ts)
