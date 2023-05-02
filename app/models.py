import os
import sys
import yaml

class Task:
    def __init__(self, name: str, dependencies: list[str]):
        self.name = name
        self.dependencies = dependencies

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}'{(', ' + str(self.dependencies)) if len(self.dependencies) > 0 else ''}) "

    def __len__(self):
        return len(self.dependencies)

    def __getitem__(self, item):
        return self.dependencies[item]

    def info(self):
        info = f"""
        Task info:
        * name: {self.name}
        * dependencies: """
        info += ', '.join(self.dependencies)
        return info


class Build:
    def __init__(self, name: str, tasks: list[Task]):
        self.name = name
        self.tasks = tasks

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}'{(', ' + str(self.tasks)) if len(self.tasks) > 0 else ''}"

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, item):
        return self.tasks[item]

    def info(self):
        info = f"""
        Task info:
        * name: {self.name}
        * tasks: """
        tasks = [[x for x in y.dependencies] + [y.name] for y in self.tasks]
        tasks = sum(tasks, [])
        info += ', '.join(tasks)
        return info


def load_data(path_to_tasks: str = 'tasks.yaml', path_to_builds: str = 'builds.yaml') -> tuple[list[Task], list[Build]]:
    #check_paths({'tasks': path_to_tasks, 'builds': path_to_builds})
    tasks = []
    builds = []
    # Загружаем все tasks
    with open(path_to_tasks, 'r') as f:
        data = yaml.load(f, yaml.Loader)
        for task in data['tasks']:
            tasks.append(Task(task['name'], task['dependencies']))

    # Загружаем все builds, подключаем к ним уже созданные объекты Task
    with open(path_to_builds, 'r') as f:
        data = yaml.load(f, yaml.Loader)
        for build in data['builds']:
            task_names = build['tasks']
            build_tasks = []
            for task_name in task_names:
                for i, task in enumerate(tasks):
                    if task.name == task_name:
                        build_tasks.append(tasks[i])
            builds.append(Build(build['name'], build_tasks))

    return tasks, builds


def check_paths(paths):
    try:
        f = open(paths['tasks'])
    except FileNotFoundError as e:
        print('Path to tasks.yaml is wrong! Please specify path in main.py file.')
        os.system('pause')
        sys.exit()
    try:
        f = open(paths['builds'])
    except FileNotFoundError as e:
        print('Path to builds.yaml is wrong! Please specify path in main.py file.')
        os.system('pause')
        sys.exit()
    return 0
