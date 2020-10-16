import time

class cm_timer_1:
    def __init__(self):
        self.start = time.monotonic()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print('time: {}'.format(time.monotonic() - self.start))

class cm_timer_2:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

