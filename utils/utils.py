from PyQt5.QtWidgets import QDesktopWidget


def split_content_if_needed(content):
    lines = content.split('\n')
    if len(content) <= 1450 and len(lines) < 25:
        return [content]
    else:
        result = []
        current = ''
        for idx, line in enumerate(lines):
            if len(current) + len(line) > 1450 or idx % 24 == 0:
                result.append(current)
                current = ''
            current += '<p>' + line + '</p>'
        result.append(current)
        return result


def move_window_to_center(window):
    qr = window.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())
