out_file = open("name.txt", 'w')
name = input("please input your name:")
print("Your name is {}".format(name), file=out_file)
out_file.close()

read_file = open("name.txt",'r')
read_name = print(read_file.read())
read_file.close()

r_n = open("Prac 02/numbers.txt",'r')
read_l = r_n.readlines()
print(int(read_l[0])+int(read_l[1]))

read_nums = open("Prac 02/numbers.txt",'r')
sum = 0
for line in read_nums:
    sum = sum + int(line)
print(sum)
read_nums.close()