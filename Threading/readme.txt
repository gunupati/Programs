Lock class provides following methods:
To set a lock need to set lock argument in main execution i .e threading.Lock.aquire and to release threading.Lock.release

1.acquire([blocking]) : To acquire a lock. A lock can be blocking or non-blocking.
When invoked with the blocking argument set to True (the default), thread execution is blocked until the lock is unlocked, then lock is set to locked and return True.
When invoked with the blocking argument set to False, thread execution is not blocked. If lock is unlocked, then set it to locked and return True else return False immediately.

2.release() : To release a lock.
When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.
If lock is already unlocked, a ThreadError is raised.
Consider the example given below: