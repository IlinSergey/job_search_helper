
import pytest

from utils.custom_types import SearchParams


@pytest.fixture(scope="session")
def covering_letter_from_yagpt_response():
    response = {"result": {"alternatives": [{"message": {"role": "assistant",
                                                         "text": "covering letter for test description."},
                                             "status": "ALTERNATIVE_STATUS_FINAL"}],
                           "modelVersion": "08.12.2023",
                           "usage": {"completionTokens": "9",
                                     "inputTextTokens": "62",
                                     "totalTokens": "71"}}}
    return response


@pytest.fixture(scope="session")
def description_vacation_text():
    response = {"id": "91672663", "premium": False, "billing_type": {
        "id": "standard_plus", "name": "Стандарт плюс"
        },
                "relations": [], "name": "Программист - разработчик Python / PHP Developer",
                "insider_interview": None, "response_letter_required": False, "area": {
                    "id": "2", "name": "Санкт-Петербург", "url": "https://api.hh.ru/areas/2"
                    },
                "salary": {"from": None, "to": 75000, "currency": "RUR", "gross": True},
                "type": {"id": "open", "name": "Открытая"},
                "address": {"city": "Санкт-Петербург", "street": "улица Седова",
                            "building": "11", "lat": 59.899577, "lng": 30.401415,
                            "description": None, "raw": "Санкт-Петербург, улица Седова, 11",
                            "metro": {"station_name": "Елизаровская",
                                      "line_name": "Невско-Василеостровская",
                                      "station_id": "16.232", "line_id": "16",
                                      "lat": 59.89669, "lng": 30.423656},
                            "metro_stations": [{"station_name": "Елизаровская",
                                                "line_name": "Невско-Василеостровская",
                                                "station_id": "16.232", "line_id": "16",
                                                "lat": 59.89669, "lng": 30.423656
                                                }]},
                "allow_messages": True,
                "experience": {
                    "id": "between1And3", "name": "От 1 года до 3 лет"
                    },
                "schedule": {
                    "id": "fullDay", "name": "Полный день"
                    },
                "employment": {
                    "id": "full", "name": "Полная занятость"
                    },
                "department": None, "contacts": None,
                "description": "<p>в команду Дата-центра Имаклик ищем Программиста-разработчика Python / PHP Developer</p> <p><strong>Обязанности:</strong></p> <ul> <li>Разработка отдельных модулей программных комплексов</li> </ul> <p> </p> <p><strong>Требования:</strong></p> <ul> <li>Базовые знания (основы): Linux, MySQL, Apache HTTP Server, SQL, Flask, Django</li> <li>Ключевые навыки: Python, PHP, Linux, MySQL, Apache HTTP Server, SQL, Flask</li> <li>Дополнительно: Git , OpenCV, Numpy, Redis, RabbitMQ</li> </ul> <strong>Условия:</strong> <ul> <li>гарантируем оформление трудовых отношений в соответствии с ТК РФ</li> <li>оплата больничных и отпусков</li> <li>работа в дружелюбном/доброжелательном коллективе</li> <li>развитая корпоративная культура, проведение ярких и активных мероприятий</li> <li>гибкий график отпусков</li> <li>полная занятость, полный день</li> </ul> <p><strong>Желательно:</strong></p> (приветствуется): Git, OpenCV, Numpy, Redis, RabbitMQ <p> </p>",  # noqa: E501
                "branded_description": None,
                "vacancy_constructor_template": None,
                "key_skills": [{"name": "Python"}, {"name": "PHP"}, {"name": "Linux"},
                               {"name": "MySQL"}, {"name": "Apache HTTP Server"}, {"name": "SQL"},
                               {"name": "Flask"}],
                "accept_handicapped": False,
                "accept_kids": False,
                "archived": False,
                "response_url": None,
                "specializations": [],
                "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
                "code": None,
                "hidden": False,
                "quick_responses_allowed": False,
                "driver_license_types": [],
                "accept_incomplete_resumes": False,
                "employer": {
                    "id": "678261",
                    "name": "Имаклик",
                    "url": "https://api.hh.ru/employers/678261",
                    "alternate_url": "https://hh.ru/employer/678261",
                    "logo_urls": {
                        "original": "https://hhcdn.ru/employer-logo-original/1125875.jpg",
                        "90": "https://hhcdn.ru/employer-logo/6124089.jpeg",
                        "240": "https://hhcdn.ru/employer-logo/6124090.jpeg"
                        },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=678261",
                    "accredited_it_employer": True, "trusted": True},
                "published_at": "2024-01-24T17:23:51+0300",
                "created_at": "2024-01-24T17:23:51+0300",
                "initial_created_at": "2024-01-15T17:23:51+0300",
                "negotiations_url": None,
                "suitable_resumes_url": None,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=91672663",
                "has_test": False,
                "test": None,
                "alternate_url": "https://hh.ru/vacancy/91672663",
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "languages": []}
    return response


@pytest.fixture(scope="session")
def covering_letter_from_openai_response():
    response = {
                "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
                "object": "text_completion",
                "created": 1589478378,
                "model": "gpt-3.5-turbo-instruct",
                "system_fingerprint": "fp_44709d6fcb",
                "choices": [
                    {
                        "text": "Test covering letter from OpenAI service",
                        "index": 0,
                        "logprobs": None,
                        "finish_reason": "length"
                    }
                ],
                "usage": {
                    "prompt_tokens": 5,
                    "completion_tokens": 7,
                    "total_tokens": 12
                }
    }
    return response


@pytest.fixture(scope="session")
def response_from_hh():
    response = {
        "items": [
            {
                "id": "92292020",
                "premium": False,
                "name": "Программист Python junior",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {
                    "id": "1002",
                    "name": "Минск",
                    "url": "https://api.hh.ru/areas/1002"
                },
                "salary": {
                    "from": 300,
                    "to": 1000,
                    "currency": "USD",
                    "gross": False
                },
                "type": {
                    "id": "open",
                    "name": "Открытая"
                },
                "address": {
                    "city": "Минск",
                    "street": "проспект Дзержинского",
                    "building": "3Б",
                    "lat": 53.891614,
                    "lng": 27.527435,
                    "description": None,
                    "raw": "Минск, проспект Дзержинского, 3Б",
                    "metro": None,
                    "metro_stations": [],
                    "id": "13795427"
                },
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-01-27T14:26:23+0300",
                "created_at": "2024-01-27T14:26:23+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92292020",
                "show_logo_in_search": None,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/92292020?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/92292020",
                "relations": [],
                "employer": {
                    "id": "3189689",
                    "name": "Рэдис Бай",
                    "url": "https://api.hh.ru/employers/3189689",
                    "alternate_url": "https://hh.ru/employer/3189689",
                    "logo_urls": {
                        "240": "https://hhcdn.ru/employer-logo/2384601.png",
                        "90": "https://hhcdn.ru/employer-logo/2384600.png",
                        "original": "https://hhcdn.ru/employer-logo-original/485687.png"
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3189689",
                    "accredited_it_employer": False,
                    "trusted": True
                },
                "snippet": {
                    "requirement": "Знание языка <highlighttext>python</highlighttext>. Знание хотя бы одного фреймворка для backend разработки: django, flask, fastapi (основной стек у нас). ",  # noqa E501
                    "responsibility": "Разработка микроприложений на базе FastApi. Разработка различных интеграций между SAAS сервисами (сервисы оплат, доставок и прочего) по API. "  # noqa E501
                },
                "contacts": None,
                "schedule": {
                    "id": "fullDay",
                    "name": "Полный день"
                },
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "professional_roles": [
                    {
                        "id": "96",
                        "name": "Программист, разработчик"
                    }
                ],
                "accept_incomplete_resumes": False,
                "experience": {
                    "id": "noExperience",
                    "name": "Нет опыта"
                },
                "employment": {
                    "id": "full",
                    "name": "Полная занятость"
                },
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None
            },
            {
                "id": "92010900",
                "premium": False,
                "name": "Программист Python junior",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {
                    "id": "1",
                    "name": "Москва",
                    "url": "https://api.hh.ru/areas/1"
                },
                "salary": {
                    "from": 85000,
                    "to": 90000,
                    "currency": "RUR",
                    "gross": True
                },
                "type": {
                    "id": "open",
                    "name": "Открытая"
                },
                "address": {
                    "city": "Москва",
                    "street": "улица Солянка",
                    "building": "13/3с1",
                    "lat": 55.751285,
                    "lng": 37.641935,
                    "description": None,
                    "raw": "Москва, улица Солянка, 13/3с1",
                    "metro": None,
                    "metro_stations": [],
                    "id": "2745671"
                },
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-01-28T12:42:19+0300",
                "created_at": "2024-01-28T12:42:19+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92010900",
                "show_logo_in_search": None,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/92010900?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/92010900",
                "relations": [],
                "employer": {
                    "id": "864643",
                    "name": "CDNvideo (ООО СДН-видео)",
                    "url": "https://api.hh.ru/employers/864643",
                    "alternate_url": "https://hh.ru/employer/864643",
                    "logo_urls": {
                        "original": "https://hhcdn.ru/employer-logo-original/1194862.png",
                        "90": "https://hhcdn.ru/employer-logo/6399901.png",
                        "240": "https://hhcdn.ru/employer-logo/6399902.png"
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=864643",
                    "accredited_it_employer": True,
                    "trusted": True
                },
                "snippet": {
                    "requirement": "<highlighttext>Python</highlighttext> (asyncio, aiohttp, Tornado). Навыки работы с Linux (командная строка, API). Хорошее знание паттернов проектирования, структур данных и классических алгоритмов. ",  # noqa E501
                    "responsibility": "Разработка ПО для сети доставки контента CDNvideo и автоматизации конфигурирования услуг клиентами (задачи связаны с большими нагрузками (highload) и обработкой..."  # noqa E501
                },
                "contacts": None,
                "schedule": {
                    "id": "fullDay",
                    "name": "Полный день"
                },
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "professional_roles": [
                    {
                        "id": "96",
                        "name": "Программист, разработчик"
                    }
                ],
                "accept_incomplete_resumes": False,
                "experience": {
                    "id": "between1And3",
                    "name": "От 1 года до 3 лет"
                },
                "employment": {
                    "id": "full",
                    "name": "Полная занятость"
                },
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None
            }
        ],
        "found": 50,
        "pages": 25,
        "page": 0,
        "per_page": 2,
        "clusters": None,
        "arguments": None,
        "fixes": None,
        "suggests": None,
        "alternate_url": "https://hh.ru/search/vacancy?enable_snippets=True&items_on_page=2&search_period=1&text=Python+junior"  # noqa E501
    }
    return response


@pytest.fixture(scope="session")
def search_params() -> SearchParams:
    return SearchParams(
        vacancy_name="Python junior",
        experience="between1And3",
        type_of_employment="full",
        schedule="fullDay",
    )


@pytest.fixture(scope="session")
def user_id():
    return 1


@pytest.fixture(scope="session")
def chat_id():
    return 123


@pytest.fixture(scope="session")
def vacation_id():
    return 92292020


@pytest.fixture(scope="session")
def description_about_vacancy_response():
    response = {
        "id": "92292020",
        "premium": False,
        "billing_type": {
            "id": "free",
            "name": "Бесплатная"
        },
        "relations": [],
        "name": "Программист Python junior",
        "insider_interview": None,
        "response_letter_required": False,
        "area": {
            "id": "1002",
            "name": "Минск",
            "url": "https://api.hh.ru/areas/1002"
        },
        "salary": {
            "from": 300,
            "to": 1000,
            "currency": "USD",
            "gross": False
        },
        "type": {
            "id": "open",
            "name": "Открытая"
        },
        "address": {
            "city": "Минск",
            "street": "проспект Дзержинского",
            "building": "3Б",
            "lat": 53.891614,
            "lng": 27.527435,
            "description": None,
            "raw": "Минск, проспект Дзержинского, 3Б",
            "metro": None,
            "metro_stations": []
        },
        "allow_messages": True,
        "experience": {
            "id": "noExperience",
            "name": "Нет опыта"
        },
        "schedule": {
            "id": "fullDay",
            "name": "Полный день"
        },
        "employment": {
            "id": "full",
            "name": "Полная занятость"
        },
        "department": None,
        "contacts": None,
        "description": "<p><strong>Мы - Radis.by</strong><br />C 2017 года занимаемся автоматизацией бизнес-процессов для сфер ритейла: e-commerce и традиционный ритейл, услуг и производственной сферы с использованием облачных технологических решений. Занимаем ведущую позицию на русскоязычном рынке среди интеграторов RetailCRM.</p> <p>Активно растем и развиваемся и сейчас нам в штат требуется python-разработчик.</p> <p><strong>Обязанности:</strong></p> <ul> <li>Разработка микроприложений на базе FastApi.</li> <li>Разработка различных интеграций между SAAS сервисами (сервисы оплат, доставок и прочего) по API.</li> <li>Разработка API собственных решений.</li> <li>Проектирование архитектуры проекта совместно с PM.</li> <li>Работа в GitHub.</li> <li>Трекинг времени и задач в ClickUP</li> </ul> <strong>Требования:</strong> <ul> <li>Знание языка python.</li> <li>Знание хотя бы одного фреймворка для backend разработки: django, flask, fastapi (основной стек у нас).</li> <li>Опыт работы с базами данных (PostgreSQL, mongo).</li> <li>Наличие опыта коммерческой разработки.</li> <li>Желательно профильное высшее образование по computer science (если вы сейчас учитесь - тоже рассматриваем).</li> </ul> <strong>Условия:</strong> <ul> <li>Молодой коллектив, отсутствие бюрократии;</li> <li>Интересная работа в быстро развивающейся компании;</li> <li>График работы: 5/2, с 09.00 до 18.00 или с гибким графиком рабочего времени, есть возможность удалённой работы по необходимости;</li> <li>Испытательный срок: 1-2 месяца, обучение от руководителей, реальные задачи и ответственность со второй недели;</li> <li>Заработная плата: на время испытательного срока - 300$</li> </ul>",  # noqa: E501
        "branded_description": None,
        "vacancy_constructor_template": None,
        "key_skills": [
            {
                "name": "Python"
            },
            {
                "name": "Django Framework"
            },
            {
                "name": "Flask"
            },
            {
                "name": "SQL"
            },
            {
                "name": "API"
            },
            {
                "name": "JSON API"
            },
            {
                "name": "GitHub"
            },
            {
                "name": "REST"
            },
            {
                "name": "Docker"
            },
            {
                "name": "PostgreSQL"
            }
        ],
        "accept_handicapped": False,
        "accept_kids": False,
        "archived": False,
        "response_url": None,
        "specializations": [],
        "professional_roles": [
            {
                "id": "96",
                "name": "Программист, разработчик"
            }
        ],
        "code": None,
        "hidden": False,
        "quick_responses_allowed": False,
        "driver_license_types": [],
        "accept_incomplete_resumes": False,
        "employer": {
            "id": "3189689",
            "name": "Рэдис Бай",
            "url": "https://api.hh.ru/employers/3189689",
            "alternate_url": "https://hh.ru/employer/3189689",
            "logo_urls": {
                "90": "https://hhcdn.ru/employer-logo/2384600.png",
                "original": "https://hhcdn.ru/employer-logo-original/485687.png"
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3189689",
            "accredited_it_employer": False,
            "trusted": True
        },
        "published_at": "2024-01-27T14:26:23+0300",
        "created_at": "2024-01-27T14:26:23+0300",
        "initial_created_at": "2024-01-27T14:26:23+0300",
        "negotiations_url": None,
        "suitable_resumes_url": None,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92292020",
        "has_test": False,
        "test": None,
        "alternate_url": "https://hh.ru/vacancy/92292020",
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "languages": []
    }
    return response


@pytest.fixture(scope="session")
def clear_vacancy_description():
    result = "Мы - Radis.byC 2017 года занимаемся автоматизацией бизнес-процессов для сфер ритейла: e-commerce и традиционный ритейл, услуг и производственной сферы с использованием облачных технологических решений. Занимаем ведущую позицию на русскоязычном рынке среди интеграторов RetailCRM. Активно растем и развиваемся и сейчас нам в штат требуется python-разработчик. Обязанности:  Разработка микроприложений на базе FastApi. Разработка различных интеграций между SAAS сервисами (сервисы оплат, доставок и прочего) по API. Разработка API собственных решений. Проектирование архитектуры проекта совместно с PM. Работа в GitHub. Трекинг времени и задач в ClickUP  Требования:  Знание языка python. Знание хотя бы одного фреймворка для backend разработки: django, flask, fastapi (основной стек у нас). Опыт работы с базами данных (PostgreSQL, mongo). Наличие опыта коммерческой разработки. Желательно профильное высшее образование по computer science (если вы сейчас учитесь - тоже рассматриваем).  Условия:  Молодой коллектив, отсутствие бюрократии; Интересная работа в быстро развивающейся компании; График работы: 5/2, с 09.00 до 18.00 или с гибким графиком рабочего времени, есть возможность удалённой работы по необходимости; Испытательный срок: 1-2 месяца, обучение от руководителей, реальные задачи и ответственность со второй недели; Заработная плата: на время испытательного срока - 300$ "  # noqa E501
    return result


@pytest.fixture(scope="session")
def vacancy_from_db():
    return ("Some vacancy description * https://hh.ru/vacancy/92292020", 92292020)
