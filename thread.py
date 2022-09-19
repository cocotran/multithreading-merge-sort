from threading import Thread


class ThreadWithReturnValue(Thread):
    def __init__(
        self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None
    ):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        print(f"Thread {self.name} started")
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        print(f"Thread {self.name} finished: {self._return}")
        return self._return


class ThreadManager:
    def __init__(self) -> None:
        self.thread_count = 0

    def get_new_thread_name(self) -> str:
        self.thread_count += 1
        return bin(int(self.thread_count)).replace("0b", "")
