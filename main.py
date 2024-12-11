import urwid


def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def on_ask_change(edit, new_edit_text):
    password = new_edit_text
    score = 0
    checks = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    for check_function in checks:
        if check_function(password):
            score += 2
    reply.set_text("Рейтинг этого пароля: %s" % str(score))


password_edit = urwid.Edit("Введите пароль: ", mask="*")
reply = urwid.Text("Рейтинг этого пароля: 0")

pile = urwid.Pile([password_edit, reply])
main = urwid.Filler(pile)


def main_loop():
    urwid.connect_signal(password_edit, 'change', on_ask_change)
    urwid.MainLoop(main).run()


if __name__ == "__main__":
    main_loop()
