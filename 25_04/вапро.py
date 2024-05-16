def length_without_hail(string):
    words = string.split()
    for word in words:
        if "град" in word:
            return -1
    return len(string)


string1 = input()
string2 = input()
string3 = input()

lengths = [length_without_hail(string1), length_without_hail(string2), length_without_hail(string3)]

max_length = max(lengths)
max_index = lengths.index(max_length)

print(max_length, end=" ")
print([string1, string2, string3][max_index])
