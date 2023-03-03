import sys

from aois_sem4_lab1.src.utils import print_representation_table, print_task1, print_task2, print_task3, print_task4
from aois_sem4_lab1.src.binarylib import *


def main():
    try:
        x1 = int(sys.argv[1])
        x2 = int(sys.argv[2])
    except (IndexError, ValueError) as err:
        x1 = 11
        x2 = 21

    print_representation_table(x1,x2)
    print_task1(x1,x2)
    print_task2(x1,x2)
    print_task3(x1,x2)
    print_task4(1.25, 10.5)

    

if __name__ == "__main__":
    main()