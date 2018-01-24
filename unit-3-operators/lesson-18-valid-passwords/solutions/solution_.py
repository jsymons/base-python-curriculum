# #### Don't change these passwords #### #
password_1 = 'Jhx85a'
password_2 = 'ajd2819adkBjld'
password_3 = '81$br&j#'
password_4 = 'kp03%$Ji19Br!rdV'
# #### Don't change these passwords #### #

# == Your Code Below == ##

## Is Long Enough
# Has at least 12 chars
is_long_enough_pwd_1 = len(password_1) >= 12  # False
is_long_enough_pwd_2 = len(password_2) >= 12
is_long_enough_pwd_3 = len(password_3) >= 12
is_long_enough_pwd_4 = len(password_4) >= 12

## Has at least one of the following numbers: 0, 1, 2, 3
has_one_number_pwd_1 = (
    '0' in password_1 or
    '1' in password_1 or
    '2' in password_1 or
    '3' in password_1)
has_one_number_pwd_2 = (
    '0' in password_2 or
    '1' in password_2 or
    '2' in password_2 or
    '3' in password_2)
has_one_number_pwd_3 = (
    '0' in password_3 or
    '1' in password_3 or
    '2' in password_3 or
    '3' in password_3)
has_one_number_pwd_4 = (
    '0' in password_4 or
    '1' in password_4 or
    '2' in password_4 or
    '3' in password_4)

## Has at least one of these characters, v, V, r, R, b, B.
has_required_character_pwd_1 = (
    'v' in password_1 or
    'V' in password_1 or
    'r' in password_1 or
    'R' in password_1 or
    'b' in password_1 or
    'B' in password_1)
has_required_character_pwd_2 = (
    'v' in password_2 or
    'V' in password_2 or
    'r' in password_2 or
    'R' in password_2 or
    'b' in password_2 or
    'B' in password_2)
has_required_character_pwd_3 = (
    'v' in password_3 or
    'V' in password_3 or
    'r' in password_3 or
    'R' in password_3 or
    'b' in password_3 or
    'B' in password_3)
has_required_character_pwd_4 = (
    'v' in password_4 or
    'V' in password_4 or
    'r' in password_4 or
    'R' in password_4 or
    'b' in password_4 or
    'B' in password_4)

## Has at least one symbol: $%#&
at_least_one_symbol_pwd_1 = (
    '$' in password_1 or
    '%' in password_1 or
    '#' in password_1 or
    '&' in password_1)
at_least_one_symbol_pwd_2 = (
    '$' in password_2 or
    '%' in password_2 or
    '#' in password_2 or
    '&' in password_2)
at_least_one_symbol_pwd_3 = (
    '$' in password_3 or
    '%' in password_3 or
    '#' in password_3 or
    '&' in password_3)
at_least_one_symbol_pwd_4 = (
    '$' in password_4 or
    '%' in password_4 or
    '#' in password_4 or
    '&' in password_4)
