from .email_notification import EmailNotification
from .notification import Notification
from .push_notification import PushNotification
from .sms_notification import SMSNotification


class SimpleNotificationFactory:
    """Simple Factory Pattern"""

    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        notification_type = notification_type.upper()

        if notification_type == "EMAIL":
            return EmailNotification()
        elif notification_type == "SMS":
            return SMSNotification()
        elif notification_type == "PUSH":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")
