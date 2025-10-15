from .email_notification import EmailNotification
from .notification import Notification
from .notification_creator import NotificationCreator


class EmailNotificationCreator(NotificationCreator):
    """Concrete Creator"""

    def create_notification(self) -> Notification:
        return EmailNotification()
