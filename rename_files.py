import os
def rename_files():
    #(1) get file names from a folder
    list_path = r"C:\OOP\prank"
    file_list = os.listdir(r"C:\OOP\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    saved_path = list_path
    print("Current Working Directory is "+saved_path)

    #(2) for each file, rename filename
    for file_name in file_list:
        print(file_name)
        print(file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
        


rename_files()


os.listdir(r"C:\OOP\prank")
