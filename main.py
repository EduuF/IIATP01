from utils.get_inputs import *
from utils.algorithm_manager import *

if __name__ == '__main__':

    selected_algorithm, elements, print_results = get_inputs()

    try:
        alg_instance = algorithm_manager(selected_algorithm, elements)
    except ValueError as e:
        print(e)
        sys.exit(1)

    alg_instance.set_print_results(print_results)
    alg_instance.sort_elements()
    alg_instance.print_result()
