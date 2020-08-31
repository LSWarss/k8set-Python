import pathlib, os, re

current_folder = pathlib.Path(__file__).parent.absolute()
fileExt = r"*.kubeconfig"

arrKubeconfigs = list(pathlib.Path(current_folder).glob(fileExt))

if (len(arrKubeconfigs) == 0):
    print("Current directory does not contains any kubeconfig files.")
else:
    print(f"Curent directory contains {len(arrKubeconfigs)} kubeconfig files in current folder")
    for i in range(len(arrKubeconfigs)):
        print(f"{i}. {arrKubeconfigs[i]}")

file_number = input("Please type here file number:")
number_regex='^[0-9]+$'

if (re.match(number_regex, file_number) == True):
    print("Please enter only numbers here")
elif(int(file_number) < 0 and int(file_number) > len(arrKubeconfigs)):
    print(f"Please select file number from range 0 and {len(arrKubeconfigs)}")
else:
    selected_kubeconfig = arrKubeconfigs[int(file_number)]

    print(f"Following kubeconfig: {selected_kubeconfig} will be set as active one")
    
    os.environ["KUBECONFIG"] = str(selected_kubeconfig)

list.clear(arrKubeconfigs)
    