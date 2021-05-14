# flake8: noqa
"""Remove not used files."""
import logging
import os
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

manifest = {
    "step_functions": [
        "tests/test_step_functions.py",
        "{{cookiecutter.project_name_slug}}/interface/aws/step_functions.py",
        "{{cookiecutter.project_name_slug}}/interface/aws/handler_step_function.py",
        "{{cookiecutter.project_name_slug}}/application/machines",
        "{{cookiecutter.project_name_slug}}/application/handlers/start_demo_machine.py",
        "state_machine",
    ],
}

step_functions_choice = "{{ cookiecutter.add_step_functions }}"
logger.debug("Add step functions: {}".format(step_functions_choice))

exclude_files = []

if step_functions_choice != "yes":
    exclude_files = manifest["step_functions"]

for string_path in exclude_files:
    path = Path().cwd().joinpath(string_path)
    if path.is_dir():
        shutil.rmtree(path)
    else:
        os.remove(str(path))
