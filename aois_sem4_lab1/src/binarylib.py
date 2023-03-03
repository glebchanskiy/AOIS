from typing import List

BINARY_DIGITS = 16
FLOAT_INDEX_DIGITS = 8
FLOAT_MANTISSA_DIGITS = 23


class Float:
    sign = 0
    index = []
    mantissa = []


def to_string(binary: List[int] | Float) -> str:
    if type(binary) == Float:
        return f"{binary.sign}|{binary.index}|{binary.mantissa}"
    elif type(binary) == list:
        return ''.join(str(bit) for bit in binary)
    else:
        return 'error type'


def to_direct(number: int, size: int) -> List[int]:
    binary = list()
    buf: int = 0
    num: int = abs(number)

    while num:
        buf = num % 2
        binary.append(buf)
        num //= 2

    for i in range(0, size - len(binary)):
        binary.append(0)

    binary.reverse()

    if number < 0:
        binary[0] = 1
    return binary


def to_reverse(number: int, size: int) -> List[int]:
    binary = to_direct(number, size)

    if binary[0] == 0:
        return binary
    else:
        for i in range(1, len(binary)):
            if binary[i] == 1:
                binary[i] = 0
            else:
                binary[i] = 1
        return binary


def from_direct_to_reverse(binary: List[int]) -> List[int]:
    if binary[0] == 0:
        return binary
    else:
        for i in range(1, len(binary)):
            if binary[i] == 1:
                binary[i] = 0
            else:
                binary[i] = 1
        return binary


def to_additional(number: int, size: int) -> List[int]:
    binary = to_reverse(number, size)
    binary_one = [0] * BINARY_DIGITS
    binary_one[len(binary_one)-1] = 1

    if binary[0] == 0:
        return binary
    else:
        binary = addition(binary, binary_one)

        return binary


def from_direct_to_additional(binary: List[int]) -> List[int]:
    binary = from_direct_to_reverse(binary)
    binary_one = [0] * BINARY_DIGITS
    binary_one[len(binary_one)-1] = 1

    if binary[0] == 0:
        return binary
    else:
        binary = addition(binary, binary_one)
        return binary

        # -------


def addition(a: List[int], b: List[int]) -> List[int]:
    result: List[int] = []
    trans: bool = False

    for i in range(len(a)-1, -1, -1):
        if a[i] == 0 and b[i] == 0 and not trans:
            result.append(0)
            trans = False
        elif a[i] == 0 and b[i] == 0 and trans:
            result.append(1)
            trans = False
        elif a[i] == 1 and b[i] == 0 and not trans:
            result.append(1)
            trans = False
        elif a[i] == 1 and b[i] == 0 and trans:
            result.append(0)
            trans = True
        elif a[i] == 0 and b[i] == 1 and not trans:
            result.append(1)
            trans = False
        elif a[i] == 0 and b[i] == 1 and trans:
            result.append(0)
            trans = True
        elif a[i] == 1 and b[i] == 1 and not trans:
            result.append(0)
            trans = True
        elif a[i] == 1 and b[i] == 1 and trans:
            result.append(1)
            trans = True

    result.reverse()
    return result


def multiplication(a: List[int], b: List[int]) -> List[int]:
    binary_result = [0]*BINARY_DIGITS
    binary_one = [1]*BINARY_DIGITS
    binary_zero = [0]*BINARY_DIGITS

    sign: int = 0 if a[0] == b[0] else 1

    while b != binary_zero:
        binary_result = addition(binary_result, a)
        b = addition(b, binary_one)

    binary_result[0] = sign
    return binary_result


def division(a, b):
    binary_result = [0]*BINARY_DIGITS
    binary_zero = [0]*BINARY_DIGITS

    binary_one = [0]*BINARY_DIGITS
    binary_one[BINARY_DIGITS-1] = 1

    sign: int = 0 if a[0] == b[0] else 1

    a[0] = 0
    b[0] = 1

    b = from_direct_to_additional(b)

    while a[0] != 1 and a != binary_zero:
        a = addition(a, b)
        if a[0] == 1 or a == binary_zero:
            break
        binary_result = addition(binary_result, binary_one)

    binary_result[0] = sign

    return from_direct_to_additional(binary_result)


def to_float(number: float) -> Float:
    binary_float = Float()
    number_as_string = str(number)

    if number < 0:
        binary_float.sign = 1
        number = -number

    index = 0
    for i in range(len(number_as_string)-1, -1, -1):
        if number_as_string[i] == '.':
            break
        else:
            index += 1

    number *= pow(10, index)
    number = int(number)
    binary_float.index = to_direct(index, FLOAT_INDEX_DIGITS)
    binary_float.mantissa = to_direct(number, FLOAT_MANTISSA_DIGITS)

    return binary_float


def less(first: List[int], second: List[int]) -> bool:
    for i in range(0, len(first)-1):
        if first[i] == 1 and second[i] == 0:
            return False
        elif first[i] == 0 and second[i] == 1:
            return True
    return True

def stabilisation(a: Float, b: Float, old_index):
   
    binary_one = [0]*FLOAT_INDEX_DIGITS
    binary_one[len(binary_one)-1] = 1
    while a.index != b.index:
        a.index = addition(a.index.copy(), binary_one.copy())
        

    d_mantissa = direct_to_decimal(a.mantissa.copy())
    d_mantissa *= pow(10, (direct_to_decimal(a.index.copy())  - direct_to_decimal(old_index) ))
    a.mantissa = to_direct(d_mantissa, FLOAT_MANTISSA_DIGITS)
    return a


def float_addition(a: Float, b: Float) -> Float:
    binary_float = Float()

    # только положительные флоты
    if a.sign == 1 and b.sign == 1:
        binary_float.sign = 1
        a.mantissa[0] = 1
        b.mantissa[0] = 1
    elif a.sign == 1:
        a.mantissa[0] = 1
    elif b.sign == 1:
        b.mantissa[0] = 1

    if less(a.index, b.index):
        a = stabilisation(a, b, a.index.copy())
    else:
        b = stabilisation(b, a, b.index.copy())

    binary_float.index = addition(a.index, b.index)  
    binary_float.mantissa = addition(a.mantissa.copy(), b.mantissa.copy())

    return binary_float


def float_to_decimal(binary: Float):
    return direct_to_decimal(binary.mantissa) * pow(10, -direct_to_decimal(binary.index) // 2)


def direct_to_decimal(binary: List[int]):
    number = 0
    binary.reverse()
    for i in range(0, len(binary)-1):
        if binary[i] == 1:
            number += pow(2, i)

    if binary[len(binary) - 1] == 1:
        return -number
    else:
        return number
