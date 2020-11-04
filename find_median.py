# Name: Jamar Hill
# Date: 11/2/2020
# Description: Assignment 6.a




def find_median(list):
    """sorting organizes the numbers in the list"""
    list.sort()
    """len feature find the gives each value in a list a position"""
    x = len(list)
    """solving for an even amount of items in a list"""
    if(len(list) %2 == 0):
        """An even list amount is going to offer two vaue positions is the median. """
        """The formula below thake the higher value and lower value of the median and divides the by two."""
        return (list[x // 2] + list[x // 2 - 1]) / 2
    else:
        """Solving for an odd amount of items in a list"""
        return list[x // 2]



print(find_median([13, 7, -3, 82, 4]))
print(find_median([6, 9, 5, 1, 3]))
print(find_median([100, 15, 1, 576]))
