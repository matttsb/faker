# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as BaseProvider


class Provider(BaseProvider):
    # Source:
    # https://en.wikipedia.org/wiki/INSEE_code

    # The format is as follows: syymmlloookkk cc,[1] where

    # s is 1 for a male, 2 for a female,
    # yy are the last two digits of the year of birth,
    # mm is the month of birth, usually 01 to 12 (but there are special values for persons whose exact date of birth is not known),
    # ll is the number of the départment of origin : 2 digits, or 1 digit and 1 letter in metropolitan France, 3 digits for overseas.
    # ooo is the commune of origin (a department is composed of various communes) : 3 digits in metropolitan France or 2 digits for overseas.
    # kkk is an order number to distinguish people being born at the same place in the same year and month. This number is the one given by the Acte de naissance, an official paper which officialize a birth (and is needed throughout life for various administrative procedures, such as getting an identity card).
    # 'cc' is the "control key", 01 to 97, equal to 97-(the rest of the number modulo 97) or to 97 if the number is a multiple of 97.
       
    nino_formats = (
        '############# ##',
    )

    def ssn(self):
        pattern = self.random_element(self.nino_formats)
        return self.numerify(self.generator.parse(pattern))
