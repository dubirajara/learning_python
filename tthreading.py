from threading import Thread
import time

# def make(i):
# 	print('ejecutando thread {}'.format(i))
# 	time.sleep(3)
# 	print('finalizando thread {}'.format(i)) 


# for i in range(5):
# 	t = Thread(target=make, args=(i,))
# 	t.start()


def worker(message):
    for i in range(5):
        print(message)
        time.sleep(1)
 
 
t = Thread(target=worker,args=("thread sendo executada",))
t.start()
while t.isAlive():
    print("Aguardando thread")
    time.sleep(5)
 
print("Thread morreu")
print("Finalizando programa")