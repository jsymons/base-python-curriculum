def create_queue():
    return []


def enqueue(queue, element):
    queue.append(element)


def dequeue(queue):
    if not queue:
        return None

    return queue.pop(0)
