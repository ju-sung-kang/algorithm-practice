import sys


def heapadd(heap, x):  # max 힙에 x 추가
    heap.append(x)
    cur = len(heap) - 1
    while cur > 1:
        if heap[cur // 2] < heap[cur]:
            tmp = heap[cur // 2]
            heap[cur // 2] = heap[cur]
            heap[cur] = tmp
            cur = cur // 2
        else:
            break


def heappop(heap):  # max 힙에서 추출
    max_val = heap[1]
    heap[1] = heap[-1]
    heap.pop()
    cur = 1
    heapsize = len(heap) - 1
    while True:
        biggest = cur
        if 2 * cur <= heapsize:
            if heap[biggest] < heap[2 * cur]:
                biggest = 2 * cur

        if 2 * cur + 1 <= heapsize:
            if heap[biggest] < heap[2 * cur + 1]:
                biggest = 2 * cur + 1

        tmp = heap[cur]
        heap[cur] = heap[biggest]
        heap[biggest] = tmp
        if cur != biggest:
            cur = biggest
        else:
            break

    return max_val


n = int(sys.stdin.readline())
maxheap = [0]
minheap = [0]

heapadd(maxheap, int(sys.stdin.readline()))
sys.stdout.write(str(maxheap[1]) + '\n')
for i in range(n-1):
    x = int(sys.stdin.readline())
    if x > maxheap[1]:
        heapadd(minheap, (-1) * x)
        if len(minheap) > len(maxheap):
            heapadd(maxheap, (-1) * heappop(minheap))
    else:
        heapadd(maxheap, x)
        if len(maxheap) - len(minheap) >= 2:
            heapadd(minheap, (-1) * heappop(maxheap))

    sys.stdout.write(str(maxheap[1]) + '\n')