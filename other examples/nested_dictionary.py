big_dictionary = {}

for k in range(5):
    big_dictionary[k] = dict(f1="h1", f2="h2", f3="h3")

print(big_dictionary.keys())
print(big_dictionary)
print('\n')
print(big_dictionary[0])
print(big_dictionary[0].keys())