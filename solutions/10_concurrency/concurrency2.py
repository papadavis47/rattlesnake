from threading import Lock, Thread


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def increment(self, amount: int = 1) -> None:
        with self.lock:
            self.value += amount


def run_workers(worker_count: int, increments: int) -> int:
    counter = Counter()

    def work() -> None:
        for _ in range(increments):
            counter.increment()

    threads = [Thread(target=work) for _ in range(worker_count)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return counter.value


class TrackingLock:
    def __init__(self):
        self.events: list[str] = []

    def __enter__(self) -> None:
        self.events.append("enter")

    def __exit__(self, *exc_info: object) -> None:
        self.events.append("exit")


def test_counter_uses_lock():
    counter = Counter()
    tracking_lock = TrackingLock()
    counter.lock = tracking_lock
    counter.increment(2)
    assert tracking_lock.events == ["enter", "exit"]
    assert counter.value == 2


def test_all_thread_updates_are_counted():
    assert run_workers(8, 500) == 4000
