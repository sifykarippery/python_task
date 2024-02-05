#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main program to generate output of the eledia filter file problem statement
"""

import pathlib
import os


def get_all_file_paths(dir: str, ext: str):
    given_path = pathlib.Path(dir)
    files = list(given_path.rglob(f"*.{ext}"))
    list_paths = [file.as_uri().replace("file://", "") for file in files]
    return list_paths


def generate_eledia_files_tree(source_dir: str, eledia_file_paths: list):
    source_folder_index = len(source_dir.split("/"))
    tree_files = {}
    for file_path in eledia_file_paths:
        file_depth = len(file_path.split("/"))-source_folder_index
        if file_depth in tree_files:
            tree_files[file_depth].append(file_path)
            tree_files.update({file_depth: sorted(tree_files[file_depth])})
        else:
            tree_files.update({file_depth: [file_path]})
    return tree_files


def find_id_in_file(id: int, file_path: str):
    f = open(file_path, "r")
    file_lines = f.readlines()
    for line in file_lines:
        splits = line.split(": ")
        if splits[0].strip() == str(id):
            return splits[1].strip()
    return None


def generate_final_output(id: int, files_tree: dict):
    final_output = []
    for key in sorted(files_tree.keys()):
        files_list = files_tree[key]
        for file in sorted(files_list):
            find_result = find_id_in_file(id, file)
            if find_result is not None:
                final_output.append(find_result)

    return final_output


def eledia_text(id: int, dir: str):

    eledia_file_paths = get_all_file_paths(dir, "eledia")
    files_tree = generate_eledia_files_tree(dir, eledia_file_paths)
    eledia_output = generate_final_output(id, files_tree)
    if len(eledia_output) != 0:
        print(" ".join(eledia_output))



if __name__ == '__main__':
    eledia_text(100, os.getcwd()+"/data_files/suite1")
    eledia_text(1,  os.getcwd()+"/data_files/suite2/")
    eledia_text(1,  os.getcwd()+"/data_files/suite3/")
