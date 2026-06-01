
# project_list.py
# spring 2026
# prof. lehman
#
# two parallel lists example
# sample list processing creates a list of projects
# and a list with minutes to complete project
#

# index        0              1            2        3       4      
project = ["cs111 p4", "storyboarding", "paper", "sleep", "study"]
minutes = [   45,          300,           120,    60,      200 ]

print( project[ 1 ] ) #??? storyboarding
print()
print()

# display all projects and minutes
i = 0
while i < len( project ):
    
    print( f"project: {project[ i ]}, time: {minutes[ i ]} minutes" )
    
    i = i + 1
    
print()
print()

print("number of projects: ", len(minutes) )

hours = sum(minutes) / 60
print("total time for projects: ", hours, " hours" )
print()

# display the name of the shortest project
short = min(minutes)
print("shortest project: ", short  )

i = 0
while i < len( project ):
    
    if minutes[ i ] == short:
        print( f"shortest project is {project[ i ]}, time is {minutes[ i ]} minutes" )
    
    i = i + 1
    
print()




