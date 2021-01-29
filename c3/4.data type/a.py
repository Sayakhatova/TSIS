"""
Text Type:	str
Numeric Types:	int, float, complex(x = 1j)
Sequence Types:	list( ["apple", "banana", "cherry"] ), tuple( ("apple", "banana", "cherry") ), range( range(6) )
Mapping Type:	dict( {"name" : "John", "age" : 36} )
Set Types:	set( {"apple", "banana", "cherry"} ), frozenset( frozenset({"apple", "banana", "cherry"}) )
Boolean Type:	bool
Binary Types:	bytes( b"Hello" ), bytearray( bytearray(5) ), memoryview( memoryview(bytes(5)) )
"""
#You cannot convert complex numbers into another number type

#random numbers
import random
print(random.randrange(1, 10))