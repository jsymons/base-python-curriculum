class Cookie(object):

    @classmethod
    def create_cookies(cls, amount):
        # return [cls() for _ in range(amount)]
        cookies = []
        for _ in range(amount):
            # cookies.append(Cookie())
            cookies.append(cls())

        return cookies
