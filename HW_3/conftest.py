import pytest
import yaml
import logging
from HW_3 import check_output_text
import os

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

logging.basicConfig(filename='stat.txt', level=logging.INFO, format='%(asctime)s %(message)s')


@pytest.fixture(scope='class')
def make_folders():
    logging.info('Шаг 1: Создание папок')
    return check_output_text(f" mkdir -p {data.get('folder_in')} {data.get('folder_out')}", '')


@pytest.fixture(scope='class')
def delete_folders():
    yield
    logging.info('Шаг 4: Удаление папок')
    return check_output_text(f"rm -rf {data.get('folder_in')} {data.get('folder_out')}", '')


@pytest.fixture(scope='class')
def make_files():
    logging.info('Шаг 2: Создание файлов')
    result = check_output_text(f"cd {data.get('folder_in')}; touch text_1.txt text_2.txt text_3.txt", '')
    file_sizes = [os.path.getsize(f"{data.get('folder_in')}/text_1.txt"),
                  os.path.getsize(f"{data.get('folder_in')}/text_2.txt"),
                  os.path.getsize(f"{data.get('folder_in')}/text_3.txt")]
    logging.info(f'Размеры файлов: {file_sizes}')
    return result
