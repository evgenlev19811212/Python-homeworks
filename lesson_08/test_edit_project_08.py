from API_YouGile import YouGile

api = YouGile()


def test_edit_project_positive():  # редактирование проекта
    # создание проекта
    IdCompany = api.get_companies()
    API_key = api.get_keys(IdCompany)
    resp = api.create_project(API_key)
    project_Id = resp.json()['id']
    # проверка создания
    assert resp.status_code == 201
    # редактирование проекта
    resp_edit = api.edit_project(API_key, project_Id)
    # проверка редактрования
    assert resp_edit.status_code == 200
    assert resp_edit.json()['id'] == project_Id
    # удаление тестовых данных
    del_Id = api.delete_project(API_key, project_Id)
    # проверка удаления
    assert del_Id == project_Id


def test_edit_project_negative():  # без названия при редактировании
    # создание проекта
    IdCompany = api.get_companies()
    API_key = api.get_keys(IdCompany)
    resp = api.create_project(API_key)
    project_Id = resp.json()['id']
    # проверка создания
    assert resp.status_code == 201
    # редактирование проекта
    resp_edit = api.edit_project(API_key, project_Id, "")
    # проверка НЕредактирования
    assert resp_edit.status_code == 400
    assert resp_edit.json()["message"] == ["title should not be empty"]
    # удаление тестовых данных
    del_Id = api.delete_project(API_key, project_Id)
    # проверка удаления
    assert del_Id == project_Id
