#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    if len(argv) == 4:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]

        if operator == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif len(operator) > 2:
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif operator == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
