# file handling 

#  1) without using with statement 
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement 
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()

# 3) using with statement 
with open('file_path', 'w') as file:
    file.write('hello world !')

# a simple file writer object 
class MessageWriter(object):
    def __init__(self, file_name):
        self.





