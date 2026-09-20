
class FindMax:
    def find_max_in_lst(self, lst):
        max_value = lst[0]

        for x in range(len(lst)):
            if lst[x] > max_value:
                max_value = lst[x]

        return max_value
                

    # efficient / simple
    def find_max(self, num1, num2, num3):

        if num1 >= num2 and num1 >= num3:
            return num1

        elif num2 >= num1 and num2 >= num3:
            return num2

        else:
            return num3


    # nested if
    def find_max2(self, num1, num2, num3):

        if num1 >= num2:

            if num1 >= num3:
                return num1

            else:
                return num3

        else:

            if num2 >= num3:
                return num2

            else:
                return num3


find_max = FindMax()

print(find_max.find_max(1, 2, 3))

print(find_max.find_max2(1, 2, 3))