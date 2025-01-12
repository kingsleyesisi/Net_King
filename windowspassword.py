import winreg

def read_sam_key():
  try:
    sam_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SAM', 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
    i = 0
    while True:
      try:
        value = winreg.EnumValue(sam_key, i)
        print(value)
        i += 1
      except OSError:
        break
  except OSError as e:
    print(f"Failed to open SAM key: {e}")
  finally:
    winreg.CloseKey(sam_key)
    print("SAM key closed")


if __name__ == "__main__":
  read_sam_key()