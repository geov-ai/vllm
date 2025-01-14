# from .communication_op import *
# from .parallel_state import *
# from .utils import *

def divide(a, b):
    assert b == 1
    return a

def get_tensor_model_parallel_rank():
    return 0

def get_tensor_model_parallel_world_size():
    return 1

def split_tensor_along_last_dim(x):
    return [x]


def tensor_model_parallel_all_gather(x):
    return x

def tensor_model_parallel_all_reduce(x):
    return x