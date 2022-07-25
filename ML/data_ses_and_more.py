import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# average speed is equal to mean
print(sum(speed) / len(speed))
x = numpy.mean(speed)
print(x)

# found median value result is different in odd len
print(speed[len(speed) // 2])
x = numpy.median(speed)
print(x)

# mode
