from abc import ABC, abstractmethod


class AbstractAPIJob(ABC):
    """Абстрактный метод для работы с API"""

    @abstractmethod
    def get_info(self) -> None:
        pass


class AbsDBManager(ABC):
    """Абстрактный метод для работы с SQL запросами"""

    @abstractmethod
    def get_companies_and_vacancies_count(self) -> None:
        pass

    @abstractmethod
    def get_all_vacancies(self) -> None:
        pass

    @abstractmethod
    def get_avg_salary(self) -> None:
        pass

    @abstractmethod
    def get_vacancies_with_higher_salary(self) -> None:
        pass

    @abstractmethod
    def get_vacancies_with_keyword(self, key) -> None:
        pass
