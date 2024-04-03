
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from config.settings import ADDRESS_MAIL_RU
from usersApp.models import User


def recovery_password(email):
    if email:
        try:
            user = User.objects.get(email=email)
            password = get_random_string(12)
            user.set_password(password)
            user.save()

            send_mail(
                subject='Вы сменили пароль',
                message=f'Ваш новый пароль {password}',
                from_email=ADDRESS_MAIL_RU,
                recipient_list=[user.email]
            )

            return {'success': 'marketApp/category_list.html'}

        except Exception as e:

            error_message = f"Ошибка отправки сообщения: {e}"
            return {'success': 'usersApp/forget_password.html', 'context': {'error_message': error_message}}

        except ObjectDoesNotExist:

            error_message = "пользователь не найден"
            return {'success': 'usersApp/forget_password.html', 'context': {'error_message': error_message}}

    else:
        error_message = ""

        return {'success': 'usersApp/forget_password.html', 'context': {'error_message': error_message}}


