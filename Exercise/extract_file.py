file_path = input().split("\\")

name, extension = file_path[-1].split(".")

print(f"File name: {name}\n"
      f"File extension: {extension}")
