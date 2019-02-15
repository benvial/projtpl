#!/usr/bin/env python
import os
import tempfile, yaml
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


json_tex ={
    "project_name": "{{ cookiecutter.project_name }}",
    "author_name": "{{ cookiecutter.author_name }}",
    "email": "{{ cookiecutter.email }}",
    "git_host_username": "{{ cookiecutter.git_host_username }}",
    "repo_name": "{{ cookiecutter.project_name }}",
    "description": "{{ cookiecutter.description }}",
    "_copy_without_render": ["custom.sty"]
}

conf = {}
conf["default_context"] = json_tex

config_tex, tmp_path = tempfile.mkstemp("latex.yml")
try:
    with open(config_tex, "wb") as tmp:
        tmp.write(yaml.dump(conf).encode("utf-8"))

finally:
    textmp_path = "https://github.com/benvial/textmp"
    # https://github.com/benvial/jupyter_tools
    os.system("cookiecutter -o tmp -f --no-input --config-file " + tmp_path + " " + textmp_path)
    os.remove(tmp_path)

try:
    os.system("rm -rf {}/reports/latex".format(PROJECT_DIRECTORY))
except OSError:
    pass
os.system("mv tmp/{{ cookiecutter.project_name }} {}/reports/latex".format(PROJECT_DIRECTORY))
os.system("rm -rf tmp")
os.system("git clone https://github.com/benvial/jupyter_tools")
os.system("mv jupyter_tools notebooks")
os.system("rm -rf notebooks/.git notebooks/.gitignore" )
