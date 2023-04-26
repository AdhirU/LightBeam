import json

class DirectoryTree:
    """Directory Tree data structure with unqie ID for each directory"""
    counter = 1
    def __init__(self, name, parent=None):
        self.id = DirectoryTree.counter
        self.name = name
        self.parent = parent
        self.children = {}
        DirectoryTree.counter += 1

def load_from_file(file_name:str) -> DirectoryTree:
    """Creates directory tree from .json config file
    
        Keyword arguments:
        file_name -- name of .json file    
    """
    with open(file_name) as f:
        config = json.load(f)

    if "root" not in config:
        raise ValueError("Invalid config file")

    root = DirectoryTree("root", None)
    tree = build_tree(root, config["root"])
    return tree



def build_tree(tree:DirectoryTree, config:dict) -> DirectoryTree:
    """Builds directory tree recursively

        Keyword arguments:
        tree -- directory tree that is constructed recursively
        config -- dictionary that specifies directory structure
    """
    for k, v in config.items():
        new_folder = DirectoryTree(k, parent=tree)
        new_folder = build_tree(new_folder, v)
        tree.children[k] = new_folder

    return tree

