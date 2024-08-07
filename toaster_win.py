from winotify import Notification, audio


def toaster(title, msg):
    toast = Notification(app_id="LittleOwl",
                         title=title,
                         msg=msg,
                         duration="long")
    toast.show()


