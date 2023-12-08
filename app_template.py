import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

class AdvancedApp:
     def __init__(self, root):
         self.root = root
         self.root.title("Advanced Tkinter Application")

         # Create and place interface elements
         self.label = tk.Label(root, text="Select a script to execute:")
         self.label.pack(pady=10)

         # Create a drop-down list to select a script
         self.script_var = tk.StringVar()
         self.script_combobox = ttk.Combobox(root, textvariable=self.script_var, values=["script1", "script2", "script3"])
         self.script_combobox.pack(pady=10)

         # Create a button to execute the script
         self.run_button = tk.Button(root, text="Run", command=self.run_script)
         self.run_button.pack(pady=10)

         # Create a text field to display the results
         self.output_text = tk.Text(root, height=10, width=50)
         self.output_text.pack(pady=10)

     def run_script(self):
         script_name = self.script_var.get()
         if script_name:
             try:
                 result = subprocess.check_output(["python", f"{script_name}.py"], text=True)
                 self.output_text.delete(1.0, tk.END) # Clear previous output
                 self.output_text.insert(tk.END, result)
             except Exception as e:
                 messagebox.showerror("Error", f"Error executing script: {str(e)}")
         else:
             messagebox.showinfo("Warning", "Select a script to run.")

if __name__ == "__main__":
     root = tk.Tk()
     app = AdvancedApp(root)
     root.mainloop()
