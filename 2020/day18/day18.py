#!/usr/bin/env python
from sys import argv as sysArgv


def calc_total_1st(plain_op):
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


def calc_total_2nd(plain_op):
    # Accumulator of the sums
    res_sum = int(plain_op[0])
    # Iterator of the rest of the list
    it = iter(plain_op[1:])
    # List with only results of sums and prod signs
    plain_prods_op = []
    try:
        for op in it:
            if op == '*':
                # If the next op is prod, save the sum
                # (sum can be a result of adding number
                # or a single number (e.g. 1 * 3 -> res_sum = 1))
                plain_prods_op.append(res_sum)
                # Append the prod sign
                plain_prods_op.append(op)
                # Read the next number as the sum
                res_sum = int(next(it))
            else:
                # If there's a sum, do it
                res_sum += int(next(it))
    except StopIteration:
        pass
    # Add the last number
    plain_prods_op.append(res_sum)
    # Find the product of all the number
    # (reusing code, since with this input, only the product
    # branch will be used)
    return calc_total_1st(plain_prods_op)


def calc_total(plain_op, star):
    if star == 1:
        return calc_total_1st(plain_op)
    else:
        return calc_total_2nd(plain_op)

def perform_maths(op, ptr, star):
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
            par_res, ptr = perform_maths(op, ptr+1, star)
            plain_op.append(par_res)
        elif n == ')':
            # Return result of the parenthesis and the last index
            # Returns ptr too to mark the end of the parenthesis
            return calc_total(plain_op, star), ptr
        else:
            # Add value/operator to the "calculator"
            plain_op.append(n if n in ['+', '*'] else int(n))
        ptr += 1
    # Return result of line
    # (only used outside parenthesis, no need to return ptr)
    return calc_total(plain_op, star)


def loop(operations, star):
    res = 0
    for line in operations:
        res += perform_maths(line, 0, star)
    return res


def main():
    operations = open(sysArgv[1], 'r').read().replace(' ', '').strip().split('\n')
    print("1st STAR SOLUTION ->", loop(operations, 1))
    print("2nd STAR SOLUTION ->", loop(operations, 2))


if __name__ == "__main__":
    main()
