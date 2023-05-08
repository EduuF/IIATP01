from src.algorithms.BFS import *
from src.algorithms.IDS import *
from src.algorithms.UCS import *
from src.algorithms.GBFS import *
from src.algorithms.AStar import *

def algorithm_manager(algorithm, elements):
    algoritms = {
        'B': BFS,
        'I': IDS,
        'U': UCS,
        'A': AStar,
        'G': GBFS
    }

    if algorithm in algoritms:
        return algoritms[algorithm](elements)
    else:
        raise ValueError("Error: '{}' is not a valid algorithm.".format(algorithm))

