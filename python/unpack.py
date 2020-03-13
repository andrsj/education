# Unpaccing
	>>> first,second,*rest = (1,2,3,4,5,6,7,8)
	>>> first # Первое значение
	1
	>>> second # Второе значение
	2
	>>> rest # Все остальные значения
	[3, 4, 5, 6, 7, 8]

	#######################

	>>> first,*rest,last = (1,2,3,4,5,6,7,8)
	>>> first
	1
	>>> rest
	[2, 3, 4, 5, 6, 7]
	>>> last
	8