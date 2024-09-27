from djoser.email import ActivationEmail as DjoserActivationEmail

class ActivationEmail(DjoserActivationEmail):
    template_name = 'email/activation_email.html'
