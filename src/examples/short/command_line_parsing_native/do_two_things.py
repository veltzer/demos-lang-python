import sys

if sys.argv[1] == "say_hello":
    print("hello")
    sys.exit(0)
if sys.argv[1] == "say_goodbye":
    print("goodbye")
    sys.exit(0)
print("I donno what you want from me...")
