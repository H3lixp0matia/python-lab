import threading
import random
import time

class Pieciu_filozofow(threading.Thread):
    running = True

    def __init__(self, index, leftFork, rightFork):
        threading.Thread.__init__(self)
        self.index = index
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        while(self.running):
            # Filozof myśli
            time.sleep(20)
            print ('Filozof %s jest glodny.' % self.index)
            self.dine()

    def dine(self):
        # Jeśli oba widelce są wolne, filozof zacznie jeść 
        fork1, fork2 = self.leftFork, self.rightFork
        while self.running:
            fork1.acquire() # czeka na lewy widelec
            locked = fork2.acquire(False) 
            if locked: break #jeśli prawy widelec nie jest wolny, filozof zostawia lewy widelec
            fork1.release()
            print ('Filozof %s zmienia widelce.' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        #Filozof zostawia oba widelce po jedzeniu
        fork2.release()
        fork1.release()
 
    def dining(self):			
        print ('Filozof %s zaczyna jeść. '% self.index)
        time.sleep(30)
        print ('Filozof %s kończy jeść i zaczyna myśleć.' % self.index)

def main():
    forks = [threading.Semaphore() for n in range(5)] #Tablica widelcow

    philosophers = [Pieciu_filozofow(i, forks[i%5], forks[(i+1)%5])
        for i in range(5)]

    Pieciu_filozofow.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Pieciu_filozofow.running = False
    print ("Koniec.")
 

if __name__ == "__main__":
    main()