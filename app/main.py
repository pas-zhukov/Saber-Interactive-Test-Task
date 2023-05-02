import click
from models import load_data, check_paths

# Путь к файлам tasks.yaml и builds.yaml
# Используем dict для дальнейшего удобства создания команд
PATH_TO_FILES = {
    'tasks': 'tasks.yaml',
    'builds': 'builds.yaml'
}
# Проверяем корректность пути к файлам
check_paths(PATH_TO_FILES)
# Загружаем данные из файлов в глобальные переменные
TASKS, BUILDS = load_data(*PATH_TO_FILES.values())


@click.group()
def commands():
    pass


@click.command('list')
@click.argument('entity', type=click.Choice(PATH_TO_FILES.keys()), required=1)
def list(entity: str):
    """
    Prints the list of loaded task or build names.

    """
    if entity == 'tasks':
        click.echo('List of available tasks:')
        for task in TASKS:
            click.echo(f'* {task}')
    else:
        click.echo('List of available builds:')
        for build in BUILDS:
            click.echo(f'* {build}')


@click.command('get')
@click.argument('entity', type=click.Choice(['task', 'build']), required=1)
@click.argument('name', type=str, required=1)
def get(entity: str, name: str):
    """
    Prints detailed info about specific task or build.

    NAME: Specify the name of task/build.
    """
    if entity == 'task':
        tasks_names = [x.name for x in TASKS]
        try:
            click.echo(TASKS[tasks_names.index(name)].info())
        except ValueError:
            click.echo(f'{entity.title()} named "{name}" does not exist!')
    else:
        builds_names = [x.name for x in BUILDS]
        try:
            click.echo(BUILDS[builds_names.index(name)].info())
        except ValueError:
            click.echo(f'{entity.title()} named "{name}" does not exist!')


commands.add_command(list)
commands.add_command(get)

if __name__ == '__main__':
    commands()
