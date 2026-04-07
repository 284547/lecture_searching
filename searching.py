import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field != "unordered_numbers":
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as json_file:
        seq = json.load(json_file)
    return seq[field]

def linear_search(sekvence, number):
    positions = []
    for i in range(len(sekvence)):
        if sekvence[i] == number:
            positions.append(i)

    return {
        "position": positions,
        "count": len(positions)
    }

def binary_search(order_sequence, number):
    left = 0
    right = len(order_sequence) -1

    while left <= right:
        mid = (left + right) // 2
        if order_sequence[mid] == number:
            return mid
        elif order_sequence[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return None




def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    vysledek = linear_search(sequential_data, 33)
    print(vysledek)
    ordered_data = binary_search(sequential_data, 22)
    print (ordered_data)




if __name__ == '__main__':
    main()