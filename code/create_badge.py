import argparse
import os
import time
import subprocess
from typer import Typer

app = Typer()

@app.command()
def main(firstname: str = " ",
         fullname: str = " ",
         company: str = " ",
         status: str = "Attendee",
         localpath: str = "/home/user/Documents/Badger_2040"
):
    # Set other variables
    badge_logo = "/badges/BadgeLogo.jpg"
    badge_file = os.path.join(localpath, "code/badge.txt")
    badge_image = os.path.join(localpath, "images/BadgeLogo.jpg")
    serial_port = "/dev/ttyACM0"


    # Write the information to a file called badge.txt
    with open(badge_file, "w") as f:
        f.write(f"{status}\n"
                f"{firstname}\n"
                f"{fullname}\n\n"
                f"{company}\n\n"
                f"{badge_logo}"
        )

    # Wait for the Badger 2040 board to be ready
    time.sleep(2)

    # Transfer the files to the Badger 2040 board
    subprocess.run(['rshell', '-p', 
                    serial_port, 
                    'cp', 
                    badge_file, 
                    badge_image, 
                    '/badges'])
