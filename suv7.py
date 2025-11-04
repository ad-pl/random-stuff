import time
from random import getrandbits
from uuid import UUID
def uuid7(shift:int=None,rand_a:int=None,rand_b:int=None)->UUID:
	rand_a=rand_a if rand_a!=None else getrandbits(12)
	rand_b=rand_b if rand_b!=None else getrandbits(62)
	shift=shift if shift!=None else 0
	return UUID(bytes=bytes(int(time.time()*1000+shift).to_bytes(6)+((7<<12|(2**12-1&rand_a)).to_bytes(2))+((2<<62|(2**62-1&rand_b)).to_bytes(8))))
def uuid8(a:int,b:int,c:int)->UUID:
	return UUID(bytes=bytes(a.to_bytes(6)+((8<<12|2**12-1&a).to_bytes(2))+(2<<62|2**12-1&b).to_bytes(8)))
