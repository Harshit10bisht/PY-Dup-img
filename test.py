import sys
import datatime

time = datetime.datetime.now()

output = "Hi % my name is Harshit Bisht and time is %" % (sys.argv[1],time)

print(output)