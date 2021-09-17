from mpi4py import MPI
import sys

if (len(sys.argv) > 1) :
    _from = int(sys.argv[1])
else :
    _from = 0

comm = MPI.COMM_WORLD
me = comm.Get_rank()
size = comm.Get_size()

if _from >= size:
    print("ERR : _FROM PARAMETER IS BIGGER THAN " + str(size - 1))
    print("SOLUTION : _FROM MUST BE LESS THAN : " + str(size - 1))
    exit()

print("Hi from <"+str(me)+">")

if me == _from:
    buf = ["coucou"]
    print("I'm <"+str(me)+">: send " + buf[0])
    for i in range(0, size):
        if(i != _from):
	        comm.send(buf, dest=i, tag=99)
else:
    buf = comm.recv(source=_from, tag=99)
    print("I'm <"+str(me)+">: receive " + buf[0])
