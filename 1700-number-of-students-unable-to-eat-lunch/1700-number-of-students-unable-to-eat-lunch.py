from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):


        students=deque(students)
        sandwiches=deque(sandwiches)
        rotation=0

        while students and sandwiches:
            if sandwiches[0]==students[0]:
                sandwiches.popleft()
                students.popleft()
                rotation=0

               
            else:
                students.append(students.popleft())
                rotation+=1

            if rotation == len(students):
                break
            
        return len(students)
        
        # count=0
        # if students==sandwiches:
        #     return 0
        
        # while students and sandwiches:
            
        #     if len(sandwiches)==1 and  len(students)==1:
        #         if students != sandwiches:
        #             count+=1
 
        #     elif sandwiches[0]==students[0]:
        #         sandwiches.remove(sandwiches[0])
        #         students.remove(students[0])
        #         count+=1
        #     else:
        #         front=students[0]
        #         del students[0]
        #         students.append(front)
        
        # return count
            

                

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna