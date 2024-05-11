import os

from natsort import natsorted, realsorted, humansorted, os_sorted

list1 = ['5', '6', '8', '12', '16']
print(sorted(list1))  # usual sort

list2 = ['5 m 10 cm', '6 m 2 cm', '8 ft 15 in', '12 m 24 cm', '16 ft 12 in']
print(natsorted(list2))  # natsorted

list3 = ['version-1.4.2', 'version-2.5.6', 'version-1.8.3', 'version-1.7.2', 'version-4.0.9']
print(natsorted(list3))  # natsorted

list4 = ['1.2', '-3', '2.4', '-3.4', '6.1']
print(realsorted(list4))  # realsorted

list5 = ['apple', 'book', 'laptop', 'clown', 'keyboard']
print(humansorted(list5))  # humansorted

print(os_sorted(os.listdir('/')))  # os_sorted
