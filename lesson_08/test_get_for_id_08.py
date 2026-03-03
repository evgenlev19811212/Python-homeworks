from API_YouGile import YouGile

api = YouGile()


def test_get_for_id_positive():  # получение проекта по ID
    # создание проекта
    IdCompany = api.get_companies()
    API_key = api.get_keys(IdCompany)
    resp = api.create_project(API_key)
    project_Id = resp.json()['id']
    # проверка создания
    assert resp.status_code == 201
    # получение проекта по ID
    resp_get = api.get_for_id(API_key, project_Id)
    # проверка получения
    assert resp_get.status_code == 200
    assert resp_get.json()['id'] == project_Id
    assert resp_get.json()['title'] == "Best Of Project"
    # удаление тестовых данных
    del_Id = api.delete_project(API_key, project_Id)
    # проверка удаления
    assert del_Id == project_Id


def test_get_for_id_negative():  # получение по несуществующему ID
    IdCompany = api.get_companies()
    API_key = api.get_keys(IdCompany)
    resp = api.get_for_id(API_key, "123")
    # проверка НЕполучения
    assert resp.status_code == 404
    assert resp.json()["message"] == "Проект не найден"
    assert resp.json()["error"] == "Not Found"
