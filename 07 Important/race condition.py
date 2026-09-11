# Race Condition Example
import threading

balance = 100

def withdraw(amount):
    global balance
    temp = balance
    temp = temp - amount
    balance = temp
    print(f"Withdraw {amount}, Balance: {balance}")

# Two threads
t1 = threading.Thread(target=withdraw, args=(50,))
t2 = threading.Thread(target=withdraw, args=(50,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", balance)



#  Solution with Lock
balance = 100
lock = threading.Lock()

def withdraw(amount):
    global balance
    with lock:
        balance -= amount
        return balance
    
