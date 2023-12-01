# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден
# в её выводе и False в противном случае. Передаваться должна только одна строка,
# разбиение вывода использовать не нужно.


import subprocess


def check_output_text(command, target_text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    print(out)
    if result.returncode == 0 and target_text in result.stdout:
        return True
    else:
        return False


command = 'cat /etc/os-release'
target_text = 'Ubuntu 22.04.1 LTS'
is_text_found = check_output_text(command, target_text)
print(is_text_found)
