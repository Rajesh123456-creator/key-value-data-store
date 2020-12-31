import os
import json
run=True
flag=False
rd={}
jkb=0
k,jsn=[],[]
dn=input("\nEnter the Directory name(EX:'DIRECTORY NAME:\FOLDER NAME\\'): ")
if not(os.path.exists(dn)):
    print("Your Directory is not exist.\nSo,the text file is Created inside the Folder named Rajeshwar in Directory 'D'.\n")
    ndn='D:\\Rajeshwar\\'
    if not(os.path.exists(ndn)):
        os.mkdir(ndn)
    dn=ndn
fln=input("Enter the Filename(EX:'FILE NAME'): ")
fn=dn+fln+".txt"
with open(fn,"w") as wf:
    pass
print("\nYour Text File",fln,"created successfully\n")
while(run):
    fs=(os.path.getsize(fn))//(1024*1024*1024)
    if(fs>1):
        print("File Size is more than 1 GB.\n")
        break
    GO=True
    while(GO):
        try:
            ch=int(input("1.Create a data store\n2.Read the data store\n\
3.Delete the data store\n4.Exit\n\nEnter your choice: "))
            GO=False
        except:
            print("Enter correct Integer Value.\n")
    if(ch==1):
            flag=True
            rnn=True
            while(rnn):
                    try:
                        key_no=int(input("Enter the number of keys you want to insert in the file "+fln+':'))
                        rnn=False
                    except:
                        print("Enter Integer value.")
            for i in range(1,key_no+1):
                Go=True
                while(Go):
                    key=input("\nEnter the key name {}: ".format(i))
                    if(len(key)<32):
                        Go=False
                    else:
                        print("The key value must be less than 32 characters.")
                k.append(key)
                rn=True
                while(rn):
                    try:
                        no=int(input("\nEnter No of fields for your key "+key+': '))
                        rn=False
                    except:
                        print("Enter Integer value.")
                raj={}
                rd[key]={}
                for j in range(no):
                    jk=input("\nEnter the json key:")
                    jv=input("Enter the json value: ")
                    raj[jk]=jv
                    json_obj=json.dumps(raj)
                    jkb=jkb+((len(json_obj.encode("utf-8")))//1024)
                    if(jkb>16):
                        print(jkb)
                        print("Your JSON object value is exceeded more than 16KB.\n")
                        break
                    rd[key][jk]=jv
                    
                jsn.append(json_obj)
                with open(fn,"a") as wf:
                    wf.write(key+"="+str(json_obj)+"\n")
            print("Your data store has been successfully created.\n")
    elif(ch==2):
        go=True
        if(flag and k):
            while(go):
                ky=input("Enter the key from the following key list {}:".format(k))
                if(ky not in k):
                    print("Your entered key is not present in the file {}.\n".format(fln))
                else:
                    go=False
            print(rd[ky],"\n")
        else:
            print("File does not contain any data store.Create the data store in {}.\n".format(fln))
    elif(ch==3):
        g=True
        if(flag and k):
            while(g):
                kyy=input("Enter the key from the following key list {}:".format(k))
                if(kyy not in k):
                    print("Your entered key is not present in the file {}.".format(fln))
                else:
                    g=False
            ix=k.index(kyy)
            k.pop(ix)
            jsn.pop(ix)
            with open(fn,"w") as wf:
                for i in range(len(k)):
                    wf.write(k[i]+"="+str(jsn[i])+"\n")
            print("Data store for Your Entered key {} is successfully deleted\n".format(kyy))
        else:
            print("File does not contain any data store.Create the data store in {}.\n".format(fln))
    elif(ch==4):
        print("EXIT")
        run=False
    else:       
        print("Enter a valid choice\n")






















