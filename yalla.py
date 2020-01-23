import os
from zipfile import ZipFile



def main():
    print('choose ')

    hidden_file_abs_path= input("Enter path of the file you want to hide:\n")
    hidden_file_name = os.path.basename(hidden_file_abs_path)
    hidden_file_dir_path = os.path.dirname(hidden_file_abs_path)

    image_file_abs_path= input("Enter path of the image should be cover:\n")
    img_file_name = os.path.basename(image_file_abs_path)
    img_file_dir_path = os.path.dirname(image_file_abs_path)



    os.chdir(hidden_file_dir_path)
    ZipFile('hd.zip','w').write(hidden_file_name)

    hidden_zipfile_abs_path= hidden_file_dir_path +'\hd.zip'
    os.chdir(img_file_dir_path)
    command = 'copy /b '+img_file_name + ' + '+hidden_zipfile_abs_path
    os.system(command)


if __name__ == "__main__":
    main()