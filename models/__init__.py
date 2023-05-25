import sys
dirctory_path = r'C:\Users\HP\Desktop\alu-AirBnB_clone'
sys.path.append(dirctory_path)  # Replace with the actual path to the project directory

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Call reload() method on the storage instance
storage.reload()
