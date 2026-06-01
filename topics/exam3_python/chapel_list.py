# chapel_list.py
# spring 2026
# prof. lehman
#
# sample list processing creates a list of student id's (huid)
# and student chapel credits (credit)
#

# Option #1 - creating parallel empty lists

# huid (huntington id)
huid = [] #empty

# chapel credits
credit = [] #empty

print( "Empty lists ..." )
print( "HU id: ", huid )
print( "Chapel Credits: ", credit )
print()
print()


# Option #2 - start with sample entries and append new entries
#            0       1
huid =   ["s222", "s333"] #two entries
credit = [32,      25] 

huid.append("s111")
credit.append( 28 )

print( "Three items in lists ...")
print( "HU id: ", huid )
print( "Chapel Credits: ", credit )
print()
print()


# Option #3 - use sentinel loop to add additional students
print("Add additional data ...")

new_id = input('Enter HUID "Done" to quit: ')

while new_id != "Done":

    # add huid to list
    huid.append( new_id )
    
    # ask for chapels and add to credit list
    new_credit = int( input("Enter #chapels: ")  )
    credit.append( new_credit )
    
    new_id = input('Enter HUID "Done" to quit: ')
    # go up to while

print()
print( "Current items in list ...")
print( "HU id: ", huid )
print( "Chapel Credits: ", credit )
print()
print()


print( "Number of students: ", len( huid ) )
print( "Total credits for all HU students: ", sum( credit ) )
print()
print( "Most credits: ", max( credit ) )
print( "Least credits: ", min( credit ) )
print()

avg = sum(credit)/len(credit)
print( "Average credits: ", avg )
print()

print( "first student in list", huid[0], credit[0] )
print( "last student in list", huid[-1], credit[-1] )
print( )
print( )




# uncomment to use sample data rather than previous lists
# huid =  ['s222', 's333', 's111', 's444', 's555', 's666', 's777', 's888', 's999']
# credit = [32, 25, 18, 33, 37, 18, 15, 14, 26]

# show all items in list one at a time
print( "huid => # chapels" )
i = 0
while i < len( huid ):
    
    print( f"Student ID: {huid[i]} => {credit[i]} chapels" )
    
    i = i + 1
    # end while
    
print()
print()

# process items in list
low = 0
done = 0

i = 0
while i < len(huid):
    
    # count number of students with less than 25 chapels
    if credit[ i ] < 25:
#        print( "low: ", huid[ i ], credit[ i ] )
        low = low + 1

    # count number of students with 30+ chapels
    if credit[ i ] >= 30:
#        print( "high: ", huid[ i ], credit[ i ] )
        done = done + 1

    i = i + 1

print("        Students with 30+ chapels  :-) ", done )
print("Students with less than 25 chapels :-( ", low )







