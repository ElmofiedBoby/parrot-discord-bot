queue = []
lastplayed = "Nothing"
counter = 0

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

def inc_counter(num):
    counter = get_counter() + 1

def dec_counter(num):
    counter = get_counter() - 1

def get_counter():
    return counter

def song_played(song):
    remove_queue()
    lastplayed = song.title

def get_last_played():
    return lastplayed