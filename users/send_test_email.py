from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Send a test email'

    def handle(self, *args, **kwargs):
        try:
            send_mail(
                'Test Email',
                'This is a test email.',
                settings.EMAIL_HOST_USER,
                ['your_email@example.com'],  # Replace with your email
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS('Successfully sent test email'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error sending email: {e}'))
