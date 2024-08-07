import os
import time
import configparser
from timer import Timer
import asyncio
from broker import tattle, tattle_str
import csv
import argparse
import json


config = configparser.ConfigParser()

username = ""


def configurator():
    if os.path.exists("config.ini"):
        tattle("", "Config: OK >> ", 0)
        config.read("config.ini")
        if "username" in config["DEFAULT"]:
            global username
            username = config["DEFAULT"]["username"]
            print("You logged in as > " + username)
    else:
        tattle("", "Config file was not found! Creating one", 1)
        create_config()


def create_config():
    with open("config.ini", "w") as f:
        username_input = input(tattle_str("", "Enter your username: "))
        config["DEFAULT"]["username"] = username_input
        config.write(f)
    configurator()

def save_csv(desc, start, end, stop, reason):
    header = ["Description", "Date", "Time of start", "Time of finish", "Time if stopped", "Reason"]
    line = [
        desc,
        time.strftime('%Y-%m-%d', time.localtime(start)),
        time.strftime('%H:%M:%S', time.localtime(start)),
        time.strftime('%H:%M:%S', time.localtime(end)),
        time.strftime('%H:%M:%S', time.localtime(stop)),
        reason
    ]

    if os.path.exists("log.csv"):
        with open("log.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(line)
            f.close()
            tattle("", "Data save in existing file", 1)
    else:
        with open("log.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(line)
            tattle("", "Data save in a new file", 1)

    return header, line


def send_to_server(header, line):
    # COMPLETE IT LATER
    data = {
        header[0]: line[0],
        header[1]: line[1],
        header[2]: line[2],
        header[3]: line[3],
        header[4]: line[4],
        header[5]: line[5]
    }




def main(time, desc):
    minutes = time
    desc = desc
    configurator()
    timer = Timer(minutes, username)
    start, end, stop, reason = asyncio.run(timer.main())
    header, line = save_csv(desc, start, end, stop, reason)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="Number of minutes")
    parser.add_argument("description", type=str, nargs="+", help="Description of timer")

    args = parser.parse_args()

    main(args.number, ' '.join(args.description))
