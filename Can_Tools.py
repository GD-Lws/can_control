def is_number(self):
    try:
        float(self)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(self)
        return True
    except (TypeError, ValueError):
        pass

    return False
