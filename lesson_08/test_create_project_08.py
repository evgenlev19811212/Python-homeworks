from API_YouGile import YouGile

api = YouGile()


def test_create_project_positive():  # создание проекта
    IdCompany = api.get_companies()
    API_key = api.get_keys(IdCompany)
    resp = api.create_project(API_key)
    project_Id = resp.json()['id']
    # проверка создания
    assert resp.status_code == 201
    # удаление тестовых данных
    del_Id = api.delete_project(API_key, project_Id)
    # проверка удаления
    assert del_Id == project_Id


def test_create_project_negative():  # создание проекта без названия
    IdCompany = api.get_companies()
    API_key = api.get_keys(IdCompany)
    resp = api.create_project(API_key, "")
    # проверка НЕсоздания
    assert resp.status_code == 400
    assert resp.json()["message"] == ["title should not be empty"]
