import winreg 

sam_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SAM', 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)

try:
  i = 0
  while True:
    value = winreg.EnumValue(sam_key, i)
    print(value)
    i += 1
except OSError:
  pass
finally:
  print(winreg.CloseKey(sam_key))