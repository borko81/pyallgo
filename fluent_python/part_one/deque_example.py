from collections import deque

dq = deque(range(10), maxlen=10)

print(dq)

dq.rotate()

print(dq)

dq.appendleft(100)
dq.extend([11, 22, 33])
dq.append(101)
print(dq[-1])

