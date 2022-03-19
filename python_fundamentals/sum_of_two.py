import common as c


def solution(num_list, target):
    num_dict = {}
    ret_list = []

    for i, n in enumerate(num_list):
        if ((target - n) in num_dict.keys()):
            ret_list.append((i, num_dict[target - n]))
        else:
            num_dict[n] = i

    return ret_list


def execute_me():
    c.print_module_name()
    num_list = [2, 6, 1, 9, 5, 7, 0]
    target = 9

    res_list = solution(num_list, target)

    print(res_list)
