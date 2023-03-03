from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^\+994\d{9}$',
    message="Phone number must be in the format: "
            "'+994dddddddd'. Up to 9 digits allowed."
)

