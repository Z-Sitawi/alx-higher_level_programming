#!/usr/bin/python3
def find_peak(list_of_integers):
    """
        Finds a peak in a list of unsorted integers.

    :param list_of_integers: list of unsorted integers
    :return: The peak found / list of the peaks / None if no peak found.
    """
    lint = list_of_integers
    length = len(lint)
    if length == 0:
        return None

    if length == 1:
        return lint[0]

    peaks = []
    if length == 2:
        if lint[0] > lint[1]:
            peaks.append(lint[0])
        else:
            peaks.append(lint[1])
    else:
        if lint[0] > lint[1]:
            peaks.append(lint[0])
        if lint[-1] > lint[-2]:
            peaks.append(lint[-1])

        for n in range(1, length - 1):
            if lint[n-1] <= lint[n] >= lint[n+1]:
                peaks.append(lint[n])
    return find_peak(peaks)
