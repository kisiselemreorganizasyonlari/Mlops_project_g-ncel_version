import os
import sys

import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV



from box.exceptions import BoxValueError
from box.config_box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
import yaml
import json
import joblib
from typing import Any
import base64


def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'w') as file_obj:
            pickle.dump(obj,file_obj)


    except Exception as e:
        raise e
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise e
    
@ensure_annotations

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
          ValueError: if yaml file is empty
          e:empty file

    Returns:
        ConfigBox: config box object

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) 
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty") 
    except Exception as e:
        raise e  
    

@ensure_annotations

def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    
    Args:
        path_to_directories(list): list of path of directories
        ignore_log:(bool,optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"