from unittest import TestCase, main
from functions.func import check_age, check_auth, get_cost
from Yandex_API.Yandex_API import createfolder, get_folder_info

class Age(TestCase):
    def test_True(self):
        self.assertEqual(check_age(29), 'Доступ разрешён')

    def test_True_2(self):
        self.assertEqual(check_age(12), 'Доступ запрещён')

    def test_False(self):
        self.assertEqual(check_age(14), 'Доступ запрещён')


class Auth(TestCase):
    def test_True(self):
        self.assertEqual(check_auth('admin', 'password'), 'Добро пожаловать')

    def test_False(self):
        self.assertEqual(check_auth('admin', '123'), 'Доступ ограничен')

class Cost(TestCase):
    def test_True(self):
        self.assertEqual(get_cost(8), 'Стоимость доставки: 200 руб.')

    def test_False(self):
        self.assertEqual(get_cost(19), 'Стоимость доставки: 500 руб.')

FOLDERNAME = 'test'


class TestYandexAPI(TestCase):
    def test_createfolder(self):
        result = createfolder(FOLDERNAME)
        self.assertTrue(result == 201, f'Сервер ответил: {result}')

    def test_get_folder_info(self):
        self.assertTrue(get_folder_info(FOLDERNAME) == 'dir')


if __name__ == '__main__':
    main()
