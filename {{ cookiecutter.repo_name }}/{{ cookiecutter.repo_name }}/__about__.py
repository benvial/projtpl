from datetime import date

__version__ = "0.0.1"
__author__ =  "{{ cookiecutter.author_name }}"
__author_email__ = "{{ cookiecutter.email }}"
__copyright__ = u"Copyright (c) 2017-{}, {} <{}>".format(
    date.today().year, __author__, __author_email__
)
__website__ = "https://{{ cookiecutter.git_host_username }}.github.io/{{ cookiecutter.repo_name }}"
__license__ = license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}'
__status__ = "Development Status :: 5 - Production/Stable"
__description__ = (
    "{{ cookiecutter.description }}"
)
