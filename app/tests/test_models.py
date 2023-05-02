import pytest

from app.models import Task, Build, load_data, check_paths


def test_Task():
    t = Task('task_1', ['1', '2'])
    assert t


def test_Build():
    b = Build('build_1', [Task('task_1', []), Task('task_2', [])])
    assert b


def test_wrong_path():
    with pytest.raises(FileNotFoundError):
        load_data('1', '2')


def test_check_path():
    assert check_paths({'tasks': 'tasks.yaml', 'builds': 'builds.yaml'}) == 0


def test_load_data():
    tasks, builds = load_data('tasks.yaml', 'builds.yaml')
    assert [x.name for x in builds] == ['approach_important', 'audience_stand', 'time_alone']
