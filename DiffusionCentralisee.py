from mpi4py import MPI
import sys

if len(sys.argv) > 1 :
    sender = int(sys.argv[1])

comm = MPI.COMM_WORLD
me = comm.Get_rank()
size = comm.Get_size()

print("Hi from <"+str(me)+">")

if me == sender:
    buf = ["coucou"]
    print("I'm <"+str(me)+">: send " + buf[0])
    for i in range(0, size):
        if(i != sender):
	        comm.send(buf, dest=i, tag=99)
else:
    buf = comm.recv(source=sender, tag=99)
    print("I'm <"+str(me)+">: receive " + buf[0])
