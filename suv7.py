import time
import random
import uuid

def uuidv7(shift: int = 0) -> uuid.UUID:
	result = []
	stamp = int(time.time()*1000) + shift
	result.extend(stamp.to_bytes(6, 'big'))
	result.extend((7 << 12 | random.getrandbits(12)).to_bytes(2))
	result.extend((2 << 62 | random.getrandbits(62)).to_bytes(8))
	return uuid.UUID(bytes=bytes(result))
