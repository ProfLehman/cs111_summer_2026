# input
gpa = 2.89
rate = 3.45
age = 18
name = "Norman"


#output without formatting
print("gpa is", gpa)
print("rate is", rate)
print("age is", age)
print("name is", name)
print( 10 / 3 )
print()

# format str variables
print( f"Name is {name}" )
print()

# format int variables
print( f"age is {age} years old" )
print( f"age is {age:b} years old in binary" )
print( f"age is {age:X} years old in hex" )
print()

# format with two place holders
print( f"{name} is {age} years old" )
print()


# format float\
gpa = 3.4567
print( f"gpa is {gpa}" )
print( f"gpa is {gpa:.1f}" )
print( f"gpa is {gpa:.3f}" )
print()

temp = 10 / 3
print( f"{temp:.1f}")
print( f"{10/3:.1f}" ) #place math operation in f-string
print()


# format as currency with commas
total = 5678.178
print( "Total is $", total ) # without format
print( f"Total is ${total:,.2f}" ) #with formatting
print()


# alternate approach - store formatted string, then print
msg = f"Pay = ${total:,.2f}"
print( msg )