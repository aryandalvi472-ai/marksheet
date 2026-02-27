name = input("Enter Student Name: ")

sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))

total = sub1 + sub2 + sub3
percentage = total *100/ 300


print("\n--- Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
