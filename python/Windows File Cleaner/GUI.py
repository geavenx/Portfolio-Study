import tkinter
import customtkinter
import os
import shutil
import ctypes


class Cleaner():
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("500x350")
        self.root.title("Windows Junk Cleaner")
        self.mainframe = customtkinter.CTkFrame(master=self.root)
        self.mainframe.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(
            master=self.mainframe, text="Windows Cleaner", font=('arial', 24))
        self.label.pack(pady=12, padx=10)

        self.clean_all_field = customtkinter.CTkButton(
            master=self.mainframe, text="empty recycle bin", command=self.empty_recycle_bin, font=('arial', 18))
        self.clean_all_field.pack(pady=12, padx=10, ipadx=20)

        self.clean_temp_field = customtkinter.CTkButton(
            master=self.mainframe, text="clean temp files", command=self.clean_temp_folder, font=('arial', 18))
        self.clean_temp_field.pack(pady=12, padx=10, ipadx=20)

        self.exit_field = customtkinter.CTkButton(
            master=self.mainframe, text="exit", command=self.quit_program, font=('arial', 18))
        self.exit_field.pack(pady=12, padx=10, ipadx=20)

        self.root.mainloop()
        return

    def empty_recycle_bin(self):
        print("-- empty_recycle_bin called;\n")
        SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
        SHEmptyRecycleBin.argtypes = [
            ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int]
        SHEmptyRecycleBin.restype = ctypes.c_int

        result = SHEmptyRecycleBin(None, None, 0)
        if result == 0:
            print("Successful emptying of the recycle bin.. ")
        else:
            print(" Failed to empty Recycle Bin. ")

    def quit_program(self):
        print("-- quit_program called;\n")
        quit()

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
                print(f"Error deleting {path}: {e}")

        for file in os.listdir(temp_folder_sys):
            path = os.path.join(temp_folder_sys, file)
            try:
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)

            except Exception as e:
                print(f"Error deleting {path}, {e}")


if __name__ == "__main__":
    customtkinter.set_default_color_theme("blue")
    customtkinter.set_appearance_mode("light")
    Cleaner()
