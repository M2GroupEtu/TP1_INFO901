from mpi4py import MPI
import sys

if (len(sys.argv) > 2) :
    _from = int(sys.argv[1])
    sens = int(sys.argv[2])
else :
    _from = 0
    sens = 1

comm = MPI.COMM_WORLD
me = comm.Get_rank()
size = comm.Get_size()
print("Hi from <"+str(me)+">")

if _from >= size:
    print("ERR : _FROM PARAMETER IS BIGGER THAN " + str(size - 1))
    print("SOLUTION : _FROM MUST BE LESS THAN : " + str(size - 1))
    exit()

prev = (me - 1 + size) % size
next = (me + 1) % size

print("NEXT : " + str(prev))
print("PREV : " + str(next))

def anneau_1_sens() :
    last = (_from + size - 1) % size

    if me == _from:
        buf = ["coucou"]
        comm.send(buf, dest= next, tag=99)

    elif me != last :
        buf = comm.recv(source = prev , tag=99)
        comm.send(buf, dest= next, tag=99)

    else :
        buf = comm.recv(source= prev , tag=99)

    print("I'm <"+str(me)+">: receive " + buf[0])

def anneau_2_sens():
    last_from_0 = round((size/2) + 0.1)
    true_last = (last_from_0 + _from) % size

    if me == _from:
        buf = ["coucou"]
        comm.send(buf, dest= next, tag=99)
        comm.send(buf, dest= prev, tag=99)

    elif me == true_last:
        buf = comm.recv(source= prev , tag=99)
        comm.recv(source= next , tag=99)

    elif me < (_from + size)/2 :
        buf = comm.recv(source= prev , tag=99)
        comm.send(buf, dest= next, tag=99)

    elif me > (_from + size)/2 :
        buf = comm.recv(source= next , tag=99)
        comm.send(buf, dest= prev, tag=99)
    
    print("I'm <"+str(me)+">: receive " + buf[0])


#APPEL DES FONCTIONS
if sens == 1 :
    anneau_1_sens()
else :
    anneau_2_sens()