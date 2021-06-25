from threading import Lock
import json
import threading


class Foo:
    def __init__(self):
        self.firstdone = Lock()
        self.seconddone = Lock()
        self.firstdone.acquire()
        self.seconddone.acquire()
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        self.firstdone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.firstdone:
        # printSecond() outputs "second".
            printSecond()
            self.seconddone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait for the second job to be done.
        with self.seconddone:
        # printThird() outputs "third".
            printThird()

class Solution:
    def __init__(self) -> None:
        self.foo = Foo()
        pass

    def foobar(self, nums):
        pool = []
        for num in nums:
            if num==1:
                pool.append(threading.Thread(target=self.foo.first,args=(print1,)))
            elif num==2:
                pool.append(threading.Thread(target=self.foo.second,args=(print2,)))
            elif num==3:
                pool.append(threading.Thread(target=self.foo.third,args=(print3,)))
        for p in pool:
            p.start()
        for p in pool:
            p.join()

def print1():
    print("First")

def print2():
    print("Second")

def print3():
    print("Third")


Solution().foobar([1,3,2])
