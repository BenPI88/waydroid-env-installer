import os
os.system("clear")
print("(1) Ubuntu Install")
print("More OSses Coming Soon!")
option = input()
if option == "1":
  os.system("sudo apt install curl ca-certificates -y")
  os.system("curl https://repo.waydro.id | sudo bash")
  os.system("sudo apt install waydroid -y")
  print("\nCongrats! Waydroid is now installed on your computer!\nIf you have any issues with waydroid, check out their website over at https://waydro.id")
