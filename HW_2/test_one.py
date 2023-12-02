from HW_2 import check_output_text
import pytest

folder_in = '/home/user/folder_in'
folder_out = '/home/user/folder_out'


def test_step_1():
    assert check_output_text(f" cd {folder_in}; 7z a {folder_out}/archiv_1.7z", "Everything is Ok")


def test_step_2():
    assert check_output_text(f" cd {folder_out}; 7z l archiv_1.7z", "3 files")


def test_step_3():
    assert check_output_text(f" cd {folder_out} && 7z x {folder_out}/archiv_1.7z", "Everything is Ok")


def test_step_4():
    assert check_output_text(f" cd {folder_out}; 7z a archiv_2.7z", "Everything is Ok")


def test_step_5():
    assert check_output_text(f" cd {folder_out}; 7z d archiv_1.7z", "Everything is Ok")


if __name__ == '__main__':
    pytest.main(['-vv'])
