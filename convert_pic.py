from PIL import Image
import os
import math

def input_path(file_path_list):
    while True:
        tmp = str(input()).strip()
        if tmp.upper() == "END":
            break
        else:
            file_path = "//".join(tmp.split("\\"))
            file_path_list.append(file_path)

def creating_folder(folder):
    try:
        os.mkdir(folder)
        print(f"=> Creating folder '{folder}' successfully.")
    except FileExistsError:
        print(f"=> Directory '{folder}' already exists.")
    except Exception as e:
        print(f"=> An error occurred: {e}")


def converting_files(file_path, store_folder, options, crop_option):
    filename = str(os.path.basename(file_path))
    if options == "WEBP": #WEBP
        if crop_option == "Y":
            try:
                img = Image.open(file_path)
                W, H = img.size
                tile = 1024

                cols = math.ceil(W / tile)
                rows = math.ceil(H / tile)

                for r in range(rows):
                    for c in range(cols):
                        left = c * tile
                        upper = r * tile
                        right = min(left + tile, W)
                        lower = min(upper + tile, H)

                        tile_img = img.crop((left, upper, right, lower))
                        tile_img.save(os.path.join(store_folder, filename.split(".")[0] + "_{}_{}.webp".format(r, c)), format="WEBP", quality=90)

                print("=> Converting successfully the file: {}".format(filename))
            except Exception as e:
                print(f"=> An error occurred: {e}")
        else:
            try:
                img = Image.open(file_path)
                img.save(os.path.join(store_folder, filename.split(".")[0] + ".webp"), format="WEBP", quality=90)
                print("=> Converting successfully the file: {}".format(filename))
            except Exception as e:
                print(f"=> An error occurred: {e}")
    elif options == "JPG": #JPG
        try:
            img = Image.open(file_path)
            img.save(os.path.join(store_folder, filename.split(".")[0] + ".jpg"), format="JPEG", quality=90)
            print("=> Converting successfully the file: {}".format(filename))
        except Exception as e:
            print(f"=> An error occurred: {e}")
    elif options == "PNG": #PNG
        try:
            img = Image.open(file_path)
            img.save(os.path.join(store_folder, filename.split(".")[0] + ".png"), format="PNG", optimize=True)
            print("=> Converting successfully the file: {}".format(filename))
        except Exception as e:
            print(f"=> An error occurred: {e}")
    elif options == "BMP": #BMP
        try:
            img = Image.open(file_path)
            img.save(os.path.join(store_folder, filename.split(".")[0] + ".bmp"), format="BMP")
            print("=> Converting successfully the file: {}".format(filename))
        except Exception as e:
            print(f"=> An error occurred: {e}")
    elif options == "TIFF": #TIFF
        try:
            img = Image.open(file_path)
            img.save(os.path.join(store_folder, filename.split(".")[0] + ".tiff"), format="TIFF")
            print("=> Converting successfully the file: {}".format(filename))
        except Exception as e:
            print(f"=> An error occurred: {e}")
    elif options == "GIF": #GIF
        try:
            img = Image.open(file_path)
            img.save(os.path.join(store_folder, filename.split(".")[0] + ".gif"), format="GIF")
            print("=> Converting successfully the file: {}".format(filename))
        except Exception as e:
            print(f"=> An error occurred: {e}")
    elif options == "ICO": #ICO
        try:
            img = Image.open(file_path)
            img.save(os.path.join(store_folder, filename.split(".")[0] + ".ico"), format="ICO", sizes=[(16,16), (32,32), (48,48), (64,64)])
            print("=> Converting successfully the file: {}".format(filename))
        except Exception as e:
            print(f"=> An error occurred: {e}")
    else:
        print("Option's not available. Pls try again")
    return 

def processing(choice, format):
    choice = int(choice)
    format_options = str(format[0]).upper()
    crop_option = ""

    if len(format) == 2: 
        crop_option = str(format[1]).upper()

    if choice == 1:
        folder_path_list  = list()
        print("Enter folder path you want to convert: (Ex: D:\My\Cat\Pics)")
        print("Note: You can finish your input by typing 'end'")

        input_path(folder_path_list)

        for folder_path in folder_path_list:
            try:
                folder = os.listdir(folder_path)
            except Exception as e:
                print(f"=> An error occurred: {e}")

            print("--------------- Creating folders ---------------")
            # Creating folder storing converted format pictures
            result_folder = folder_path + "//{}".format(format_options)
            creating_folder(result_folder)
            print()

            print("--------------- Converting files ---------------")

            # Converting pictures format
            for file_path in folder:
                absolute_file_path = os.path.join(folder_path, file_path)

                # Skip sub folders
                if not os.path.isfile(absolute_file_path):
                    continue

                #Converting pictures
                converting_files(file_path=absolute_file_path, 
                                 store_folder=result_folder, 
                                 options=format_options, 
                                 crop_option=crop_option)

            print()
        menu()

    elif choice == 2:
        file_path_list  = list()
        print("Enter file path you want to convert: (Ex: D:\My\Cat\Pics\Mimi.jpg)")
        print("Note: You can finish your input by typing 'end'")

        input_path(file_path_list)
        
        for file_path in file_path_list:
            folder_path = os.path.dirname(file_path)

            print("--------------- Creating folders ---------------")
            # Creating folder storing converted format pictures
            result_folder = folder_path + "//{}".format(format_options)
            creating_folder(result_folder)
            print()

            print("--------------- Converting files ---------------")

            #Converting pictures
            converting_files(file_path=file_path, 
                             store_folder=result_folder,
                             options=format_options, 
                             crop_option=crop_option)

            print()

        print()
        menu()

    else:
        menu()

def format_menu():
    print("---------------> FORMAT MENU <---------------")
    print("1. WEBP")
    print("2. JPG")
    print("3. PNG")
    print("4. BMP")
    print("5. TIFF")
    print("6. GIF")
    print("7. ICO")
    print("0. Back to menu")

    try:
        choice = int(input("Your choices: "))
    except Exception as e:
        print(e)
        format_menu()
    
    if choice == 1:
        while True:
            choice1 = str(input("You want to crop the image? (Y (Yes) or N (No): ")).upper()
            if choice1 == "Y" or choice1 == "YES":
                return ["WEBP", "Y"]
            elif choice1 == "N" or choice1 == "NO":
                return ["WEBP", "N"]
            else:
                print("Your choice is not available. Pls try again.")

    elif choice == 2:
        return ["JPG"]
    elif choice == 3:
        return ["PNG"]
    elif choice == 4:
        return ["BMP"]
    elif choice == 5:
        return ["TIFF"]
    elif choice == 6:
        return ["GIF"]
    elif choice == 7:
        return ["ICO"]
    elif choice == 0:
        return 0
    else:
        print("Your format choice is not available. Pls try again!")
        format_menu()

def menu():
    print("---------------> MENU <---------------")
    print("1. Convert all files in the folder")
    print("2. Convert separate file")
    print("0. Exit")
    try:
        choice = int(input("Your choices: "))
    except Exception as e:
        print(e)
        menu()

    if choice == 1:
        format_options = format_menu()
        if format_options == 0:
            menu()
            return
        processing(1, format= format_options)
    elif choice == 2:
        format_options = format_menu()
        if format_options == 0:
            menu()
            return
        processing(2, format= format_options)
    elif choice == 0:
        return
    else:
        print("Your choice is not available. Pls try again!")
        menu()

def main():
    menu()
    
main()