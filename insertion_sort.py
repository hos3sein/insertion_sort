x_list = [8,5,7,9,2,4,6,3]

def insertion_sort(listt):
	sorted_list=[]
	sorted_list.append(listt[0])
	for i in range(1 , len(listt)):
		sorting = listt[i]
		for j in range(len(sorted_list)):
			if sorting < sorted_list[j]:
				sorted_list.insert(j , sorting)
				break
			elif j == (len(sorted_list)-1):
				sorted_list.append(sorting)
	return(sorted_list)




print(insertion_sort(x_list))
