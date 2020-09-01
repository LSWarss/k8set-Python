import pathlib, os, re, glob
import subprocess

# TODO: Correct this path to take path where the script is trigger
current_folder = pathlib.Path(__file__).parent.absolute()
arrKubeconfigs = glob.glob('*.kubeconfig') #It looks in current directory for files with extension kubeconfig and creates list of them

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
        
        os.environ["KUBECONFIG"] = str(current_folder) + "/" + selected_kubeconfig
        kubeconfig = os.environ["KUBECONFIG"]

        # TODO: After correcting the path try out without and with subprocess.call() getting the export to work

list.clear(arrKubeconfigs)
    