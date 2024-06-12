from dataclasses import dataclass
from typing import Literal

from codeplug.channel import Channel
from codeplug.loaders import csv_loader
from codeplug.loaders.directory_loader import load_directory

@dataclass
class BuildOptions:
    regions: list[str]
    weather: bool
    gmrs: Literal["all", "simplex", "repeaters", "none"]
    frs: bool
    murs: bool
    marine: Literal["yes", "starred", "no"]

def build_config(options: BuildOptions) -> list[Channel]:
    channels = []

    for region in options.regions:
        channels.extend(load_directory(f"data/repeaters/{region}", only_starred=(options.marine == "starred")))

    if options.weather:
        channels.extend(csv_loader.load_file("data/weather.csv"))

    if options.gmrs == "all" or options.gmrs == "repeaters":
        channels.extend(csv_loader.load_file("data/gmrs/gmrs-repeater.csv"))
    if options.gmrs == "all" or options.gmrs == "simplex":
        channels.extend(csv_loader.load_file("data/gmrs/gmrs-simplex.csv"))

    if options.frs:
        channels.extend(csv_loader.load_file("data/frs.csv"))

    if options.murs:
        channels.extend(load_directory("data/murs"))

    if options.marine != "no":
        channels.extend(csv_loader.load_file("data/marine.csv", only_starred=(options.marine == "starred")))

    return channels
