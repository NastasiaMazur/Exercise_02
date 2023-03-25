
#1
numbers = [1, 2, 3, 4, 5, 6, 7, 6, 8, 9]
integer = 6

def count_integer(numbers, integer):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == integer:
            count += 1
    if count > 0:
        return count
    else:
        return 42

print(count_integer(numbers, integer))


#2
def list_func(numbers, integer):
    list_copy = numbers.copy()

    if integer in list_copy:
        index = list_copy.index(integer)
        list_copy[index] = 6
    else:
        return []

    list_copy.reverse()
    print(list_copy)

    return numbers

numbers = [1, 2, 3, 4, 5, 6, 7]
integer = 4
new_list = list_func(numbers, integer)
print(new_list)


#3
def compare_lists(list1, list2):
    common = []
    for elem in list1:
        if elem in list2 and elem not in common:
            common.append(elem)

    return common

list1 = [1, 2, 3, 9, 10]
list2 = [3, 4, 5, 6, 7, 8, 9]
common_list = compare_lists(list1, list2)
print(common_list)


#4
def remove_duplicates(lst):
    unique_set = set()
    unique_list = []
    for elem in lst:
        if elem not in unique_set:
            unique_set.add(elem)
            unique_list.append(elem)

    return unique_list

lst = [1, 1, 2, 2, 3, 4, 5, 66, 77, 55, 55, 55, 77, 90]
new_list = remove_duplicates(lst)
print(new_list)


#5
def dict_func(my_dict):
    type_value = my_dict.get("Type", "unknown type")
    brand_value = my_dict.get("Brand", "unknown brand")
    price_value = my_dict.get("Price", "unknown price")
    print(f"You have a {type_value} from {brand_value} that costs: {price_value}.")

    my_dict["OS"] = 'Windows'

    print(my_dict)
    return my_dict


my_dict = {"Type": "laptop", "Brand": "Huawei", "Price": 700}
#my_dict = {"Type": "laptop", "Price": 700}
dict_func(my_dict)