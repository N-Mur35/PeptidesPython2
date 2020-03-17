# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print
    ele
print
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print
    count, ele

    # always read for loops right to left so for l1 take each ele and print it.
    # enumerate is a built in python function which adds a counter to an iterable and returns it in an enumerate object This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.