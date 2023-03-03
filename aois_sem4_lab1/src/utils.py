from typing import List, Tuple

from tabulate import tabulate


from aois_sem4_lab1.src.binarylib import *


def _get_all_representations_of(number: int) -> Tuple[str, str, str, int]:
    return (
        to_string(to_direct(number, BINARY_DIGITS)),
        to_string(to_reverse(number, BINARY_DIGITS)),
        to_string(to_additional(number, BINARY_DIGITS)),
        number
    )


def print_representation_table(a: int, b: int) -> None:
    print('\nTASK 1 representation of numbers in bits')
    output: List[Tuple] = []

    output.append(_get_all_representations_of(a))
    output.append(_get_all_representations_of(-a))
    output.append(_get_all_representations_of(b))
    output.append(_get_all_representations_of(-b))

    print(tabulate(output, headers=[
          'direct', 'reverse', 'addition', 'decimal'], tablefmt='simple_grid'))


def print_task1(a: int, b: int) -> None:
    print('\nTASK 1 (sum)')
    print_sum_of(a, b)
    print_sum_of(-a, b)
    print_sum_of(a, -b)
    print_sum_of(-a, -b)


def print_task2(a: int, b: int) -> None:
    print('\nTASK 2 (mult)')
    print_mult_of(a, b)
    print_mult_of(-a, b)
    print_mult_of(a, -b)
    print_mult_of(-a, -b)


def print_task3(a: int, b: int) -> None:
    print('\nTASK 3 (div)')
    print_div_of(a, b)
    print_div_of(-a, b)
    print_div_of(a, -b)
    print_div_of(-a, -b)
    print_div_of(b, a)
    print_div_of(-b, a)
    print_div_of(b, -a)
    print_div_of(-b, -a)


def print_task4(a: float, b: float) -> None:
    print('\nTASK 4 (float sum)')
    print_float_sum_of(a, b)



def print_sum_of(a: int, b: int) -> None:
    bin_a: List[int] = None
    bin_b: List[int] = None

    bin_a = to_additional(a, BINARY_DIGITS)
    bin_b = to_additional(b, BINARY_DIGITS)

    print(tabulate([
        ('a: ', to_string(bin_a), a),
        ('b: ', to_string(bin_b), b),
        ('r: ', to_string(addition(bin_a, bin_b)), a+b)
    ], tablefmt='simple_grid'))


def print_mult_of(a: int, b: int) -> None:
    bin_a: List[int] = None
    bin_b: List[int] = None

    bin_a = to_direct(a, BINARY_DIGITS)
    bin_b = to_direct(b, BINARY_DIGITS)

    print(tabulate([
        ('a: ', to_string(bin_a), a),
        ('b: ', to_string(bin_b), b),
        ('r: ', to_string(multiplication(bin_a, bin_b)), direct_to_decimal(multiplication(bin_a, bin_b)))
    ], tablefmt='simple_grid'))


def print_div_of(a: int, b: int) -> None:
    bin_a: List[int] = None
    bin_b: List[int] = None

    bin_a = to_direct(a, BINARY_DIGITS)
    bin_b = to_direct(b, BINARY_DIGITS)

    print(tabulate([
        ('a: ', to_string(bin_a), a),
        ('b: ', to_string(bin_b), b),
        ('r: ', to_string(division(to_direct(a, BINARY_DIGITS), to_direct(b, BINARY_DIGITS))), int(a / b))
    ], tablefmt='simple_grid'))

def print_float_sum_of(a: float, b: float):
    bin_a = to_float(a)
    bin_b = to_float(b)
    # bin_float = 

    # print(to_string(to_float(a)))
    # print(to_string(to_float(b)))
    # print(to_string(float_addition(bin_a, bin_b)))
    # print(a, "+", b, "=", float_to_decimal(float_addition(bin_a, bin_b)))

    print(tabulate([
        ('a: ', a),
        ('b: ', b),
        ('r: ', float_to_decimal(float_addition(bin_a, bin_b)))
    ], tablefmt='simple_grid'))
