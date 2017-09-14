number_list = [10,30,45,82,50,20,44]
print("Old List: ", number_list)


def print_list(nums):
	new_list = []
	for x in number_list:
		new_list.append(x+5)
	print("New List: ", new_list)
	print("Length: ", len(new_list))

print_list(number_list)



