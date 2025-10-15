from .notification import Notification
from .notification_creator import NotificationCreator
from .sms_notification import SMSNotification


class SMSNotificationCreator(NotificationCreator):
    """Concrete Creator"""

    def create_notification(self) -> Notification:
        return SMSNotification()
