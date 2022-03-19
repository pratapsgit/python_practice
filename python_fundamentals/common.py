import sys


def print_module_name():
    # print(sys.modules[__name__])
    caller = sys._getframe(1)
    print("=========", caller.f_globals['__name__'], "=========")
