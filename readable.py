import random, uuid, time
def uuid7(shift:int=None,rand_a:int=None,rand_b:int=None)->uuid.UUID:
	return uuid.UUID(
    bytes=bytes(
      (int(time.time()*1000+(shift or 0))&2**48-1).to_bytes(6)
      +((7<<12|(2**12-1&(rand_a or random.getrandbits(12)))).to_bytes(2))
      +((2<<62|(2**62-1&(rand_b or random.getrandbits(62)))).to_bytes(8))
    )
  )
def uuid8(a:int,b:int,c:int)->uuid.UUID:
	return uuid.UUID(
    bytes=bytes(
      (2**48-1&a).to_bytes(6)
      +((8<<12|2**12-1&b).to_bytes(2))
      +(2<<62|2**62-1&c).to_bytes(8)
    )
  )
