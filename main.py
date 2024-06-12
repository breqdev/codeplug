import os
import yaml
import csv
import inquirer

regions = os.listdir("repeaters")

questions = [
    inquirer.Checkbox("regions", "Which regions would you like to include?", regions),
    inquirer.List("weather", "Would you like to include weather radio? (NOAA Weather Alert and Weatheadio)", ["Yes", "No"]),
    inquirer.List("gmrs", "Would you like to include GMRS channels?", ["All", "Simplex", "Repeaters", "None"]),
    inquirer.List("frs", "Would you like to include FRS channels?", ["Yes", "No"]),
    inquirer.List("murs", "Would you like to include MURS channels?", ["Yes", "No"]),
    inquirer.List("marine", "Would you like to include Marine VHF channels?", ["Yes", "Most Common", "No"]),
]

answers = inquirer.prompt(questions)
