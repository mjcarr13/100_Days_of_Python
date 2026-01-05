import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#so, a simple random name generator. HOw might we do this?
#we have a list of length... in this case 5, with index values from 0-4.
#we could have the random number generator pick a number from 0-4 inclusive
#then, having done so, print friend[num]

num = random.randint(0, len(friends)-1)
print(friends[num])


print(random.choice(friends))

