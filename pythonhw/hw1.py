

def q1(mystring):
    """ split the string by tabs to get an array and return the array """
    return mystring.split("\t")


def q2(mystring):
    """ split the string by tabs to get an array and return the second element of the array """
    return mystring.split("\t")[1]

def q3(myarray):
    """ myarray is an list of pairs. this function should return the sum of the first
    items in the pair and the sum of the second items """
    myarray = [(1, 2), (3, 5), (10, 9)]
    p1 = []
    p2 = []
    for i in myarray:
        p1.append(i[0])
        p2.append(i[1])
    result = map(lambda n1, n2: n1 + n2, p1, p2)
    return result

def q4(mystringarray):
    """ return the position of the first occurrence of the string 'hi' or -1 if it is not found.
    you cannot change how the array is iterated and you cannot use any list operations on mystringarray"""
    input1 = int(input("Size of list: "))
    mystringarray = list(map(str,input().split(" ")))[:input1]
    dictionary = {}
    index = 0
    for mystring in mystringarray:
                if mystring not in dictionary:
            dictionary[mystring] = index
        index += 1
    key1 = str(input("Enter string to search: "))
    if key1 in dictionary:
        return dictionary[key1]
    else:
        return -1
      
def q5(myarray):
    """ return a dictionary containing the counts of items in the input array """
    dictionary = {}
    for i in myarray:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

