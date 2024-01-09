from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def parse_input(input_data):
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    return (item_count, capacity, items)

def _optimistic_estimate(index, capacity, items_sorted_value_density):
    weight = 0
    optimistic_est = 0
    for i in range(len(items_sorted_value_density)):
        cur_w = items_sorted_value_density[i].weight
        cur_v = items_sorted_value_density[i].value

        if weight + cur_w <= capacity:
            weight += cur_w
            optimistic_est += cur_v
        else:
            frac = (capacity - weight) / cur_w
            weight += frac * cur_w
            optimistic_est += frac * cur_v
            break
    return optimistic_est

def search(item_count, capacity, items):
    optimal = 1
    value = 0
    taken = [0]*item_count
    items_sorted_value_density = items.s
    base_estimate = _optimistic_estimate(0, capacity=capacity, items_sorted_value_density= co)


def solve_it(input_data):
    item_count, capacity, items = parse_input(input_data=input_data)
    value, optimal, taken = search(item_count, capacity, items)
    output_data = str(value) + ' ' + str(optimal) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

