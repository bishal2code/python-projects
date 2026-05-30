import os

folder = r"C:\Users\bisha\OneDrive\Desktop\Check"
file_types = "text"

for i, filename in enumerate(os.listdir(folder), start=1):
    ext = os.path.splitext(filename)[1]
    new_name = f"{file_types}_{i}{ext}"

    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)

print("Renaming completed!")