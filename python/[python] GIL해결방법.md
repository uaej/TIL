# [python]GIL 해결방법

## 1. 문제점
파이썬에서 멀티 스레드를 사용하면 싱글 스레드보다 속도가 느리다!
왜? 한번에 한개의 전역변수에 접근할 수 있도록 하는 GIL 때문.
![GIL_problem](/image/python_thread_problem.JPG)

## 2. 해결방법
멀티 스레드 대신에 멀티 프로세스를 사용한다.
![GIL_solve](/image/python_thread_solve.JPG)

## 3. 소스코드
> 1부터 20000000까지 더하는 프로그램

<li> single thread
    from threading import Thread
    import time

    def do_work(start, end, result):
        sum = 0
        for i in range(start, end):
                sum += i
        result.append(sum)
        return

    if __name__ == "__main__" :
        start_time = time.time()
        START, END = 0, 20000000
        result = list()
        th1 = Thread(target=do_work, args = (START, END, result))
        th1. start()
        th1.join()
        end_time = time.time()

    print ("Result : ", sum(result))
    print("Time : ", (end_time - start_time))

<li> multi thread

    from threading import Thread
    import time

    def do_work(start, end, result):
        sum = 0
        for i in range(start, end):
                sum += i
        result.append(sum)
        return

    if __name__ == "__main__" :
        start_time = time.time()
        START, END = 0, 20000000
        result = list()
        th1 = Thread(target=do_work, args = (START, int(END/2), result))
        th2 = Thread(target=do_work, args = (int(END/2), END, result))
        th1. start()
        th2. start()
        th1.join()
        th2.join()
        end_time = time.time()

    print ("Result : ", sum(result))
    print("Time : ", (end_time - start_time))

    <li> multi processor
    from multiprocessing import Process, Queue
    import time

    def do_work(start, end, result):
            sum = 0
            for i in range(start, end):
                    sum += i
            result.put(sum)
            return

    if __name__ == "__main__" :
            start_time = time.time()
            START, END = 0, 20000000
            result = Queue()
            pr1 = Process(target=do_work, args = (START, int(END/2), result))
            pr2 = Process(target=do_work, args = (int(END/2), END, result))
            pr1. start()
            pr2. start()
            pr1.join()
            pr2.join()
            result.put('STOP')
            sum = 0
            while True :
                    tmp = result.get()
                    if tmp == 'STOP' : break
                    else : sum += tmp
            end_time = time.time()
    print ("Result : ", sum)
    print("Time : ", (end_time - start_time))


## 4. 참고 사이트
http://qkqhxla1.tistory.com/270
