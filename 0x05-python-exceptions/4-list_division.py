#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ divides element by element 2 lists """
    new_list = []
    for x in range(list_length):
        a = 0
        try:
            a = my_list_1[x] / my_list_2[x]
        except IndexError:

            print("{:s}".format("out of range"))
        except TypeError:
            print("{:s}".format("wrong type"))

        except ZeroDivisionError:

            print("{:s}".format("division by 0"))
        finally:
            new_list.append(a)
    return new_list
