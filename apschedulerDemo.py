import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func  time :',ts)

def func2():
    #耗时2S
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：',ts)
    time.sleep(2)

def func3():
    # now = datetime.datetime.now()
    # ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func  time :', 'li')

def dojob():
    #创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    #添加任务,时间间隔2S
    scheduler.add_job(func, 'interval', seconds=2, id='test_job1')
    #添加任务,时间间隔5S
    scheduler.add_job(func2, 'interval', seconds=3, id='test_job2')
    # 定时脚本任务
    scheduler.add_job(func3, 'date', run_date='2020-04-13 21:24:00')

    scheduler.start()
dojob()