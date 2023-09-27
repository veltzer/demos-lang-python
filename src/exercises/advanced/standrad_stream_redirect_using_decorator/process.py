




@redirect_output_to("out.txt")
def function():
    print("hello")
    print("goodbye")

print("hello") # <- this is to go to the screen
function() # because of the decorator - all the output of the function should go to out.txt
print("hello") # <- this to go to the screen
