'''

Assignment :Group B -16
Write a python program to store first year percentage of students in array.
Write function for sorting array of floating point numbers in ascending order
using  quick sort and display top five scores.

'''

def accept_percentage(A):
    n=int(input("Enter number of students in first year : "))
    for i in range(n):
        per=float(input(" Enter percentage of student : "))
        A.append(per)


def display(A):
    if(len(A) == 0):
          print("No record found !!")
    else:
          print("Percentage of students : ",end=" ")
          for i in range(len(A)):
              print(A[i],end="  ")
          print("\n")

def quick_sort(A, low, high):
    if low< high:
        p = partition(A, low, high)
        quick_sort(A, low, p-1)
        quick_sort(A, p+1, high)



def partition( A, low, high):
    pivot = low
    left = low + 1
    right = high

    while right >= left:
        while A[left] <= A[pivot] and left<=high:
            left = left + 1

        while A[right] > A[pivot]:
            right = right - 1

        if left < right:
            A[left], A[right] = A[right], A[left]
        
    A[pivot], A[right] = A[right],A[pivot]
    return right







    


def main():
    while True:
       print("\n")
       print("\t1: Accept first year percentage of students ")
       print("\t2: Display percentage ")
       print("\t3: quick Sort")
       print("\t4: Display top five scores")
       print("\t5: Exit")
       ch=int(input("\t Enter Your Choice : "))
       
       if ( ch==5 ):
           print("\t End of Program!")
           quit()
       elif(ch==1):
           stud_marks=[]
           accept_percentage(stud_marks)
         
       elif(ch==2):
           display(stud_marks)
          

       elif(ch==3):
           quick_sort(stud_marks, 0, len(stud_marks)-1)
           display( stud_marks)
           
       elif(ch==4):
          quick_sort(stud_marks, 0, len(stud_marks)-1)
          n=len(stud_marks)
          if n >=5 :
              print(" Top five scores : ")
              for i in range(n-1, n-6, -1):
                  print("\t  ",stud_marks[i])
          else:
              print(" Top scores : ")
              for i in range(n-1, -1, -1):
                  print("\t  ",stud_marks[i])
          
           
       else:
           print("\t Invalid Choice !!!")

main()


'''
Output :
	1: Accept first year percentage of students 
	2: Display percentage 
	3: quick Sort
	4: Display top five scores
	5: Exit
	 Enter Your Choice : 4
 Top scores : 
	   99.0
	   55.0
	   44.0


	1: Accept first year percentage of students 
	2: Display percentage 
	3: quick Sort
	4: Display top five scores
	5: Exit
	 Enter Your Choice : 6
	 Invalid Choice !!!


	1: Accept first year percentage of students 
	2: Display percentage 
	3: quick Sort
	4: Display top five scores
	5: Exit
	 Enter Your Choice : 5
	 End of Program!

'''







           
           
