import pathlib,os,re

current_folder = pathlib.Path(__file__).parent.absolute()
print(current_folder)

shell = os.environ['SHELL']
pattern = "k8set"

if("zsh" in shell):
    file = open("~/.zshrc", "r")
    for line in file:
        if(re.search(pattern, line) == True):
            print("Alias was installed previously, so we will remove old alias.")

# TODO: Delete the line where the alias was found


