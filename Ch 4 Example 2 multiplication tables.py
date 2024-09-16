#Program name: Chapter 4 Example 2 multiplication tables.py
#prints the times tables from 2 to 10

for table in range(2,11):
    print("\n",table," Times Table ")
    for i in range(2,13):
        print (table," x ",i," = ",(table * i))

input("\nPress Enter to continue ")
