import os
# renaming the files in the directory my_images

# folder = os.getcwd()
# rename_folder =os.path.join(files, "my_images")


files = os.listdir("D:\\my python\\my_images")


# for f in files :
#     name,ext = os.path.splitext(f)
#     print("name:" , name ,"| ext :", ext)


for i , f in enumerate(files , start = 1):
    name,ext = os.path.splitext(f)
    new_name  = (f"pic{i}{ext}")
    os.rename(os.path.join("D:\\my python\\my_images", f), os.path.join("D:\\my python\\my_images",new_name))
    print(f"{f} ----> {new_name}")

