def insertion_sort(to_sort):
    """
    Sort a list of numbers using the insertion sort algorithm
    Return a list of sorted numbers

    Keyword arguments:
    to_sort -- an unsorted python list of numbers
    """

    # This is the outer loop.
    for i in range(1, to_sort):
        j = i

        # This inner while loop.  Note the backwards iteration.
        # The while loop terminates when either:
        # 1. j == 0 i.e. the first element in the list is reached
        # 2. there is no need to do any sorting i.e. to_sort[j-1] < to_sort[j]
        while j > 0 and to_sort[j - 1] > to_sort[j]:
            # to swap the values we need a 3rd variables (temp)
            temp = to_sort[j]
            to_sort[j] = to_sort[j - 1]
            to_sort[j - 1] = temp
            j -= 1

    return to_sort


if __name__ == "__main__":
    list_to_sort = [14, 33, 27, 10, 35, 19, 42, 44]
    sorted_list = insertion_sort(list_to_sort)
    print(sorted_list)