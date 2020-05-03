def even_odd(list_num,odd=0,even=0):
	for  num in list_num:
		if num %2!=0 :
			odd+=1
			print("number of odd numbers in the list is :",odd)
		else:
			even+=1
			print("number of even numbers in the list is :",even)
			
even_odd([19,73,64,5,49,72,33,59,10,71,82,13,34,55,66,37,93,72,30,55])
