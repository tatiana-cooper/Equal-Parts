from string import digits


def equal_part(numbers, new_list, sum_numbers, r=1):
    """
    The program creates two new lists from given list,
    where the sum of elements in the first is equal to the sum in the second.

    The result achieves by recursively taking the element with the index starting from 1 (after +1)
    and by enumeration of elements' sum. As soon as the sum of elements in first list
    becomes bigger than sum of the second list — delete last added element.


    (list, list, int) -> (list, str, list, str)
    :param sum_numbers: sum of elements in 'numbers'
    :param numbers: given list
    :param new_list: a new list with the given list's max int
    :param r: index of element in given list (default - 1), to start processing from
    :return: two lists with equal sums and their sums
    """

    # Ignore the elements before index r
    for index, item in enumerate(numbers[r:]):
        # A new list, in which program appends a possible numbers from the given list,
        # sum of elements in it must be equal to the half of given list
        new_list.append(item)

        # If the given list's and a new list's sums are equal
        if sum(new_list) == sum_numbers / 2:

            # From given list removes numbers which are in a new list
            [numbers.remove(value) for value in new_list if value in new_list]

            return new_list, f'Sum of the first list: {sum(new_list)}', \
                numbers, f'Sum of the second list: {sum(numbers)}'

        # If half the sum of new_list is exceeded and 'item' is not the last given list's number:
        # removes 'item' from a new_list
        elif sum(new_list) > sum_numbers / 2 and index != numbers.index(numbers[-1]):
            new_list.remove(item)

        # If half the sum of new_list is exceeded and 'item' is the last given list's number:
        # removes number (in index r) from new_list and calls recursion with index r + 1, because
        # all the sum's combinations with this number in index r are not suitable for condition
        elif sum(new_list) > sum_numbers / 2 and index == numbers.index(numbers[-1]):
            new_list.remove(numbers[r])
            return equal_part(numbers, new_list, sum_numbers, r + 1)


def launch_equal_part(numbers):
    """
    Function checks if data is valid, and if valid — launches the equal_part function.
    :param numbers: given list of numbers
    :return: str if data is not valid, if data is valid — calls the equal_part function.
    If the first element is equal to the sum of a half list — returns resulting lists.
    """

    sum_numbers = sum(numbers)

    # Sorting from highest to lowest
    numbers = sorted(numbers, reverse=True)
    if sum_numbers % 2 == 0:

        # Case in which the first element is equal to the sum of a list's half
        if numbers[0] == sum(numbers) / 2:
            return [numbers[0]], f'Sum of the first list: {numbers[0]}', \
                   numbers[1:], f'Sum of the second list: {numbers[0]}'

        else:
            # Launches the main function
            return equal_part(numbers, [numbers[0]], sum_numbers)

    else:
        return "This list's numbers couldn't be divided into two equal sums."


if __name__ == '__main__':
    # [7, 6, 5, 4, 2, 2, 2]
    while True:
        user_numbers = input('Enter a list of number divided by space: ').split()
        if all(i in digits for i in user_numbers):
            user_numbers = list(map(int, user_numbers))
            print(user_numbers)
            break

    print(launch_equal_part(user_numbers))
