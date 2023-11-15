import os

def rmdir():

  n = input("Enter dir name: ")
  path = os.path.join(os.getcwd(), n)
  os.rmdir(path)
def nofet():
  os.system("neofetch")


def cls():
  os.system("clear")


def ls():
  path = os.getcwd()
  files = os.listdir(path)
  for file in files:
    print(file)


def mkdir():

  n = input("Enter dir name: ")
  path = os.path.join(os.getcwd(), n)
  os.mkdir(path)


def main():
  print("TERMINAL CLI" + os.name + " - "  + os.getcwd())
  while True:
    command = input(f"[{__name__}/~]$ ")
    if command == "ls":
      ls()
    elif command == "exit":
      print("[localhost exited]\n./savingsession")
      break
    elif command == "":
      continue
    elif command == "mkdir":
      mkdir()
    elif command == "cls" or "clear":
      cls()
    elif command == "neofetch":
      nofet()
    else:
      print(f"ERROR: '{command}' command not found")


main()
