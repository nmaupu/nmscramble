#!/usr/bin/python -W ignore::DeprecationWarning
import sys
from threading import Thread
import time
from enum import Enum
from core.cube_utils import scramble, Timer
from core.input import getch

__author__ = 'nmaupu'

suffixes = {
    '333': ["", "2", "'"],
}

axis = {
    '333': [
        ['L', 'R'],
        ['U', 'D'],
        ['F', 'B'],
    ]
}


class Status(Enum):
    INSPECTION = 0
    RESOLVING = 1
    STOPPED = 2


cuber_status = Status.STOPPED

threads = []


def main():
    global cuber_status, threads
    while True:
        s = scramble(axis['333'], suffixes['333'], 21)
        print ' '.join(s)

        cuber_status = Status.STOPPED
        get_key()
        cuber_status = Status.RESOLVING
        t = Timer()
        t_resolve = ResolvingThread(t)
        threads.append(t_resolve)
        t_resolve.start()
        get_key()
        cuber_status = Status.STOPPED
        threads.pop().join()

        duration = t.get_duration()
        print("Duration : %d,%d second(s)" % (duration / 1000, duration % 1000))


class BasicThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.stopped = False

    def start(self):
        Thread.start(self)

    def stop(self):
        self.stopped = True

    def is_running(self):
        return Thread.is_alive(self) and not self.stopped


class ResolvingThread(BasicThread):
    def __init__(self, timer):
        BasicThread.__init__(self)
        self.timer = timer

    def run(self):
        global cuber_status
        while cuber_status is Status.RESOLVING and super(ResolvingThread, self).is_running():
            duration = self.timer.get_duration()
            sys.stdout.write('Duration : %.3f second(s)           \r' % (float(duration) / 1000))
            sys.stdout.flush()
            time.sleep(.1)


class CountdownThread(BasicThread):
    def __init__(self, milliseconds):
        BasicThread.__init__(self)
        self.timer = Timer()
        self.milliseconds = milliseconds

    def run(self):
        global cuber_status
        self.timer.tick()
        while self.timer.get_duration() < self.milliseconds \
                and super(CountdownThread, self).is_running() \
                and cuber_status is Status.INSPECTION:
            sys.stdout.write('Inspection : %d second(s)           \r' % int((self.milliseconds - self.timer.get_duration()) / 1000))
            sys.stdout.flush()
            time.sleep(0.1)


class GetkeyThread(BasicThread):
    def __init__(self):
        BasicThread.__init__(self)

    def run(self):
        get_key()


def get_key():
    global threads
    k = getch()
    if k == 'q' or k == 'Q' or ord(k) == 3:
        for th in threads:
            th.stop()
        sys.exit(0)
    else:
        return k


if __name__ == '__main__':
    main()
