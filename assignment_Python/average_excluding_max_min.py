x=0
num=input("Enter the list of numbers :")
#inserting inputs into list
empty_list=list(num)
#sorting list in ascending order
empty_list.sort()
#removing the last number from list which is the maximum
empty_list.pop()
#rearranging the list from heighest to lowest
new_list=empty_list[::-1]
#removing the last number from the list which is the lowest as it has been rearranged in descending order
new_list.pop()
#using for loop to sum the remaing items in the list
for i in new_list:
    x+=i

average=x/len(new_list)

print "The average after excluding max and min number is {}".format(average)
