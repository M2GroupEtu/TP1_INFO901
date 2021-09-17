from mpi4py import MPI
import sys

if (len(sys.argv) > 1) :
    _from = int(sys.argv[1])
else :
    _from = 0

comm = MPI.COMM_WORLD
me = comm.Get_rank()
size = comm.Get_size()
print("Hi from <"+str(me)+">")

if _from >= size:
    print("ERR : _FROM PARAMETER IS BIGGER THAN " + str(size - 1))
    print("SOLUTION : _FROM MUST BE LESS THAN : " + str(size - 1))
    exit()

last = (_from + size - 1) % size
prev = (me - 1 + size) % size
next = (me + 1) % size


if me == _from:
    buf = ["coucou"]
    comm.send(buf, dest= next, tag=99)
elif me != last :
    buf = comm.recv(source = prev , tag=99)
    comm.send(buf, dest= next, tag=99)
else :
    buf = comm.recv(source= prev , tag=99)

print("I'm <"+str(me)+">: receive " + buf[0])