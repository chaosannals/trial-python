import os
import shutil

def pull_default(folder=None):
    cwd = os.getcwd()
    if None == folder:
        folder = cwd
    for path in os.listdir(folder):
        project_path = os.path.join(folder, path)
        if os.path.isdir(project_path):
            dot_git_folder = os.path.join(project_path, '.git')
            if os.path.isdir(dot_git_folder):
                print('[git pull start] {}'.format(project_path))
                os.chdir(project_path)
                os.system('git pull')
                print('[git pull end] {}'.format(project_path))
    os.chdir(cwd)

pull_default()
