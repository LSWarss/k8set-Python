import pathlib
import os

current_folder = pathlib.Path(__file__).parent.absolute()
shell = os.environ['SHELL']
home = os.environ['HOME']
pattern = "k8set"

if("zsh" in shell):
    with open(f"{home}/.zshrc", "r") as f:
        lines = f.readlines()
    with open(f"{home}/.zshrc", "w") as f:
        for line in lines:
            if "k8set" not in line:
                f.write(line)
        f.truncate()
elif("bash" in shell):
    if(os.path.isfile(f"{home}/.bash_profile")):
        with open(f"{home}/.bash_profile", "r") as f:
            lines = f.readlines()
        with open(f"{home}/.bash_profile", "w") as f:
            for line in lines:
                if "k8set" not in line:
                    f.write(line)
            f.truncate()
    elif(os.path.isfile(f"{home}/.bashrc")):
        with open(f"{home}/.bashrc", "r") as f:
            lines = f.readlines()
        with open(f"{home}/.bashrc", "w") as f:
            for line in lines:
                if "k8set" not in line:
                    f.write(line)
            f.truncate()

installation_str = f"alias k8set='python {current_folder}/src/k8set.py'"

if("zsh" in shell):
    print(f"Alias will be installed now by adding {installation_str} to {home}/.zshrc")
    with open (f"{home}/.zshrc", "a") as f:
        f.write(installation_str)
        f.close()
elif("bash" in shell):
    if(os.path.isfile(f"{home}/.bash_profile")):
        print(f"Alias will be installed now by adding {installation_str} to {home}/.bash_profile")
        with open (f"{home}/.bash_profile", "a") as f:
            f.write(installation_str)
            f.close()
    elif(os.path.isfile(f"{home}/.bashrc")):
        print(f"Alias will be installed now by adding {installation_str} to {home}/.bashrc")
        with open (f"{home}/.bashrc", "a") as f:
            f.write(installation_str)
            f.close()


print("Alias has been installed.")

print("Installation complete")