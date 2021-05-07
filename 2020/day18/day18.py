#!/usr/bin/env python
from sys import argv as sysArgv


def calc_total(plain_op):
    # Get first value
    res = int(plain_op[0])
    # Iterator to extract two elements at a time
    # ([1:] => the first is manual, the rest is operator
    # and number, in that order)
    it = iter(plain_op[1:])
    try:
        # Loop trough line
        for op in it:
            # Get number
            next_num = next(it)
            if (op == '+'):
                res += int(next_num)
            else:
                res *= int(next_num)
    except StopIteration:
        pass
    return res


def perform_maths(op, ptr):
    len_op = len(op)
    # "Calculator" like list
    # (used both inside and outside parenthesis)
    plain_op = []
    # Operational loop of line/parenthesis
    while ptr < len_op:
        n = op[ptr]
        if n == '(':
            # Calculate result of parenthesis
            # Returns ptr too to mark the end of the parenthesis
            par_res, ptr = perform_maths(op, ptr+1)
            plain_op.append(par_res)
        elif n == ')':
            # Return result of the parenthesis and the last index
            # Returns ptr too to mark the end of the parenthesis
            return calc_total(plain_op), ptr
        else:
            # Add value/operator to the "calculator"
            plain_op.append(n if n in ['+', '*'] else int(n))
        ptr += 1
    # Return result of line
    # (only used outside parenthesis, no need to return ptr)
    return calc_total(plain_op)


def loop(operations):
    res = 0
    for line in operations:
        res += perform_maths(line, 0)
    return res


def main():
    operations = open(sysArgv[1], 'r').read().replace(' ', '').strip().split('\n')
    print("1st STAR SOLUTION ->", loop(operations))


if __name__ == "__main__":
    main()
