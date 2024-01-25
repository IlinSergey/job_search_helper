from unittest.mock import AsyncMock

import pytest


@pytest.fixture(scope="function")
def update() -> AsyncMock:
    return AsyncMock()


@pytest.fixture(scope="function")
def context() -> AsyncMock:
    return AsyncMock()


@pytest.fixture(scope="session")
def covering_letter_response():
    response = {'result': {'alternatives': [{'message': {'role': 'assistant',
                                                         'text': 'covering letter for test description.'},
                                             'status': 'ALTERNATIVE_STATUS_FINAL'}],
                           'modelVersion': '08.12.2023',
                           'usage': {'completionTokens': '9',
                                     'inputTextTokens': '62',
                                     'totalTokens': '71'}}}
    return response


@pytest.fixture(scope="session")
def description_vacation_text():
    response = {'id': '91672663', 'premium': False, 'billing_type': {
        'id': 'standard_plus', 'name': 'Стандарт плюс'
        },
                'relations': [], 'name': 'Программист - разработчик Python / PHP Developer',
                'insider_interview': None, 'response_letter_required': False, 'area': {
                    'id': '2', 'name': 'Санкт-Петербург', 'url': 'https://api.hh.ru/areas/2'
                    },
                'salary': {'from': None, 'to': 75000, 'currency': 'RUR', 'gross': True},
                'type': {'id': 'open', 'name': 'Открытая'},
                'address': {'city': 'Санкт-Петербург', 'street': 'улица Седова',
                            'building': '11', 'lat': 59.899577, 'lng': 30.401415,
                            'description': None, 'raw': 'Санкт-Петербург, улица Седова, 11',
                            'metro': {'station_name': 'Елизаровская',
                                      'line_name': 'Невско-Василеостровская',
                                      'station_id': '16.232', 'line_id': '16',
                                      'lat': 59.89669, 'lng': 30.423656},
                            'metro_stations': [{'station_name': 'Елизаровская',
                                                'line_name': 'Невско-Василеостровская',
                                                'station_id': '16.232', 'line_id': '16',
                                                'lat': 59.89669, 'lng': 30.423656
                                                }]},
                'allow_messages': True,
                'experience': {
                    'id': 'between1And3', 'name': 'От 1 года до 3 лет'
                    },
                'schedule': {
                    'id': 'fullDay', 'name': 'Полный день'
                    },
                'employment': {
                    'id': 'full', 'name': 'Полная занятость'
                    },
                'department': None, 'contacts': None,
                'description': '<p>в команду Дата-центра Имаклик ищем Программиста-разработчика Python / PHP Developer</p> <p><strong>Обязанности:</strong></p> <ul> <li>Разработка отдельных модулей программных комплексов</li> </ul> <p> </p> <p><strong>Требования:</strong></p> <ul> <li>Базовые знания (основы): Linux, MySQL, Apache HTTP Server, SQL, Flask, Django</li> <li>Ключевые навыки: Python, PHP, Linux, MySQL, Apache HTTP Server, SQL, Flask</li> <li>Дополнительно: Git , OpenCV, Numpy, Redis, RabbitMQ</li> </ul> <strong>Условия:</strong> <ul> <li>гарантируем оформление трудовых отношений в соответствии с ТК РФ</li> <li>оплата больничных и отпусков</li> <li>работа в дружелюбном/доброжелательном коллективе</li> <li>развитая корпоративная культура, проведение ярких и активных мероприятий</li> <li>гибкий график отпусков</li> <li>полная занятость, полный день</li> </ul> <p><strong>Желательно:</strong></p> (приветствуется): Git, OpenCV, Numpy, Redis, RabbitMQ <p> </p>',  # noqa: E501
                'branded_description': None,
                'vacancy_constructor_template': None,
                'key_skills': [{'name': 'Python'}, {'name': 'PHP'}, {'name': 'Linux'},
                               {'name': 'MySQL'}, {'name': 'Apache HTTP Server'}, {'name': 'SQL'},
                               {'name': 'Flask'}],
                'accept_handicapped': False,
                'accept_kids': False,
                'archived': False,
                'response_url': None,
                'specializations': [],
                'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                'code': None,
                'hidden': False,
                'quick_responses_allowed': False,
                'driver_license_types': [],
                'accept_incomplete_resumes': False,
                'employer': {
                    'id': '678261',
                    'name': 'Имаклик',
                    'url': 'https://api.hh.ru/employers/678261',
                    'alternate_url': 'https://hh.ru/employer/678261',
                    'logo_urls': {
                        'original': 'https://hhcdn.ru/employer-logo-original/1125875.jpg',
                        '90': 'https://hhcdn.ru/employer-logo/6124089.jpeg',
                        '240': 'https://hhcdn.ru/employer-logo/6124090.jpeg'
                        },
                    'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=678261',
                    'accredited_it_employer': True, 'trusted': True},
                'published_at': '2024-01-24T17:23:51+0300',
                'created_at': '2024-01-24T17:23:51+0300',
                'initial_created_at': '2024-01-15T17:23:51+0300',
                'negotiations_url': None,
                'suitable_resumes_url': None,
                'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=91672663',
                'has_test': False,
                'test': None,
                'alternate_url': 'https://hh.ru/vacancy/91672663',
                'working_days': [],
                'working_time_intervals': [],
                'working_time_modes': [],
                'accept_temporary': False,
                'languages': []}
    return response
