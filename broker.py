import platform
import toaster_win
import json


def tattle(who, msg, end):
    broker = Broker(who, msg, end)
    broker.msg_printer()


def tattle_str(who, msg):
    broker = Broker(who, msg, 1)
    return broker.msg_broker()


def help():
    help_text = """Available commands:
    stop - stop timer(need to write a reason with next input);
    time - on how much time left(obviously);
    cancel - as if it never happened;
    tired - how many timers done today(under rework!).
    define - new description to current timer."""
    tattle("", help_text, 1)


def toast_it(title, message):
    toaster = Toasters(title, message)
    toaster.main()


class Broker:
    def __init__(self, who, message, string_end):
        self.name = str(who)
        self.msg = str(message)
        self.end = string_end
        self.txt = ""

    def msg_handler(self):
        name = "sys.owl"
        pointer = " >>> "
        if self.name != "":
            name = "sys." + self.name
        msg = self.msg
        self.txt = name + pointer + msg

    def msg_printer(self):
        self.msg_handler()
        print(self.txt, end="" if self.end == 0 else "\n")

    def msg_broker(self):
        self.msg_handler()
        return self.txt


class Toasters:
    def __init__(self, title, message):
        self.title = title
        self.msg = message

    def notify_windows(self):
        tattle("","Windows notification on the way!", 1)
        toaster_win.toaster(self.title, self.msg)

    def notify_linux():
        tattle("", "Linux notification", 1)

    def notify_macos():
        tattle("", "MacOS notification", 1)

    def main(self):
        system = platform.system()

        if system == "Windows":
            self.notify_windows()
        elif system == "Linux":
            self.notify_linux()
        elif system == "Darwin":  # name for macOS?
            self.notify_macos()
        else:
            tattle("", "Unsupported OS to send toast!", 1)

    if __name__ == "__main__":
        main()