#def function_name():
 #   return "hello"
#datafromfunction = function_name()
#print(datafromfunction)


#def                     =>Function keyword [define]
#say_hello()             =>Function name
#name                    =>parameter
#print(f"hello{name}")   =>task
#say_hello("yazan")      =>yazan is the argument

#a, b, c = "leen", "yazan", "Taim"
#def say_hello(name):
 #   print(f"hello {name}")

#say_hello("yazan")

#******

#def addition(n1, n2):

 #   if type(n1) != int or type(n2) != int:
  #      print("only integer allowed")

   # else:
    #print(n1 + n2)

#addition(20 , 7)

#******

#def full_name(first, middle, last):
 #   print(f"hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")
#full_name("leen", "yazan", "shorman")

#******

#def say_hello(*peoples):

 #  for name in peoples:
  #     print(f"hello {name}")

#ay_hello("leen", "ahmed", "rami", "awos")

#******

#def say_hello(name, age, country = "unknown"):
   # print("hello {name} your age {age} and your country is {country}")

#say_hello("sameh", "23",)

#******

#myskills = {
 #   "html": "80%",
  #  "css": "60%",
   # "js": "50%"
#}

#def show_skills(**skills):#**dictionary
 #   print(type(skills))

  #  for skills, value in skills.items():
   #     print(f"{skills} => {value}")

#show_skills(**myskills)

#scope**********************************

#def one():
 #   global x
 #  x = 2
 #    print(f"print variable from function scope {x}")

#def two():
 #   x = 10
 #  print(f"print variable from global scope {x}")

#one()
#print(f"print variable from global scope {x}")
#two()
#print(f"print variable from global scope after one function is called{x}")

#*****************************************************************************
#recursion function

#def cleanword(word):
    
#    if len(word) == 1:
#        return word
    
#    print(f"print start function {word}")
    
#    if word[0] == word[1]:
        
#        print(f"print before condition {word}")
#        return cleanword(word[1:])
    
#    print(f"print before return{word}")
    
#    return word[0] + cleanword(word[1:])

#print(cleanword("wwwoooorrrldd"))

#*********************************************************************
#lambda function

#def say_hello(name, age): return f"hello {name} your age is: {age}"

#hello = lamba name, age:  f"hello {name} your age is: {age}"

#print(say_hello("leen", 20))
#print(hello("leen", 20))

#print(say_hello._name_)
#print(hello._name_)
#print(type(hello))

#***************************************************************************
#file handling

#file = open("D:\python\Files\leen.txt")

#import le
#main current working directory

#print(le.getcwd())

#directory for the opened file
#print(le.path.dirname(le.path.abspath(_file_)))

#le.chdir(le.path.dirname(le.path.abspath(_file_)))
#print(le.getcwd())
#file = open("leen.txt")


#read file
#myfile = open("D:\python\Files\leen.txt", "r")
#print(myFile) #file data object
#print(myFile.name)
#print(myFile.mode)
#print(myFile.encoding)

#print(myFile.read())
#print(myFile.readline(10))
#print(type(myFile.readlines()))

#for line in myfile:
   #print(line)
   #if lin.startswith("07")
      #break
#myfile.close()

#write & append file

#myfile = open("D:\python\Files\leen.txt", "w")
#myFile.write("hello from python File")

#myList = ["leen\n", "ahmed\n", "rama\n"]
#myFile= open("D:\python\Files\leen.txt", "w")
#myFile.writelines(myList)

#myfile = open("D:\python\Files\leen.txt", "a") #append
#myFile.write("hello from python File")

#importantFile info

#myfile = open("D:\python\Files\leen.txt", "a")
#myFile.truncate(5) #byte num

#**************************************************

#x = [2, 4, 6, 7, ]
#if any(x):
 #   print("there is at least one element is true")# any is for all elements true 
#else:
 #   print(there no any true element is true)
#print(bin(100))#binary
#a = 1
#print(id(a))

#*********************************************************

#sum(iterable, start)
#a = [2, 4, 10, 30]
#print(sum(a))
#print(sum(a, 10))

#round(number, numofdigits)
#print(round(150.501))
#print(round(150.554, 2))

#range(start, end, step)
#print(list(range(0)))
#print(list(range(10)))
#print(list(range(0, 20, 2)))

#print()
#print("hello @ leen @ how @ are @ you")
#print("hello" , "leen" , "how" , "are" , "you", sep= "|")

#print("first line", end= "look its me end ")
#print("secound line")
#print("third line")


#with open("example.txt", "w", encoding = "utf-8") as file:
#    file.write("hi leen!, this is the first file for you" )

#with open("example.txt", "r", encoding = "utf-8") as file:
#    content = file.read()
#    print(content)

#**********************************************************************************

#def show_menu():
#    print("\n--- menu ---")
#    print("1. add task ")
#    print("2. show tasks")
#    print("3. delet task")
#    print("4. save tasks in file")
#    print("5. finish")

#tasks = []

#while True:
 #   show_menu()
  #choice = input("choice num:")
    #if choice == "1":
     #   task = input("enter task:")
      #  tasks.append(task)
       # print("the task added!")
        #print("current tasks:")
        ##   print(i, "-", t)

  #  elif choice == "2":
   #     for i, task in enumerate(tasks, start = 1):
    ##elif choice == "3":
      ##     num = input("enter the num of task to delete:")
        #    tasks.pop(num-1)
         #   print("task seleted!")
      #  except (ValueError, IndexError):
       ##elif choice == "4":
        #with open ("tasks.txt", "w", encoding = "utf-8") as file:
         #   for task in tasks:
          #      file.write(task + "\n")
       # print("task saved in file.")

    #elif choice == "5":
     #   print("good buy!")
      #  break
    #else:
     #   print("false, try again")

#//////////////////////////////////////////////////////////////////////

#while True:
#    print("\n--- calculator ---")
#    num1 = float(input("enter num1:"))
#    num2 = float(input("enter num2:"))

#    print("choice operation:")
#    print("1. addition.")
#    print("2. subtraction.")
#    print("3. multiplication")
#    print("4. division")
#    print("5. finish")

#    choice = input("enter num of operation:")

#    if choice == "1":
#        print("the result:", num1 + num2)
#    elif choice == "2":
#        print("the result:", num1 - num2)
#    elif choice == "3":
#        print("the result:", num1 * num2)
#    elif choice == "4":
#        if num2 != 0:
#            print("the result:", num1 / num2)
#        else:
#            print("error: It cannot be divided by zero.")
#    elif choice == "5":
#        print("good buy")
#        break
#    else:
#        print("false choice.")

#***************************************************************************************

#def average_list(numbers):
#    total = sum(numbers)#تجمع كل الارقام بالقائمة
#    count = len(numbers)#عدد العناصر بالقائمة
#    average = total / count
#    return average

#تجربة الدالة
#nums = [10, 20, 30, 40]
#result = average_list(nums)
#print("The average is:", result)


#another solu
#import math   # مكتبة الرياضيات فيها sqrt

#def analyze_list(numbers):
#    total = 0
#    count = 0
#    for num in numbers:   # نمر على كل عنصر
#        total += num
#        count += 1
#    average = total / count

#    largest = max(numbers)   # أكبر رقم
#    smallest = min(numbers)  # أصغر رقم

    # حساب الانحراف المعياري
#    variance_sum = 0
#    for num in numbers:
#        variance_sum += (num - average) ** 2   # مربع الفرق عن المتوسط
#    variance = variance_sum / count
#    std_dev = math.sqrt(variance)

#    return average, largest, smallest, total, std_dev

# المستخدم يدخل الأرقام
#nums_input = input("Enter numbers separated by commas: ")
#nums = [float(x.strip()) for x in nums_input.split(",")]

#avg, largest, smallest, total, std_dev = analyze_list(nums)

#print("The average is:", avg)
#print("The largest number is:", largest)
#print("The smallest number is:", smallest)
#print("The sum of numbers is:", total)
#print("The standard deviation is:", std_dev)

#**************************************************************************************
#def squares_list(numbers):
#    squares = []   # قائمة فارغة لتخزين النتائج
#    for num in numbers:
#        squares.append(num ** 2)   # نضيف مربع الرقم للقائمة
#    return squares

# المستخدم يدخل الأرقام
#nums_input = input("Enter numbers separated by commas: ")
#nums = [int(x.strip()) for x in nums_input.split(",")]

#result = squares_list(nums)
#print("Original list:", nums)
#print("Squares list:", result)

#************************************************************************
#def analyze_sentence(sentence):
#    words = sentence.split()             # تقسيم الجملة إلى كلمات
#    word_count = len(words)              # عدد الكلمات
#    char_count = len(sentence)           # عدد الحروف مع المسافات
#    char_no_spaces = len(sentence.replace(" ", ""))  # عدد الحروف بدون المسافات

    # حساب عدد مرات ظهور كل كلمة
#    word_frequency = {}
#    for word in words:
#        word = word.lower()   # نخلي الكلمات كلها صغيرة لتجنب التكرار بسبب الحروف الكبيرة
#        if word in word_frequency:
#            word_frequency[word] += 1
#        else:
#            word_frequency[word] = 1

    # إيجاد أكثر كلمة متكررة
#    most_common_word = max(word_frequency, key=word_frequency.get)
#    most_common_count = word_frequency[most_common_word]

#    return word_count, char_count, char_no_spaces, word_frequency, most_common_word, most_common_count

# المستخدم يدخل جملة
#user_sentence = input("Enter a sentence: ")

#words, chars, chars_no_spaces, freq, common_word, common_count = analyze_sentence(user_sentence)

#print("The number of words is:", words)
#print("The number of characters (with spaces) is:", chars)
#print("The number of characters (without spaces) is:", chars_no_spaces)
#print("Word frequency:")
#for word, count in freq.items():
#    print(f"{word}: {count}")

#print(f"\nThe most common word is '{common_word}' appearing {common_count} times.")

#***********************************************************************************************************
#def find_min_max(numbers):
#    max_num = numbers[0]   # نبدأ بأول رقم كأكبر رقم مؤقت
#    min_num = numbers[0]   # نبدأ بأول رقم كأصغر رقم مؤقت

#    for n in numbers:      # نمر على كل رقم في القائمة
#        if n > max_num:
#            max_num = n
#        if n < min_num:
#            min_num = n

#    return max_num, min_num

# المستخدم يدخل الأرقام
#nums_input = input("Enter your numbers separated by commas: ")
#numbers = [int(x.strip()) for x in nums_input.split(",")]

#max_num, min_num = find_min_max(numbers)

#print("The max number is:", max_num)
#print("The min number is:", min_num)

#****************************************************************************
#def multiplication_table(start, end):
#    for number in range(start, end + 1):   # من الرقم الأول للرقم الأخير
#        print(f"\nMultiplication table for {number}:")
#        for i in range(1, 11):             # من 1 إلى 10
#            print(f"{number} x {i} = {number * i}")

# المستخدم يدخل البداية والنهاية
#start_num = int(input("Enter the starting number: "))
#end_num = int(input("Enter the ending number: "))

#multiplication_table(start_num, end_num)
#**************************************************************************
#students = []

# إدخال أكثر من اسم
#while True:
#    name = input("Enter student name (or type stop): ")

#    if name.lower() == "stop":
#        break

#    students.append(name)

# عرض + حذف + خروج
#while True:
#    print("\n--- Student System ---")
#    print("1. Show students")
#    print("2. Delete student by number")
#    print("0. Exit")

#    choice = input("Enter choice: ")

#    if choice == "1":
#        if not students:
#            print("No students yet.")
#        else:
#            for i, name in enumerate(students, start=1):
#                print(f"{i}. {name}")

#    elif choice == "2":
#        if not students:
#            print("Nothing to delete.")
#        else:
#           for i, name in enumerate(students, start=1):
#                print(f"{i}. {name}")

#            try:
#                num = int(input("Enter number to delete: "))
#                if 1 <= num <= len(students):
#                    removed = students.pop(num - 1)
#                    print(f"Removed: {removed}")
#                else:
#                    print("Invalid number.")
#            except ValueError:
#                print("Please enter a valid number.")

#    elif choice == "0":
#        print("Exiting...")
#        break

#    else:
#        print("Invalid choice.")

#*********************************************************************************
contacts = {}

while True:
    print("\n--- Phone Book ---")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    print("6. Edit contact")
    print("7. Count contacts")
    print("8. Delete all contacts")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name")
        if name in contacts:
            print("name already exists!")
        else:
            while True:
                phone = input("Enter 10-digit phone num:")
                if phone.isdigit() and len(phone) == 10:
                    contacts[name] = phone
                    print("contact added.")
                    break 
                else:
                    print("Invalid num!")

    elif choice == "2":
        for name, phone in contacts.items():
            print(f"{name} - {phone}")

    elif choice == "3":
        search_name = input("Enter name to search:")

        found = False
        for name in contacts:
            if name.lower() == search_name.lower():
                print("phone", contacts[name])
                found = True
                break
        if not found:
            print("contact not found!")

    elif choice == "4":
        name = input("Enter name to delete:")
        if name in contacts:
            del contacts[name]
            print("deleted successfully!")
        else:
            print("contact not found ")

    elif choice == "5":
        print("goodbuy!")
        break

    elif choice == "6":
        name = input("Enter name to edit:")
        if name in contacts:
            while True:
                new_phone = input("Enter new 10-digit num:")
                if new_phone.isdigit() and len(new_phone) == 10:
                    contacts[name] = new_phone
                    print("number updated.")
                else:
                    print("Invalid num!")

    elif choice == "7":
        print("Total contacts", len(contacts))

    elif choice == "8":
        contacts.clear()
        print("All contacts deleted")

    else:
        print("Invalid choice!")