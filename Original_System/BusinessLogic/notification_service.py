from flask import flash

class notification_service:

    def __init__(self):
        pass

    def send_notification(self, notification_body):
        flash(notification_body, 'warning')

    def notify_acceptance(self):
        self.send_notification("Congratulations!! Your research has been accepted!")

    def notify_rejection(self):
        self.send_notification("Unfortunately your research has been rejected!")

    def notify_revision(self):
        self.send_notification("Your research needs revisions!")