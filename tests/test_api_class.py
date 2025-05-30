from unittest.mock import MagicMock, Mock, patch

import pytest

from src.api_class import HeadHunterAPI


@patch("requests.get")
def test_connection_api(mock_get: Mock) -> None:
    """Тестирование получения данных по API"""

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"key": "value"}

    api = HeadHunterAPI(["8932785", "9451699"])

    response = api._HeadHunterAPI__connection_api("url")
    assert response == {"key": "value"}


@patch("requests.get")
def test_connection_api_error(mock_get: Mock) -> None:
    """Тестирование ошибка функции connection_api класса HeadHunterAPI"""
    mock_get.return_value.status_code = 404

    api = HeadHunterAPI(["8932785", "9451699"])

    with pytest.raises(BaseException, match="Статус код: 404"):
        api._HeadHunterAPI__connection_api("url")


employers_ids = ["123", "456"]
api = HeadHunterAPI(employers_ids)


@patch("src.api_class.requests.get")
def test_get_info_success(mock_get):
    """Тестирование преобразования и вывода данных"""

    emp_response = MagicMock()
    emp_response.status_code = 200
    emp_response.json.return_value = {
        "id": "123",
        "name": "Employer1",
        "vacancies_url": "https://api.hh.ru/employers/123/vacancies",
    }

    vacancies_response = MagicMock()
    vacancies_response.status_code = 200
    vacancies_response.json.return_value = {
        "items": [{"id": "v1", "title": "Job 1"}, {"id": "v2", "title": "Job 2"}]
    }

    mock_get.side_effect = [
        emp_response,
        vacancies_response,
        emp_response,
        vacancies_response,
    ]

    result = api.get_info()

    expected = [
        {
            "employee": emp_response.json.return_value,
            "vacancies": vacancies_response.json.return_value["items"],
        },
        {
            "employee": emp_response.json.return_value,
            "vacancies": vacancies_response.json.return_value["items"],
        },
    ]

    assert result == expected
    assert mock_get.call_count == 4


@patch("src.api_class.requests.get")
def test_get_info_api_error(mock_get):
    """Тестирование ошибки при преобразовании и выводе данных"""

    error_response = MagicMock()
    error_response.status_code = 404
    mock_get.return_value = error_response

    try:
        api.get_info()
    except BaseException as e:
        assert "Статус код: 404" in str(e)
    else:
        assert False, "Expected BaseException was not raised"
