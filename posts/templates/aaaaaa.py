# # test Arbitrary Keyword Arguments
# def function1(*number ,**name):
#     print(number)
#     print(name)

# function1(1,2,3,4,ddd="ddd", h = "hadasd")
# def hash_list():
#     from collections import defaultdict
#     default_dict = defaultdict(int)

#     dict_a = dict()
#     dict_a["apple"] = 1
#     # dict_a["banana"] +=1
#     print(dict_a)

#     default_dict["apple"] = 1
#     default_dict["banana"]+=1
#     print(default_dict)
# hash_list()

# from collections import Counter
# s1 = 'abcdefga'
# s2 = 'bcdefgb'
# def hash_list2():
#     c1 = Counter(s1)
#     c2 = Counter(s2)
#     print(c1)
#     print(c2)
# hash_list2()
a = [1,2,3]
b = [2,3,4]
print(a & b)