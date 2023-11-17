
x_list = [5,8,6,7,9,2,4]

def insertion_sort(x_list):
	sorted_list=[]
	while True:
		sorted_list.append(min(x_list))
		x_list.remove(min(x_list))
		if len(x_list) == 1:
			sorted_list.append(x_list[0])
			break

	return(sorted_list)


answer = insertion_sort(x_list)

print(answer)