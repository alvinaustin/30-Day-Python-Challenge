age=int(input("Enter Customer Age:->"))
if age<=10:
    print("Ticket fare is 1$.")
elif age<=60:
    print("Ticket fare is 3$.")
else:
    print("Entry is prohibited for citizens above the age of 60.")