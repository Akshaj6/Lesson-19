test_dict = {'Codingal' : 2, 'is' : 2, 'the' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}
print("The original dictionary was " + str(test_dict))
K = 2
result = 0
for key in test_dict:
    if test_dict[key] == K:
        result = result + 1
print(result)