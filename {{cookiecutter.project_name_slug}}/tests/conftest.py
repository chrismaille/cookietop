"""Pytest main conftest module."""
import json
import os
import pytest

from stela import settings
from uuid import UUID, uuid4

from pathlib import Path
from typing import Any, Dict

from models import {{cookiecutter.model_name_camel}}Document


@pytest.fixture(autouse=True)
def document_session():
    """Remove table after test.

    This automatic fixture is used at function level:
        * After each test: delete and create dynamodb table.

    """
    if {{cookiecutter.model_name_camel}}Document.exists():
        {{cookiecutter.model_name_camel}}Document.delete_table()
    {{cookiecutter.model_name_camel}}Document.create_table(
        read_capacity_units=1, write_capacity_units=1, wait=True
    )

    # Run tests
    yield

    # Remove table
    {{cookiecutter.model_name_camel}}Document.delete_table()


@pytest.fixture
def new_{{cookiecutter.model_name_slug}}_document_data() -> Dict[str, UUID]:
    return {"uuid": uuid4()}


@pytest.fixture
def {{cookiecutter.model_name_slug}}_document(new_{{cookiecutter.model_name_slug}}_document_data: Dict[Any, Any]) -> {{cookiecutter.model_name_camel}}Document:
    """Return {{cookiecutter.model_name_camel}}Document Fixture.

    :return: {{cookiecutter.model_name_camel}}Document instance
    """
    new_instance = {{cookiecutter.model_name_camel}}Document(**new_{{cookiecutter.model_name_slug}}_document_data)
    new_instance.save()
    return new_instance


def load_fixture(filename: str) -> Dict[Any, Any]:
    """Load fixtures from fixtures folder.

    :param filename: json filename
    :return: Dict
    """
    if settings.get("use_cookie_path", False):
        base_path = os.environ.get("PYTHONPATH", "").split(":")[0]
    else:
        base_path = str(Path().cwd())
    file_path = Path().joinpath(base_path, "tests", "fixtures", filename)
    with open(str(file_path)) as file:
        fixture = json.load(file)
    return fixture
