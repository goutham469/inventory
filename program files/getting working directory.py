import os
file_name = str(os.getcwd())
print("original file -->",file_name)
l=[]
for i in range(len(file_name)):
    if file_name[i] == '\\' :
        l.append('/')
    else :
        l.append(file_name[i])
l.append('/')
l.append("billings/")
name = customer_details[0]
l.append(name)

l = "".join(l)
print("file name :",l)
with open (l,"w") as f :
    f.write("hello its the file")

