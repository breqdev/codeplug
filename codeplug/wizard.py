import os
import inquirer

from codeplug.builder import BuildOptions, build_config
from codeplug.serialize import serialize

regions = os.listdir("data/repeaters")

questions = [
    inquirer.Checkbox("regions", "Which regions would you like to include?", regions),
    inquirer.List("weather", "Would you like to include weather radio? (NOAA Weather Alert and Weatheradio)", ["Yes", "No"]),
    inquirer.List("gmrs", "Would you like to include GMRS channels?", ["All", "Simplex", "Repeaters", "None"]),
    inquirer.List("frs", "Would you like to include FRS channels?", ["Yes", "No"]),
    inquirer.List("murs", "Would you like to include MURS channels?", ["Yes", "No"]),
    inquirer.List("marine", "Would you like to include Marine VHF channels?", ["Yes", "Most Common", "No"]),
]

answers = inquirer.prompt(questions)

options = BuildOptions(
    regions=answers["regions"],
    weather=(answers["weather"] == "Yes"),
    gmrs=answers["gmrs"].lower(),
    frs=(answers["frs"] == "Yes"),
    murs=(answers["murs"] == "Yes"),
    marine=("yes" if answers["marine"] == "Yes" else "starred" if answers["marine"] == "Most Common" else "no"),
)

config = build_config(options)
print(serialize(config))
