# we need to find the most frequent character in the string

# we get a string value as input

# make everything lowercase done
#take only alphabets from the string done
# store the number of times each alphabet appears in the string value done
# store alphabet in dictionary in front of the number of times it appears done
# print the dictionary in descending order of the number of times the alphabet appears done
# print it in a certain way

def frequency(inputstring):
    dict = {}
    inputstring=inputstring.lower()
    for i in inputstring:
        if i.isalpha():
             dict[i] = dict.get(i, 0) + 1
# Sort the letters based on their frequencies in descending order
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True) # sort the dictionary by value # x[1] means sort by value because value is at index 1
    # print it in a certain way
    for item in sorted_dict:
        i, freq = item  # unpack the tuple
        print(f"{i} = {freq:02d}", end=" ") # 02d means 2 digits, pad with 0 if necessary

# Prompt the user for input
x=str(input("Enter the string: "))
frequency(x)