def enqueue(n):
    global rear
    rear += 1
    q[rear] = n


q = [0] * 10
front = -1
rear = -1

rear += 1  # enqueue
q[rear] = 1

enqueue(2)
enqueue(3)

while front != rear:  # 큐가 비어있지 않으면
    front += 1
    print(q[front])

queue = []
queue.append(1)
queue.append(2)
queue.append(3)

while len(queue) > 0:
    print(queue.pop(0))  # dequeue : queue.pop(0)

print(queue)