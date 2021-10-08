import math

#Question 1
def  compute_pi(n): #computing pi from the user
    #intializing the variables
    num=1
    pi=0
    for z in range(n):
        denom= 2*z+1 #calculating the denominator
        if z % 2 == 0 : # if its an even number
         pi+= (num/denom)
        else: #if its an odd number
            pi-=(num/denom)
    pi *=4
    return pi

#Question 2
def compute_sqrt(x): # omputing the square root of a number
    last =1
    for z in range(10): # the loop has to repeat 10 times
        next = 0.5 * (last + x / last) #the formula to get the next guess from the last guess
        last=next # computes the square root
    return last # returns the square root

#Question 3
def is_primes(n): # computing a prime number
    for z in range(2,n):
        if n  % z  ==0:  #??????????????????
            return False
    return True

def display_primes(n): #displaying the prime number less thaan or equal to n
    for z in range(2, n):
        if is_primes(z)== True: # calling the helper function
            print("Primes numbers =", z)# printing the prime numebrs

#Question 4
def  process_scores( ):
        storeNames = []
        storeScores = []
        totalScore = 0
        minScore = 999
        maxScore = -1
        minName = ""
        maxName = ""
        while (True):  # the while function to repeat the user to enter the Student name and score
            # The user enters the Student Info
            name = input("Enter the Students name and and Score(press space before entering score) and q to Quit:")
            # Breaking out the loop after entering quit
            if name == 'q' or name == 'Q':
                break
            else:
                tempName, tempScore = name.split()#spliting the name and score
                tempScore = int(tempScore) #calling the score as integer
                #Appending to enter the list
                storeNames.append(tempName)
                storeScores.append(tempScore)


        for x in range(len(storeScores)):
            #Get the minimum score from the user
            if storeScores[x] < minScore:
                minScore = storeScores[x]
                # getting the student name who has the minimum score
                minName = storeNames[x]
                #Get the
            if storeScores[x] > maxScore:
                maxScore = storeScores[x]
                maxName = storeNames[x]

            totalScore = totalScore + storeScores[x]

        print("The minimum Value is : ", minScore)
        print("The maximum Value is : ", maxScore)
        print("The Average Score is : ", totalScore / len(storeScores))

        print("The Student who has the Maximum score is: ", maxName)
        print("The Student who has the Minimum Score is: ", minName)








#Question 5
def  compute_tax(income, status, state):
    income= int(income)
    if state =='i' or state == 'I':
        if status =="single" or status =="SINGLE":
            if income < 30000:
                taxRate =0.20 * income
            elif income >= 30000:
                taxRate= 0.25 * income
        elif status =="married" or status=="MARRIED":
            if income < 50000:
                taxRate= 0.10 * income
            elif income >=50000:
                taxRate= 0.15 * income
    elif state=='o'or state =='O':
        if status == "single" or status == "SINGLE":
            if income < 30000:
                taxRate = 0.17 * income
            elif income >= 30000:
                taxRate = 0.22 * income
        elif status == "married" or status == "MARRIED":
            if income < 50000:
                taxRate = 0.07 * income
            elif income >= 50000:
                taxRate = 0.12 * income
    return taxRate

#Question 6
def solve_quadratic(a,  b, c):
    formula= b *b - 4 * a * c # the formula if there are solutions
    sqrt= math.sqrt(abs(formula))
    if formula <0:
        return 0
    else:
        solution1= float((-b + sqrt(b * b -4* a * c))/ 2 * a)
        solution2 = float((-b + sqrt(b * b - 4 * a * c)) / 2 * a)

#Question7
def sort(list):
    list=[12,33,0,5,13]
    for i in range (len(list)):
        min=i
        for j in range(i+1, len(list)):
            if list[min]> list[j]:
                min=j


    list[i],list[min]= list[min], list[i]

    return list

#Question8
def id_password(first, last):
    userName= first[0] + last #User ID is the first letter of the first name followed by last name
    print(userName.upper()) #username works
    #size= first[-1] # The size to ge the last letter
    # the first and last letter of the first name and the first three letters of the last name
    # the length of the first and last name
    passWord= len(first)+len(last)

    #print(first[0, size-1] + last[0:3])
    print("Length" , len(first), len(last)) # works
    print("FIRST: ", first[0:-1])
    print("LAST:", last[0:3])
    #passWord= first[0, size] + last[0:3] +len(first)+len(last)
    #print(passWord.upper())

    return userName.upper(), passWord.upper()



#Question 9
def file_sort(infile, outfile):
    readFile= open("student.txt", "r")
    numOfStudents = int(readFile.readLine())
    info=[]
    count=0

    for line in readFile:
        info.append(line.split())
    readFile.close()

    for z in range(numOfStudents):
        for x in range(numOfStudents -z):
            if int (info[x][0])> int(info[x+1][0]):
                info[x], info[x+1]= info[x+1], info[x]

    writeFile= open(outfile, 'w')
    writeFile.write(str(numOfStudents))
    for i in range(numOfStudents):
        writeFile.write()

    writeFile.close()

def main():#main Menu to choose the options from
    print("WELCOME TO PYTHON PROGRAMMING")
    choice=0
    print("\n1- Computing PI\n")
    print("2- Computing Square Root\n")
    print("3- Displaying Primes\n")
    print("4- Processing Grades\n")
    print("5- Computing tax\n")
    print("6- Solving Quadratic\n")
    print("7- Sort Numbers\n")
    print("8- Student Information\n")
    print("9- Sorting File\n")
    print("10- QUIT\n")
    choice = input("Enter the menu: ")
    while(choice !='10'):

        if choice =='1':
           num= int(input("Enter the number to compute PI: "))
           print(compute_pi(num))

        if choice =='2':
            num= int(input("Enter the number to find the square root: "))
            print(compute_sqrt(num))

        if choice =='3':
            num= int(input("Enter the number to find the prime: "))
            display_primes(num)

        if choice=='4':
            process_scores()

        if choice =='5':
            income=input("Enter the income:")
            status= input("Enter the marital status 'single or married': ")
            state=input("Enter the residency (i= instate or o= out of state): ")
            total= compute_tax(income, status, state)

            total_float= "{:.2f}".format(total)
            print("Tax amount is ", total_float)
        if choice == '6':
            print("Enter the 3 values for the quadratic function")
            a= int(input("Enter a: "))
            b= int(input("Enter b: "))
            c= int(input ("Enter c: "))

            if a==0:
                print("Cannot be a non-zero value: ")
            else:
                q= solve_quadratic(a,  b, c)
                if q==0:
                    print("The equation has no roots")
                else:
                    print("The equation has root ",q)

        if choice == '7':
            print("Sorted Array" )
            for i in range(len (sort(list))):
                print(sort(list))

        if choice == '8':
            first= input("Enter your first name: ")
            last= input ("Enter your last Name: ")
            print(id_password(first, last))


        print("\n1- Computing PI\n")
        print("2- Computing Square Root\n")
        print("3- Displaying Primes\n")
        print("4- Processing Grades\n")
        print("5- Computing tax\n")
        print("6- Solving Quadratic\n")
        print("7- Sort Numbers\n")
        print("8- Student Information\n")
        print("9- Sorting File\n")
        print("10- QUIT\n")
        choice = input("Enter the menu: ")

main()






