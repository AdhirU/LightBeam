from load_config import load_from_file, DirectoryTree 


def traverse(path: str, directory_tree:DirectoryTree) -> DirectoryTree:
    """Traverses the directory tree along the path specified

        Keyword arguments:
        path: absolute path that will be traversed
        directory_tree: data structure on which to perform action
    """
        # Check for valid absolute path (starts at root)
    path_list = path.split('/')
    if not path_list or path_list[0] != "root":
        raise ValueError("Invalid path provided")
    path_list = path_list[1:]
    current_folder = directory_tree
    # Traverse to location where folder must be added
    for folder in path_list:
        if folder in current_folder.children:
            current_folder = current_folder.children[folder]
        else:
            raise ValueError("Invalid path provided")
    return current_folder


def add(name:str, path:str, directory_tree:DirectoryTree) -> DirectoryTree:
    """Adds folder to a directory tree at a location specified by the path
        
        Keyword arguments:
        name -- name of the folder that will be added
        path -- absolute path of the location where the folder will be added
        directory_tree -- data structure on which to perform action
    """
    # Get parent folder
    parent = traverse(path, directory_tree)
    # Check for unique name
    if name in parent.children:
        raise ValueError(f"Folder with name {name} already exists")
    # Set parent and child links
    new_folder = DirectoryTree(name, parent=parent)
    parent.children[name] = new_folder
    return new_folder


def remove(path:str, directory_tree:DirectoryTree):
    """Removes folder specified by the path
    
        Keyword arguments:
        path -- absolute path of folder to be removed
        directory_tree -- data structure on which to perform action
    """
    # Get parent folder
    folder = traverse(path, directory_tree)
    parent = folder.parent
    # Delete child folder from parent
    del parent.children[folder.name]


def fetch(folder:DirectoryTree) -> str:
    """Fetch the path of the folder

        Keyword argument:
        folder -- folder whose path will be returned
    """
    # Calls recursive function to fetch path
    path = fetch_rec(folder, "")
    return path


# Recursively fetch the path of folder
def fetch_rec(folder:DirectoryTree, path:str) -> str:
    """Recursively computes the path of a folder by traversing parent
    
        Keyword arguments:
        folder -- current folder in the path
        path -- path string that is accumulated by each recursion
    """
    if folder is None:
        return path
    path = folder.name + "/" + path
    return fetch_rec(folder.parent, path)


def update(path:str, name:str, directory_tree:DirectoryTree) -> DirectoryTree:
    """Updated name of folder specified by path

        Keyword arguments:
        path -- absolute path of folder whose name will be updated
        name -- new name for the folder 
        directory_tree -- data structure on which to perform action
    """
    folder = traverse(path, directory_tree)
    folder.name = name
    return folder


if __name__ == '__main__':
    # Loads data structure from config file
    root = load_from_file("config.json")

    # Print absolute path of folders f5 and f6
    f5 = traverse(path="root/f1/f5", directory_tree=root)
    f6 = traverse(path="root/f3/f6", directory_tree=root)
    print(fetch(f5))
    print(fetch(f6))

    # Add new folder f7 as child of f6
    f7 = add("f7", "root/f3/f6", root)
    print(fetch(f7))

    # Update name of f3 and check path of f7
    update("root/f3", "f3_new", root)
    print(fetch(f7))

    # Remove f5
    remove("root/f1/f5", root)
    try:
        f5 = traverse("root/f1/f5", directory_tree=root)
    except ValueError:
        print("f5 removed")
