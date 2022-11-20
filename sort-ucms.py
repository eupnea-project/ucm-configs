#!/usr/bin/env python3

import os

from functions import *

if __name__ == "__main__":
    # Set verbose in functions.py
    set_verbose(True)

    # Loop through overlays
    for file in os.listdir("board-overlays"):
        if "overlay" in file:
            overlay = file.replace("overlay-", "")  # pure overlay name
            try:
                for board in os.listdir(
                        f"board-overlays/overlay-{overlay}/chromeos-base/chromeos-bsp-{overlay}/files/"):
                    if "audio-config" in board:
                        print(f"Found legacy audio config for {board}")
                        mkdir(f"upstream/{overlay}", create_parents=True)
                        cpdir(f"board-overlays/overlay-{overlay}/chromeos-base/chromeos-bsp-{overlay}/files/audio-"
                              f"config/ucm-config", f"upstream/{overlay}")
                    elif os.path.isdir(
                            f"board-overlays/overlay-{overlay}/chromeos-base/chromeos-bsp-{overlay}/files/{board}"
                            f"/audio-5_4/ucm-config"):
                        print(f"Found 5.4 audio config for {board}")
                        mkdir(f"upstream/{overlay}/{board}", create_parents=True)
                        cpdir(
                            f"board-overlays/overlay-{overlay}/chromeos-base/chromeos-bsp-{overlay}/files/{board}"
                            f"/audio-5_4/ucm-config", f"upstream/{overlay}/{board}")
                    elif os.path.isdir(f"board-overlays/overlay-{overlay}/chromeos-base/chromeos-bsp-{overlay}/files/"
                                       f"{board}/audio/ucm-config"):
                        print(f"Found normal audio config for {board}")
                        mkdir(f"upstream/{overlay}/{board}", create_parents=True)
                        cpdir(f"board-overlays/overlay-{overlay}/chromeos-base/chromeos-bsp-{overlay}/files/{board}"
                              f"/audio/ucm-config", f"upstream/{overlay}/{board}")
            except FileNotFoundError:
                print(f"Didnt find 'files' in {overlay}, skipping")
