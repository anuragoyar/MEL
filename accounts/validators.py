import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SpecialCharacterValidator:
    """
    Validate that the password contains at least one special character.
    """
    def __init__(self, special_chars=None):
        self.special_chars = special_chars or r'[!@#$%^&*(),.?":{}|<>]'
    
    def validate(self, password, user=None):
        if not re.search(self.special_chars, password):
            raise ValidationError(
                _("Password must contain at least one special character."),
                code='password_no_special_char',
            )
    
    def get_help_text(self):
        return _("Your password must contain at least one special character.")


class DigitValidator:
    """
    Validate that the password contains at least one digit.
    """
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                _("Password must contain at least one digit."),
                code='password_no_digit',
            )
    
    def get_help_text(self):
        return _("Your password must contain at least one digit.") 