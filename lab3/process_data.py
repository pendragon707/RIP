import json
import sys
import re
import random
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.print_result import print_result
from lab_python_fp.unique import Unique

path = '/Users/nonpenguin/my/pythonchic/rip/my_labs/lab3/data_light.json'

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(Unique([one_dict["job-name"] for one_dict in data], ignore_case=True)))

@print_result
def f2(arg):
    r = re.compile("программист*")
    return list(filter(r.match, arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    salary = []
    for i in range(len(arg)):
        salary.append(random.randint(100000, 200000))
    return list(zip(arg, salary))


if __name__ == '__main__':
    with cm_timer_1():
       f4(f3(f2(f1(data))))
