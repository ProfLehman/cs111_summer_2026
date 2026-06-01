# ------------------------------------------------------------
#     Program: sales_sentinel_loop.py
#      Author: Lehman
#        Date: spring 2026
#
# Description: Repeatedly enter sales amounts until -1 is entered.
#              The program will:
#                - calculate the total number sold
#                - find the highest sales amount
#                - store the name of the top seller
# ------------------------------------------------------------

total = 0

high_number = -1
high_name = "unknown"

sold = int( input(f"enter number sold (-1 to quit): ") ) # prime loop
while sold != -1:
    
    # add to total
    total = total + sold
 
    # update high sale
    if sold > high_number:
        high_number = sold
        high_name = input("Enter name: ")
 
    # get next sale
    sold = int( input(f"enter number sold (-1 to quit): ") )

    # end loop goes up to line with "while"

print()
print()
print( "total sold = ", total)
print( "most sold = ", high_number)
print( "high seller = ", high_name)

