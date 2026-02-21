#1 
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#apple
#banana
#cherry


#2
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#apple
#banana
#cherry


#3
mystr = "banana"

for x in mystr:
  print(x)

#b
#a
#n
#a
#n
#a


#4
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#1
#2
#3
#4
#5


#5
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#1
#2
#3
#4
#5


# Generators and Iterators in Python
# An iterator is an object that allows sequential access to elements.
# iter() creates an iterator from an iterable object.
# next() returns the next value and moves the iterator forward.
# A generator is a simpler way to create iterators using the yield keyword.
# yield returns a value and pauses the function until the next request.
# Generator expressions create generators using a short syntax.
