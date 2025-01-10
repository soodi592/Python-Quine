import os
import subprocess
import sys

#    ███████╗ ██████╗  ██████╗ ██████╗ ██╗███████╗ █████╗ ██████╗ 
#    ██╔════╝██╔═══██╗██╔═══██╗██╔══██╗██║██╔════╝██╔══██╗╚════██╗
#    ███████╗██║   ██║██║   ██║██║  ██║██║███████╗╚██████║ █████╔╝
#    ╚════██║██║   ██║██║   ██║██║  ██║██║╚════██║ ╚═══██║██╔═══╝ 
#    ███████║╚██████╔╝╚██████╔╝██████╔╝██║███████║ █████╔╝███████╗
#    ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝╚══════╝ ╚════╝ ╚══════╝

# Read and print the current file's contents
print(open(__file__).read())

# Set variables
num = os.path.basename(__file__)
number = num[:4]  # Get the first four characters of the filename

# Define the new file name
# Ensure that the first three characters can be incremented numerically
new_number = str(int(number) + 1).zfill(4)  # Increment and ensure it's 4 digits (e.g., '0002' from '0001')
new_file_name = new_number + "quine" + ".py"  # Combine the incremented number with "quine.py"

# Write the current file's content into the new file
with open(new_file_name, "w") as file:
    file.write(open(__file__).read())

# Print the name of the file created
print(f"Created file: {new_file_name}")

# Ensure the file is created and accessible, then run it
try:
    # Use sys.executable to get the correct Python interpreter (e.g., python3)
    subprocess.run([sys.executable, new_file_name], check=True)
    print(f"Successfully executed {new_file_name}")
except subprocess.CalledProcessError as e:
    print(f"Error executing the file {new_file_name}: {e}")
except FileNotFoundError:
    print(f"The file {new_file_name} was not found.")
