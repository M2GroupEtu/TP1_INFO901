from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
me = comm.Get_rank()
size = comm.Get_size()
print("Hi from <"+str(me)+">")
if me == 0:
    buf = ["coucou"]