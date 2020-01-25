import os
from zipfile import ZipFile


class b_colors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    print(f'{b_colors.OK_BLUE}create file inside your photo success!{b_colors.ENDC}\n')


def extraction():
    image_file_abs_path = input("Enter path of the image should be cover:\n")
    img_file_dir_path = os.path.dirname(image_file_abs_path)
    os.chdir(img_file_dir_path)
    ZipFile(image_file_abs_path, 'r').extractall(img_file_dir_path)
    print(f'{b_colors.OK_BLUE} extract file success!\nthe file is in the same dir of the image{b_colors.ENDC}\n')

def menu():
    case = input("Please enter your choose -\n create malicious image: 1\n extract file from image: 2\n ")
    if case == "1":
        create()
    elif case == "2":
        extraction()
    else:
        print('undefined choice\n\n')
        menu()


def main():
    menu()
    print(f'{b_colors.BOLD}bye bye!{b_colors.ENDC}')


if __name__ == "__main__":
    main()