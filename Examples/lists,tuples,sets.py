

'''
 index always starts at 0 
 use sqaure brackets to pass in the location of the valules that we want
 -1 always means we want the last value in the list
 when using :(number) it means that it prits the list from 0 to (number)-1 so if it is :4 it would print 0,1,2,3 other way around when it is (number):
 This is called slicing

'''
#* When wanting to add an value to a specific location in a list we use (insert). This takes in two arguments, the index and the value itself.
#* courses.insert(0, "Art")
#* When wanting to add multiple values to a list we use (extend). 
#* Use courses.remove for removing a specific value from a list.
#* Use courses.pop for removing the last value from a list.
#* Use courses.reverse for reversing a list.
#* Use courses.sort for sorting a list in alphabetical order. If list contains numbers it will sort in ascending order.
#* Use courses.sort(reverse=True) for sorting a list in reverse.
#* Most of the time you dont have to alter the original list, this is where you use sorted(). This will not change the original list but will return a sorted list.

courses = ["History", "Math", "Science", "CompSci"]
courses_2 = ["Art", "Education"]
courses.extend(courses_2)
courses.pop() 
pop = courses.pop()
print(pop)
nums = [5, 76 , 1 , 7, 15 , 27]
nums.sort()
sorted_courses = sorted
#* print(courses.index(value)) returns the index of a value in a list.
#* print("value" in courses) returns true if a value is in a list.  
print(courses)
#* print(sum(nums)), print(max(nums)), print(min(nums)).
print(nums)
#* can name (i) anything you want it is just a variable name.
#* for i in enumerate(courses): will print the index and values in a lsit
for i in enumerate(courses, start = 1):
    print(i)
#* change into string course_str = ",".join(courses)
#* create list from string, course_str.split()
course_str = ", ".join(courses)
new_list = course_str.split(", ")

print(new_list)
print(course_str)

#*20 mins








