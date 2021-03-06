import os
from zipfile import ZipFile


def create():
    hidden_file_abs_path = input("Enter path of the file you want to hide:\n")
    hidden_file_name = os.path.basename(hidden_file_abs_path)
    hidden_file_dir_path = os.path.dirname(hidden_file_abs_path)

    image_file_abs_path = input("Enter path of the image should be cover:\n")
    img_file_name = os.path.basename(image_file_abs_path)
    img_file_dir_path = os.path.dirname(image_file_abs_path)

    os.chdir(hidden_file_dir_path)
    ZipFile('hd.zip', 'w').write(hidden_file_name)

    hidden_zipfile_abs_path = hidden_file_dir_path + '\hd.zip'
    os.chdir(img_file_dir_path)
    command = 'copy /b ' + img_file_name + ' + ' + hidden_zipfile_abs_path
    os.system(command)
    os.remove(hidden_zipfile_abs_path)
    print('Create file inside your photo success!\n')


def extraction():
    image_file_abs_path = input("Enter path of the image should be cover:\n")
    img_file_dir_path = os.path.dirname(image_file_abs_path)
    os.chdir(img_file_dir_path)
    ZipFile(image_file_abs_path, 'r').extractall(img_file_dir_path)
    print('extract file success!\nThe file is in the same dir of the image\n')


def menu():
    case = input("Please enter your choose:\ncreate malicious image: 1\nextract file from image: 2\n ")
    if case == "1":
        create()
    elif case == "2":
        extraction()
    else:
        print('undefined choice\n\n')
        menu()


def main():
    menu()
    print('bye bye!')


if __name__ == "__main__":
    main()