def average_lists(list1, list2):
    """
    this function gets two lists of numbers and return number of average element of both lists
    :param list1: list of num
    :param list2: list of num
    :return: int of average element of both lists
    """
    new_list = list1 + list2
    sum = 0
    amount = 0
    average = 0
    for number in new_list:
        sum += number
        amount += 1
    average = sum / amount
    print("the average is " + str(average))

def main():
    list1 = [2, 3, 4, 8, 5, 13]
    list2 = [66, 8, 2, 9, 12]
    average_lists(list1, list2)
main()