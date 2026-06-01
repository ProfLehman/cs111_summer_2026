# ------------------------------------------------------------
#     Program: sales_count_controlled_loop.py
#      Author: Lehman
#        Date: spring 2026
#
# Description: Enter x13 sales amounts
#              The program will:
#                - calculate the total number sold
#                - find the highest sales amount
#                - store the name of the top seller
# ------------------------------------------------------------
total = 0

high_number = -1
high_name = "unknown"

t = 1
while t <= 13:
    
    sold = int( input(f"enter number sold: ") )
    
    # update totals
    total = total + sold
    
    # update high sale
    if sold > high_number:
        high_number = sold
        high_name = input("Enter name: ")
    
    t = t + 1

    # end loop

print()
print()
print( "total sold = ", total)
print( "most sold = ", high_number)
print( "high seller = ", high_name)

