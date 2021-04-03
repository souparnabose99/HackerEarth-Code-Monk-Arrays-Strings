
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
test_count = input()
# print(test_count)
no_of_elements, no_of_rot = input().split(' ')
# print(no_of_elements)
# print(no_of_rot)
array = input()
# print(array)
# print(type(array))
arr_rot = []
for ele in list(array):
    if ele!= ' ':
        arr_rot.append(int(ele))
# print(arr_rot)

def monk_rotation(test_count, arr_rot, no_of_rot, no_of_elements):
    temp_arr = [0]*no_of_elements
    n = no_of_rot
    for i in range(no_of_rot):
        temp_arr[i] = arr_rot[(no_of_elements-n)]
        n -= 1
    m = 0
    for i in range(no_of_rot, no_of_elements):
        temp_arr[i] = arr_rot[m]
        m += 1
    return temp_arr

output = monk_rotation(test_count, arr_rot, int(no_of_rot), int(no_of_elements))
final_output = [str(i) for i in output]
print(' '.join(final_output))



