import time
import datetime
import sched

timer = sched.scheduler(time.time, time.sleep)

def work(i):
    def process():
        print('work {}'.format(i))
    return process

def loop():
    now = datetime.datetime.now()
    print(now)
    for i in range(1, 3):
        tp = now + datetime.timedelta(seconds=3)
        print('lie in {}'.format(tp))
        timer.enter(3, 2, work(i))
    ns = datetime.timedelta(seconds=10).seconds
    timer.enter(ns, 1, loop)

loop()
timer.run()