from HW_3 import check_output_text
import pytest
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.mark.usefixtures('make_folders', 'make_files', 'delete_folders')
class TestSeminar:

    def test_step_1(self):
        assert check_output_text(f" cd {data.get('folder_in')}; 7z a {data.get('folder_out')}/archiv_1.7z",
                                 "Everything is Ok")

    def test_step_2(self):
        assert check_output_text(f" cd {data.get('folder_out')}; 7z l archiv_1.7z", "3 files")

    def test_step_3(self):
        assert check_output_text(f" cd {data.get('folder_out')} && 7z x {data.get('folder_out')}/archiv_1.7z",
                                 "Everything is Ok")

    def test_step_4(self):
        assert check_output_text(f" cd {data.get('folder_out')}; 7z a archiv_2.7z", "Everything is Ok")

    def test_step_5(self):
        assert check_output_text(f" cd {data.get('folder_out')}; 7z d archiv_1.7z", "Everything is Ok")


if __name__ == '__main__':
    pytest.main(['-vv'])
