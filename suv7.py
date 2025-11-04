import time
from random import getrandbits
from uuid import UUID

def bitmasker(x:int,size:int)->int:
	return (2**size-1)&x
def uuidv7(shift:int=0,rand_a:int=getrandbits(12),rand_b:int=getrandbits(62))->UUID:
	result=(int(time.time()*1000) + shift).to_bytes(6,'big')
	result.extend((7<<12|bitmasker(rand_a,12)).to_bytes(2))
	result.extend((2<<62|bitmasker(rand_b,62)).to_bytes(8))
	return UUID(bytes=bytes(result))
def uuidv8(custom_a:int,custom_b:int,custom_c:int)->UUID:
	custom_a=bitmasker(custom_a,48)
	custom_b=bitmasker(custom_b,12)
	custom_c=bitmasker(custom_c,62)
	result=list(custom_a.to_bytes(6))
	result.extend((8<<12|bitmasker(custom_b,12)).to_bytes(2))
	result.extend((2<<62|bitmasker(custom_c,62)).to_bytes(8))
# why no 1-6:
# 1,3,4,5: python already has it
# 2: why do you need it
# 6: 'Systems that do not involve legacy UUIDv1
#     SHOULD use UUIDv7 (Section 5.7) instead.' - rfc-editor.org
