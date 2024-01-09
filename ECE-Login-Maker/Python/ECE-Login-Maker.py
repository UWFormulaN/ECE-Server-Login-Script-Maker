import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print("Starting script maker")

WaterlooID = input("What is your Waterloo ID : ")

script = """
#!/bin/bash

echo \'Starting login Process for ECE Server as {}\'

echo -e " 
 #######                                           #     #    #######  #####  #######     #####                                     
 #        ####  #####  #    # #    # #        ##   ##    #    #       #     # #          #     # ###### #####  #    # ###### #####  
 #       #    # #    # ##  ## #    # #       #  #  # #   #    #       #       #          #       #      #    # #    # #      #    # 
 #####   #    # #    # # ## # #    # #      #    # #  #  #    #####   #       #####       #####  #####  #    # #    # #####  #    # 
 #       #    # #####  #    # #    # #      ###### #   # #    #       #       #                # #      #####  #    # #      #####  
 #       #    # #   #  #    # #    # #      #    # #    ##    #       #     # #          #     # #      #   #   #  #  #      #   #  
 #        ####  #    # #    #  ####  ###### #    # #     #    #######  #####  #######     #####  ###### #    #   ##   ###### #    #                                                                                           
"

""".format(WaterlooID)

script += "timeout 10s ssh {}@iccad5".format(WaterlooID)

script += """
read -p \'\n\n\nIf the Login didnt work make sure youve: \n
1. Inputted the right Waterloo ID \n
2. Connected to CISCO VPN \n
3. Are connected to Internet \'
"""


#Ask for output path and name
output_path = filedialog.asksaveasfilename(defaultextension=".sh", filetypes=[("Bash File", "*.sh"), ("All files", "*.*")])

#Save File
with open(output_path, 'w') as file:
    # Write the data to the file
    file.write(script)






