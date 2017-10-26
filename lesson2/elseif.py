grade_percentage = int(raw_input("Please enter your numerical grade: "))

if grade_percentage < 50:
    print "F"
elif grade_percentage < 60:
    print "D"
elif grade_percentage < 70:
    print "C"
elif grade_percentage < 80:
    print "B"
else:
    print "A"
