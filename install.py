import pathlib,os

current_folder = pathlib.Path(__file__).parent.absolute()
print(current_folder)

shell = os.environ['SHELL']
home = os.environ['HOME']
pattern = "k8set"

print(home)

if("zsh" in shell):
    # file = open("~/.zshrc", "r")
    # for line in file:
    #     if(re.search(pattern, line) == True):
    #         print("Alias was installed previously, so we will remove old alias.")
    with open(f"{home}/.zshrc", "r") as f:
        lines = f.readlines()
    with open(f"{home}/.zshrc", "w") as f:
        for line in lines:
            if "k8set" in line:
                f.write(line)
        f.truncate()

installation_str =f"alias k8set= python {current_folder}/k8set.py"

print(f"Alias will be installed now by adding {installation_str} to {home}/.zshrc")

if("zsh" in shell):
    with open (f"{home}/.zshrc", "w") as f:
        f.write(installation_str)
        f.close()

print("Alias has been installed.")

print("Installation complete")