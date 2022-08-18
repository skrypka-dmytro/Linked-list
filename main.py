from linked_list import LinkedList

my_list = LinkedList()

my_list.append(2)
my_list.append(4)
my_list.append(8)
my_list.append(6)
my_list.append(16)

print(my_list.value_at(1))

my_list.push_front(1)

my_list.show()

my_list.insert(2, 9)

my_list.remove(2)

my_list.remove_back()

my_list.remove_front()

my_list.reverse()

my_list.show()

my_list.length()
