from http.client import responses
from time import sleep
import pytest
from  YouGileApi import YouGileApi

api = YouGileApi("https://yougile.com")

@pytest.mark.positive
def test_add_project_positive():
    title = "SkyPro"
    project = api.new_project(title)
    assert project.status_code == 201

@pytest.mark.negative
def test_add_project_negative():
    title = ""
    project = api.new_project(title)
    assert project.status_code == 400

@pytest.mark.positive
def test_positive_change_project():
    title = "SkyPro1"
    project = api.new_project(title)
    project_id = project.json()['id']
    print(project_id)

    new_title = "EasyCod"
    new_result = api.change_project(project_id, new_title)
    print(new_result)
    assert new_result.status_code == 200

@pytest.mark.negative
def test_negative_change_project():
    title = "SkyPro2"
    project = api.new_project(title)
    project_id = project.json()['id']
    print(project_id)

    new_title = ""
    new_result = api.change_project(project_id, new_title)
    print(new_result)
    assert new_result.status_code == 400

@pytest.mark.positive
def test_get_project_id_positive():
    title = "SkyPro3"
    project = api.new_project(title)
    project_id = project.json()['id']
    print(project_id)

    get_project_id = api.get_project_id(project_id)
    id_project = get_project_id.json()['id']
    title_project = get_project_id.json()['title']
    print(id_project, title_project)
    assert get_project_id.status_code == 200

@pytest.mark.negative
def test_get_project_id_negative():
    title = "SkyPro4"
    project = api.new_project(title)
    project_id = project.json()['id']
    print(project_id)

    get_project_id = api.get_project_id('385730d5-303c-40c2-8e9e-3dea73f157c')
    assert get_project_id.status_code == 404
