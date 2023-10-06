#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    ctr = 1
    print(
            "{} {}{}"
            .format(argc, "argument" if argc == 1
                    else "argumentsi", ':' if argc > 0 else '.')
        )
    if argc:
        for arg in argv:
            if arg != argv[0]:
                print("{}: {}".format(ctr, arg))
                ctr += 1
