import os

file_name=input("Enter a file name: ")

while True:

    if os.path.isfile(file_name):
        choice=input("What do you want to do:\n\nA) Read the file\nB) Delete the file and start over\nC) Append the file\nD) Replace s single line\nE) Exit\n\n-> ")
        if choice=="A":
            text_content=open(file_name)
            print(text_content.read())
            text_content.close()
        if choice=="B":
            os.remove(file_name)
            text_write=input("Enter text you want to write: ")
            text_content=open(file_name,"w")
            text_content.write(text_write+"\n")
            text_content.close()
        if choice=="C":
            text_write=input("Enter text you want to write: ")
            text_content=open(file_name,"a")
            text_content.write(text_write+"\n")
            text_content.close()
        if choice=="D":
            line_number=int(input("Enter line number to update: "))
            text_write=input("Enter text you want to write: ")
            text_content=open(file_name,"r")
            text_existing=text_content.readlines()
            text_content.close()
            text_content=open(file_name,"w")
            text_existing[line_number-1]=text_write+"\n"
            for content in text_existing:
                text_content.write(content)
            text_content.close()
        if choice=="E":
            break

    else:
        text=input("Enter text you want to write: ")
        file_open=open(file_name,"w")
        file_open.write(text+"\n")
        file_open.close()
        break
