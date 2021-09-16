from mpi4py import MPI

#mpiexec -n 4 py HelloWorld.py
#test

comm = MPI.COMM_WORLD
me = comm.Get_rank()
size = comm.Get_size()
print("Hi from <"+str(me)+">")
