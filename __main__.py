from random import getrandbits
from uuid import UUID
from time import time
def uuid7(shift:int=None,rand_a:int=None,rand_b:int=None)->UUID:
	return UUID(bytes=bytes(int(time()*1000+(shift or 0)).to_bytes(6)+((7<<12|(2**12-1&(rand_a or getrandbits(12)))).to_bytes(2))+((2<<62|(2**62-1&(rand_b or getrandbits(62)))).to_bytes(8))))
def uuid8(a:int,b:int,c:int)->UUID:
	return UUID(bytes=bytes(a.to_bytes(6)+((8<<12|2**12-1&a).to_bytes(2))+(2<<62|2**12-1&b).to_bytes(8)))
