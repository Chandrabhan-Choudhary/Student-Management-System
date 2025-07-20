#  Student Management System 
# Importing Required Libraries and Modules
import mysql.connector as sqltor
import matplotlib.pyplot as plt
a='*'*17
b='*'*43
# Establishing Connection With MySQL
mycon=sqltor.connect(host='localhost',user='root',passwd='password' ,database='school_db')
if mycon.is_connected()==False:
  print('error in connection')
elif mycon.is_connected()==True:
  print('Connection Established Successfully!')
# Setting Up Cursor
cursor=mycon.cursor()
# Creating Database
cursor.execute("create database if not exists school_db;")
cursor.execute("use school_db;")
# Creating Student Table
creat_tb="create table if not exists student (Admno int(5) primary key,Rollno int(5) not null, Name varchar(35),Class int(3),Section varchar(2),Age int(3),Gender varchar(2),Aadhar int(16),SSMID int(10))"
cursor.execute(creat_tb)
cursor.rowcount

# Function For Adding New Student Data
def new():
  print(' ')
  print(b)
  print('                New Student')
  print(b)
  Admno=input('Admission  Number ~ ')
  Rollno=input('Roll Number ~ ')
  Name=input('Name ~ ')
  Class=input('Class ~ ')
  Section=input('Section ~ ')
  Age=input('Age ~ ')
  Gendr=input('Gender ~ ')
  Adharno=input('Aadhar Number ~ ')
  ssm=input('SSMID ~ ')
  print(' ')
  # Inserting Data In MySQL
  qry = "insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
  values = (Admno, Rollno, Name, Class, Section, Age, Gendr, Adharno, ssm)
  cursor.execute(qry, values)

  mycon.commit()
  print('Added Successfully!')
  cursor.rowcount
  print(" ")
  def conti1():
      print(b)
      print(' ')
      print('Do You Want To Continue?')
      print('y : yes')
      print('n : no')
      a=input('y or n ~ ')
      if a=='y':
         print(' ')
         new()
      elif a=='n':
         print(' ')
         main2()
      else :
         print(' ')
         print('Error!! xx Wrong Input xx')
         print(' ')
         conti1()
  conti1()
  
# Designing Secondary Menu
def main2():
    print(' ')
    print('1 : New Student Record')
    print('2 : Update Student Record')
    print('3 : Delete Student Record')
    print('4 : Search Student Record')
    print('5 : Previous Menu')
    print (' ')
    inpt2=int(input('Choose any one option ~ '))
    if inpt2==1:
      new()
    elif inpt2==2:
      updt()
    elif inpt2==3:
      delete()
    elif inpt2==4:
      search()
    elif inpt2==5:
      main1()
    else:
      print(' ')
      print('Error!! xx Wrong Input xx')
      main2()
      
# Function For Updation Of Student Data
def updt():
    print(b)
    print('              Update Records')
    print(b)
    Admno=input('Admission  Number ~ ')
    print('What would you like to update? ')
    print('1 : Roll Number')
    print('2 : Class ')
    print('3 : Section ')
    print('4 : Age')
    choic=int(input('Choose Any One Option ~ '))
    print(' ')
    if choic==1:
       Rollno=input('New Roll Number ~ ')
       qry="update student set Rollno=%s where Admno=%s"
       cursor.execute(qry,(Rollno, Admno))
       cursor.rowcount
       mycon.commit()
    elif choic==2:
       Class=input('New Class ~ ')
       qry="update student set Class=%s where Admno=%s"
       cursor.execute(qry,(Class,Admno))
       cursor.rowcount
       mycon.commit()
    elif choic==3:
       Section=input('New Section ~ ')
       qry="update student set Section=%s where Admno=%s"
       cursor.execute(qry,(Section,Admno))
       cursor.rowcount
       mycon.commit()
    elif choic==4:
       Age=input('New Age ~ ')
       qry="update student set Age=%s where Admno=%s"
       cursor.execute(qry,(Age,Admno))
       cursor.rowcount
       mycon.commit()
    else:
       print(' ')
       print('Error!! xx Wrong Input xx')
       print(' ')
       updt()
    print(' ')
    print('Updated Successfully!')
    print(' ')
    def conti2():
        print(' ')
        print('Do You Want To Continue?')
        print('y : yes')
        print('n : no')
        a=input('y or n ~ ')
        if a=='y':
           print(' ')
           updt()
        elif a=='n':
           print(' ')
           main2()
        else :
           print(' ')
           print('Error!! xx Wrong Input xx')
           print(' ')
           conti2()
    conti2()
  
# Function For Deletion Of Student Data
def delete():
    print(b)
    print('              Delete Records')
    print(b)
    Admno=[input('Admission  Number To delete ~ ')]
    qry="delete from student where Admno=%s"
    cursor.execute(qry,(Admno))
    cursor.rowcount
    mycon.commit()
    print(' ')
    print('Deleted Successfully !')
    print(' ')
    def conti3():
        print(' ')
        print('Do You Want To Continue?')
        print('y : yes')
        print('n : no')
        a=input('y or n ~ ')
        if a=='y':
           print(' ')
           delete()
        elif a=='n':
           print(' ')
           main2()
        else :
           print(' ')
           print('Error!! xx Wrong Input xx')
           print(' ')
           conti3()
    conti3()
  
# Function For Searching For a Student
def search():
    print(b)
    print('            Search For Student')
    print(b)
    Rollno=[input('Roll Number To Be Searched ~ ')]
    qry="select * from student where Rollno=%s"
    cursor.execute(qry,(Rollno))
    cursor.rowcount
    rows = cursor.fetchall()

    if cursor.rowcount == 0:
        print("No student record found.")
    else:
        print("Student Record Found!!:")
        print("{:<7} {:<7} {:<35} {:<7} {:<7} {:<7} {:<7} {:<16} {:<10}".format(
         "Admno", "Rollno", "Name", "Class", "Section", "Age", "Gender", "Aadhar", "SSMID"))
        for row in rows:
            print("{:<7} {:<7} {:<35} {:<7} {:<7} {:<7} {:<7} {:<16} {:<10}".format(
             row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            
    def conti3():
        print(' ')
        print('Do You Want To Continue?')
        print('y : yes')
        print('n : no')
        a=input('y or n ~ ')
        if a=='y':
           print(' ')
           search()
        elif a=='n':
           print(' ')
           main2()
        else :
           print(' ')
           print('Error!! xx Wrong Input xx')
           print(' ')
           conti3()
    conti3()
  
# Function For Analysis Of Data
def analysis():
   print(b)
   print('               Data Analysis')
   print(b)
   # Execute the query to get the number of students in each class
   qry = "SELECT Class, COUNT(*) FROM student GROUP BY Class"
   cursor.execute(qry)

   # Store the results in a list
   results = cursor.fetchall()

   # Create a list to store the class names
   class_names = []

   # Create a list to store the number of students in each class
   student_count = []

   # Iterate through the results and add the class name and student count to the appropriate lists
   for result in results:
       class_names.append(result[0])
       student_count.append(result[1])

   # Plot the data using matplotlib
   plt.bar(class_names, student_count,color='pink')
   plt.xlabel("Class")
   plt.ylabel("Number of Students")
   plt.title("Number of Students in Each Class")
   plt.show()
   input('Press Enter Key To Continue')
   main1()
  
# Designing Main Menu
def main1():
  print(a,'Welcome',a)
  print(' ')
  print('1 : Modify Database')
  print('2 : View Database')
  print('3 : Graphical Analysis')
  print('4 : Exit')
  print(' ')
  inpt1=int(input('Choose any one option ~ '))
  print(' ')
  print(b)
  if inpt1==1:      
       main2()
  elif inpt1==2:
       print(b)
       print(' ')
       qry="SELECT * FROM student ORDER BY Rollno"
       cursor.execute(qry)
       cursor.rowcount
       rows = cursor.fetchall()

       if cursor.rowcount == 0:
           print("No student records found.")
       else:
           print("Student Records:")
           print("{:<7} {:<7} {:<35} {:<7} {:<7} {:<7} {:<7} {:<16} {:<10}".format(
            "Admno", "Rollno", "Name", "Class", "Section", "Age", "Gender", "Aadhar", "SSMID"))
           for row in rows:
               print("{:<7} {:<7} {:<35} {:<7} {:<7} {:<7} {:<7} {:<16} {:<10}".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
           
       print(' ')
       print(b)
       input("Press enter key to continue")
       main1()
  elif inpt1==3:
       analysis()
  elif inpt1==4 :
       # Close the cursor and connection
       cursor.close()
       mycon.close()
       print(' ')
       print('Thanks!  See You Again ')
       print(' ')
       print(b)
  elif inpt1>4:
       print(' ')
       print('Error!! xx Wrong Input xx')
       print(' ')
       print(b)
       main1()    
main1()