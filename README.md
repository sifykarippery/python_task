# Coding Challenge

[![Python Test application(CI/CD)](https://github.com/sifykarippery/python_task/actions/workflows/python_test.yml/badge.svg)](https://github.com/sifykarippery/python_task/actions/workflows/python_test.yml)


## 1. Problem
A directory is given which can contain files and subdirectories. Subdirectories can also contain files and subdirectories.

Some files within this directory structure have the extension .eledia and are either empty or contain text, with
lines in the format <ID>: <Text>

A file with the ending .eledia could have the following content:

123: Hello!
1477: run
4: The weather should be good tomorrow.

Each ID appears a maximum of once in a file. If the ID does not exist in a file, that file is skipped.


## 2. Task
A function eledia_text(id: int, dir: str) ÿ str should be written, which receives an ID and a directory path as input.
All files within the directory path with the ending .eledia should be found and the text associated with the input ID should
be read out. The read texts are then appended together with a space between them, in the order in which they appear
in the directory levels. If there are several .eledia files in a directory level , the order is alphabetical.

Example: 

![Example](docs/images/example-pic.jpeg)

## 3. Delivery

A Python module eledia.py that contains the eledia_text function . The module can contain additional (auxiliary)
functions, variables, etc.


## 4. Solution

Solution can be designed in 3 steps/functions

## 4.1 Approach

1. First Get all the Paths from the input (dir: str). this function can retrieve list of all paths recursively from folder to all child folders/files where file path ends with `.eledia`

    ```python
    def get_all_file_paths(dir: str, ext: str=None) -> list(str):
        """Get all absolute file path where extension path matches with input `ext`
        """
        pass
    ```

2. From the files list , generate ordered_tree_files from the input basically structure should contain 
    ```python 
    files_tree = {
        0: ['/dev/a/x.eledia',]
        1: ['/dev/a/b/x.eledia', '/dev/a/c/x.eledia']
    }

    def generate_files_tree(files: list(str)) -> dict
        pass


    ```

3. From the above the `files_tree` generate final output


## 4.2 Test Files

Placed all files in directory data_files

## 4.3 How to run
```
python main.py

or

pipenv run python main.py

```

## 4.4 How to Run Test

```
pytest
```
## Remark
- Used  os.getcwd() for easier testing

## 5. CI/CD (Continues Integration Testing)
- Configured CI/CD via github Action for unit pytest On every PR to main branch
