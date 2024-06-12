from codeplug.loaders import csv_loader, yaml_loader

import os

from codeplug.channel import Channel

def load_directory(directory: str, only_starred: bool = False) -> list[Channel]:
    channels = []

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".csv"):
                channels.extend(csv_loader.load_file(os.path.join(dirpath, filename), only_starred=only_starred))
            elif filename.endswith(".yaml"):
                channels.append(yaml_loader.load_file(os.path.join(dirpath, filename)))

    return channels
