#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    print(sys.argv)
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    args = sys.argv[1:]
    if args[1] not in ('+', '-', '/', '*'):
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    a = int(args[0])
    b = int(args[2])
    res = "{:d} {:s} {:d} = {}"
    match args[1]:
        case '+':
            print(res.format(a, args[1], b, add(a, b)))
        case '-':
            print(res.format(a, args[1], b, sub(a, b)))
        case '/':
            print(res.format(a, args[1], b, div(a, b)))
        case '*':
            print(res.format(a, args[1], b, mul(a, b)))
