from .email_notification import EmailNotification
from .push_notification import PushNotification
from .sms_notification import SMSNotification


class NotificationServiceNaive:
    """Naive implementation without factory pattern (anti-pattern)"""

    def send_notification(self, notification_type: str, message: str) -> None:
        if notification_type == "EMAIL":
            email = EmailNotification()
            email.send(message)
        elif notification_type == "SMS":
            sms = SMSNotification()
            sms.send(message)
        elif notification_type == "PUSH":
            push = PushNotification()
            push.send(message)
        else:
            print(f"Unknown notification type: {notification_type}")
