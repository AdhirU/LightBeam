This module contains two python scripts:
- `load_config.py`: This defines the DirectoryTree data structure and the `load_from_file` function. `load_from_file` takes the name of a config file in .json format as input and returns a directory tree built with the specified configuration.

- `run_operations.py`: This defines the `add`, `remove`, `fetch` and `update` functions that operate on a DirectoryTree

To test the operations, on the terminal type `python run_operations.py`. By default, the file creates a directory tree from `config.json` and runs a few sample operations on it.
