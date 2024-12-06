import validators


def urlValidator(url):
    valid = validators.url(url)
    return valid



