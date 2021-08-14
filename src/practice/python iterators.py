def reverse_string_generator(string):
    for i in range(len(string) - 1, -1, -1):
        yield string[i]


def all_even(x):
    n = 0
    while True:
        if n <= x:
            yield n
            n = n + 2
        else:
            break




def generator():
    """ A simple generator"""
    n = 1
    print("This is the first run")
    yield n

    n += 1
    print("This is the second run")
    yield n

    n += 1
    print("This is the third run")
    yield n


# class PowTwo:
#
#     def __init__(self, max=0):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#

if __name__ == "__main__":
    # object_of_powtwo = PowTwo(4)
    # iterator = iter(object_of_powtwo)
    #
    # while True:
    #     try:
    #         print(next(object_of_powtwo))
    #     except StopIteration:
    #         break

    # for i in object_of_powtwo:
    #     print(i)

    # for item in generator():
    #     print(item)
    #
    # for char in reverse_string_generator("Hello"):
    #     print(char, end='')
    #
    #
    # def fibonnacci_nums(num):
    #     x = 0
    #     y = 1
    #     for _ in range(num):
    #         x, y = y, x + y
    #         yield x
    #
    #
    # def square(nums):
    #     for num in nums:
    #         yield num ** 2
    #
    #
    # print(f'\n{sum(square(fibonnacci_nums(10)))}')
    #
    # list_ = [1, 2, 3, 4, 5, 6]
    # target = 3
    # iterable = (target - x for x in list_)
    #
    # count = 0
    # for x, y in enumerate(list_):
    #     if y in iterable:
    #         print(x, iterable[count])
    #         break
    #     else:
    #         count += 1
    for i in all_even(50):
        print(i)
