import sys

def get_inputs():
    input_args = sys.argv[1:]

    selected_algorithm = input_args[0]
    vector_size = int(input_args[1])
    elements = [int(x) for x in input_args[2:vector_size + 2]]
    print_results = (input_args[-1:] == ["PRINT"])

    return selected_algorithm, elements, print_results
