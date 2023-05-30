import os
import shutil
import ctypes
import time


class Cleaner():
    def __init__(self):
        while True:
            self.clean_temp_folder()
            time.sleep(1800)

    def clean_temp_folder(self):
        print("-- clean_temp_folder called;\n")
        temp_folder_user = os.environ['TEMP']
        temp_folder_sys = 'C:\windows\TEMP'

        for file in os.listdir(temp_folder_user):
            path = os.path.join(temp_folder_user, file)

            try:
                if os.path.isfile(path):
                    os.remove(path)
                    print(f"{path} deleted")
                else:
                    shutil.rmtree(path)
                    print(f"{path} deleted")

            except Exception as e:
                pass  # print(f"Error deleting {path}: {e}")

        for file in os.listdir(temp_folder_sys):
            path = os.path.join(temp_folder_sys, file)
            try:
                if os.path.isfile(path):
                    os.remove(path)
                    print(f"{path} deleted")
                else:
                    shutil.rmtree(path)
                    print(f"{path} deleted")

            except Exception as e:
                pass  # print(f"Error deleting {path}, {e}")


if __name__ == "__main__":
    Cleaner()
