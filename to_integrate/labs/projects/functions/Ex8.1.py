########################################################
# Insert your TIMER FUNCTIONS here

#

start_timer()  # noqa: F821
lines = 0
for row in open ("words"):
    lines += 1
    
end_timer()  # noqa: F821
print ("Number of lines:",lines)