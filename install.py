import os
os.system("clear")
print("(1) Ubuntu/Debian Install")
print("(2) Fedora Install")
print("More OSses Coming Soon!")
option = input()
if option == "1":
  os.system("sudo apt install curl ca-certificates -y")
  os.system("curl https://repo.waydro.id | sudo bash")
  os.system("sudo apt install waydroid -y")
  os.system("sudo systemctl enable --now waydroid-container")
  print("\nCongrats! Waydroid is now installed on your computer!\nIf you have any issues with waydroid, check out their website over at https://waydro.id")
if option == "2":
  os.system("sudo dnf install waydroid")
  os.system("sudo systemctl enable --now waydroid-container")
  print("\nCongrats! Waydroid is now installed on your computer!\nIf you have any issues with waydroid, check out their website over at https://waydro.id\n\nSystem OTA: https://ota.waydro.id/system\nVendor OTA: https://ota.waydro.id/vendor")
