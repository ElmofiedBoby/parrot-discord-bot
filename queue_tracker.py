queue = []
lastplayed = "Nothing"
counter = 0


class b:

    def __init__(self):
        self.has_init = False
        self.play_status = False

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

    def inc_counter(self, num):
        self.counter = b.get_counter() + 1

    def dec_counter(self, num):
        self.counter = b.get_counter() - 1

    def get_counter():
        return counter

    def song_played(self, song):
        b.remove_queue()
        self.lastplayed = song.title

    def get_last_played():
        return lastplayed

    def get_play_status(self):
        return self.play_status

    def set_play_status(self, status):
        self.play_status = status

    def get_init_status(self):
        return self.has_init

    def change_init_status(self, changed):
        self.has_init = changed