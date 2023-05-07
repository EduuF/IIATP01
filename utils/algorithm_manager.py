from src.algorithms.BFS import *
from src.algorithms.IDS import *
from src.algorithms.UCS import *
from src.algorithms.GBFS import *
from src.algorithms.AStar import *

def algorithm_manager(algorithm, elements):
    if algorithm == 'B':
        bfs_instance = BFS(elements)
        return bfs_instance

    if algorithm == 'I':
        ids_instance = IDS(elements)
        return ids_instance

    if algorithm == 'U':
        ucs_instance = UCS(elements)
        return ucs_instance

    if algorithm == 'A':
        a_star_instance = AStar(elements)
        return a_star_instance

    if algorithm == 'G':
        gbfs_instance = GBFS(elements)
        return gbfs_instance
