import unittest
from main import get_all_file_paths,generate_eledia_files_tree,find_id_in_file,generate_final_output
import os
import pathlib



def test_eledia_file_paths():
    x = get_all_file_paths(os.getcwd() + '/data_files/suite1', "eledia")
    assert len(x)==5

def test_generate_eledia_files_tree():
    y=get_all_file_paths(os.getcwd() + '/data_files/suite2', "eledia")
    x=generate_eledia_files_tree(os.getcwd() +'/data_files/suite2',y)
    test_data={1: [os.getcwd()+'/data_files/suite2/a.eledia'],
               2: [os.getcwd()+'/data_files/suite2/task1/c.eledia',
                   os.getcwd()+'/data_files/suite2/task1/f.eledia',
                   os.getcwd()+'/data_files/suite2/task1/m.eledia',
                  ],
               4: [os.getcwd()+'/data_files/suite2/task1/task2/task3/b.eledia']}
    assert x==test_data

def test_find_id_in_file():
    file=os.getcwd()+'/data_files/suite3/task1/m.eledia'
    n=find_id_in_file(143,file)
    test_text='Aller Anfang ist schwer'
    assert n==test_text



def test_generate_final_output():
    test_data={1: [os.getcwd()+'/data_files/suite3/a.eledia'],
               2: [os.getcwd()+'/data_files/suite3/task1/c.eledia',
                   os.getcwd()+'/data_files/suite3/task1/f.eledia',
                   os.getcwd()+'/data_files/suite3/task1/m.eledia'],
               4: [os.getcwd()+'/data_files/suite3/task1/task2/task3/b.eledia']}
    test_array_data=['ich bin kellner', 'Krankenhaus', 'Des Teufels liebstes Möbelstück ist die lange Bank.', 'KalEL']
    x=generate_final_output(11, test_data)
    assert x==test_array_data
