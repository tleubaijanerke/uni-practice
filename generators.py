#1 
def square_generator(n):
    for i in range(n + 1):
        yield i * i

# Test
for value in square_generator(5):
    print(value)

#This generator yields the square of numbers from 0 to n.
#yield returns values one by one instead of storing them in memory.
#Output: 0 1 4 9 16 25


#2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))

print(",".join(str(num) for num in even_numbers(n)))

#This generator yields even numbers between 0 and n.
#Numbers are converted to string and printed comma-separated.
#Output example (n=10): 0,2,4,6,8,10


#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Test
for num in divisible_by_3_and_4(50):
    print(num)

#This generator yields numbers divisible by both 3 and 4 between 0 and n.
#Condition: i % 3 == 0 and i % 4 == 0.
#Output example: 0, 12, 24, 36, 48


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Test
for value in squares(3, 7):
    print(value)
  
#This generator yields squares of numbers from a to b inclusive.
#Values are produced one at a time using yield.
#Output: 9 16 25 36 49


#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Test
for num in countdown(5):
    print(num)

#This generator yields numbers from n down to 0.
#Each iteration decreases n by 1.
#Output: 5 4 3 2 1


# Generators and Iterators in Python
# An iterator is an object that allows sequential access to elements.
# iter() creates an iterator from an iterable object.
# next() returns the next value and moves the iterator forward.
# A generator is a simpler way to create iterators using the yield keyword.
# yield returns a value and pauses the function until the next request.
# Generator expressions create generators using a short syntax.
