#process of handling files
#read-read(),if a file is opened in read method but the file doesn't exist,it throws an error
# write in file-write(),if a file is opened in write method but the file doesn't exist,it creates an empty file
#file handling flow
#1.open the file-open()
#2.perform operations in file
#3.close the file

#JSON-JS OBJECT NOTATION,SIMILAR TO DICTIONARY
# file=open('abc.txt','w')
# file.write("A")
# file.close()

# file=open('abc1.txt','a')
# file.write("Sma Ale")
# file.close()

# file=open('abc1.txt','a')
# file.write("[1,2,3,4]")#only string can be written
# file.close()

file=open('abc1.txt','r')
content=file.read()
file.close()
print(content)

#split function:
# print(content.split("-"))
listcontent=content.split("-")
for i in listcontent:
    print(i)