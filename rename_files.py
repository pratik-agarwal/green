import os
def rename_files():
    file_list = os.listdir(r"D:\Python\prank")
    print (file_list)
    old_path = os.getcwd()
    os.chdir(r"D:\Python\prank")
    for file_name in file_list:
        print ("old Name:" +file_name)
        print ("New Name:" +file_name.translate(None,"0987654321"))
        os.rename(file_name,file_name.translate(None,"0987654321"))

rename_files()

