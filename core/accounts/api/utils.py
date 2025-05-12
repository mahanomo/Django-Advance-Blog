from threading import Thread


# custom thread
class EmailThread(Thread):
    # constructor
    def __init__(self, email_obj):
        # execute the base constructor
        Thread.__init__(self)
        # set a default value
        self.email_obj = email_obj

    # function executed in a new thread
    def run(self):

        self.email_obj.send()
