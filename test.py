import configparser

config = configparser.ConfigParser()
config.read("config.ini")

username = input("Enter your username: ")
config["DEFAULT"]["username"] = username

with open("config.ini", "w") as f:
    config.write(f)
