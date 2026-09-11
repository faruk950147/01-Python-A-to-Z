class RemoveDuplicates:

    def remove_duplicates(self, lst):
        return list(set(lst))


    def remove_duplicates1(self, lst):
        return list(dict.fromkeys(lst))


    def remove_duplicates2(self, lst):
        result = []

        for i in lst:
            if i not in result:
                result.append(i)

        return result


    def remove_duplicates3(self, lst):
        result = []

        for i in lst:
            if lst.count(i) >= 1 and i not in result:
                result.append(i)

        return result


duplicates = RemoveDuplicates()

print(duplicates.remove_duplicates(
    [1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
))

print(duplicates.remove_duplicates1(
    [1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
))

print(duplicates.remove_duplicates2(
    [1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
))

print(duplicates.remove_duplicates3(
    [1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
))