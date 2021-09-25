queue = []

def add_queue(song):
    queue.append(song)

def remove_queue():
    queue.pop(0)

def get_player(index):
    return queue[index]

def get_list():
    return queue

def skip():
    queue.pop(0)

def list_size():
    return len(queue)

def modify(index, value):
    queue[index] = value