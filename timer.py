import asyncio
from aioconsole import ainput
from broker import tattle, tattle_str, help, toast_it
import time


class Timer:
    def __init__(self, duration, username):
        self.minutes = duration
        self.username = username
        self.stop_reason = "UNDEFINED"
        self.stop_time = None
        self.timer_seconds = duration * 60
        self.time_start = time.time()
        self.time_end = self.time_start + self.timer_seconds

    async def time_left(self):
        seconds_left = self.time_end - time.time()
        minutes_left = seconds_left / 60
        tattle("", f"{round(minutes_left, 1)} minutes left ({int(seconds_left)} sec.)", 1)


    async def timer(self, duration):
        time_start_str = time.strftime('%H:%M:%S', time.localtime(self.time_start))
        time_end_str = time.strftime('%H:%M:%S', time.localtime(self.time_end))
        title = f"Timer started for {duration} minutes. >>> "
        message = f"It has started at {time_start_str} AND will end at {time_end_str}."
        tattle("", title, 0)
        tattle("", message, 1)
        toast_it(title, message)
        await asyncio.sleep(self.timer_seconds)
        print("TIMER ENDED")

    async def get_input(self):
        while True:
            user_input = await ainput(tattle_str(str(self.username), "[COMMAND] (help?) >>> "))
            match user_input:
                case "stop":
                    self.stop_reason = await ainput(tattle_str(str(self.username), "[REASON?] >>> "))
                    return
                case "help":
                    help()
                case "time":
                    await self.time_left()
                case "cancel":
                    self.stop_reason = "cancelled"
                    tattle("", "Quitting unconditionally!", 1)
                    return
                case "tired":
                    print("WORK IT OUT! Need to implement better methodology!!")
                case _:
                    tattle("", "Please, type 'stop' to end the timer", 1)

    async def main(self):
        duration = self.minutes
        timer_task = asyncio.create_task(self.timer(duration))
        input_task = asyncio.create_task(self.get_input())

        await asyncio.wait([timer_task, input_task], return_when=asyncio.FIRST_COMPLETED)

        finish_title = "<(-)(-)> Timer finished! "
        finish_message = ""
        if not timer_task.done():
            # If the timer task is not done, it means the input task completed first
            # So, we cancel the timer task
            timer_task.cancel()
            try:
                await timer_task
            except asyncio.CancelledError:
                if self.stop_reason == "cancelled":
                    return
                else:
                    finish_message = "Timer cancelled. The cause it: " + str(self.stop_reason)
                    tattle("", finish_message, 1)
        else:
            finish_message = "Timer finished successfully!"
            tattle("", finish_title, 1)
        toast_it(finish_title, finish_message)
        return self.time_start, self.time_end, self.stop_time, self.stop_reason

