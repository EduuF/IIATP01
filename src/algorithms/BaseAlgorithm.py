from abc import ABC, abstractmethod
from src.algorithms.heuristic.heuristic import *

class BaseAlgorithm(ABC):
    def __init__(self, elements):
        self.elements = elements
        self.print_results = False
        self.intermediate_steps = []
        self.expanded_states = 0
        self.cost = 0

    def set_print_results(self, print_results):
        self.print_results = print_results

    def is_ordered(self, current_node):
        for i in range(len(current_node) - 1):
            if current_node[i] > current_node[i + 1]:
                return False
        return True

    def swap_cost(self, i, j):
        if abs(i - j) == 1:
            return 2
        else:
            return 4

    def get_neighbors(self, current_node, cost_so_far):
        neighbor_list = []

        for i in range(len(current_node)):
            for j in range(i + 1, len(current_node)):
                """
                - O if a seguir garante que só haveram trocas quando o elemento da esquerda for maior que o direita
                - Isso diminui muito o tempo de execução do programa conforme a execução avança pois cada vez menos 
                elementos maiores estarão à esquerda de elementos menores (Não sugere uma troca que leva a um estado 
                pior que o atual)
                """
                if current_node[i] > current_node[j]:
                    next_node = list(current_node)
                    next_node[i], next_node[j] = next_node[j], next_node[i]
                    next_node = tuple(next_node)
                    new_cost = cost_so_far + self.swap_cost(i, j)
                    neighbor_list.append((next_node, new_cost))

        return neighbor_list

    def sort_elements(self):
        start = tuple(self.elements)
        if self.is_ordered(start):
            return start, 0
        self.cost, self.expanded_states = self.search_algorithm(start)

    def print_result(self):
        print(f"{self.cost} {self.expanded_states}")
        for expanded_state in self.intermediate_steps:
            print(" ".join([str(x) for x in expanded_state]))

    def heuristic(self, state):
        return heuristic(state)

    @abstractmethod
    def search_algorithm(self, start):
        pass

