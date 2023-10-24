#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []

    for i in range(list_length):
        try:
            res.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
            continue
        except TypeError:
            print("wrong type")
            res.append(0)
            continue
        except IndexError:
            res.append(0)
            print("out of range")
            continue
        finally:
            pass
    return res
