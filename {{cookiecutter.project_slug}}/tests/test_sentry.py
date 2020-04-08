from unittest.mock import ANY

import pytest
import toml
from stela import settings, stela_reload

from interface.initializers.sentry import initialize_sentry


@pytest.fixture(autouse=True)
def before_tests(monkeypatch):
    """Define environment before each test.

    This automatic fixture is used at module level:
        * Before each test: set env SENTRY_ENDPOINT
        * After each test: remove env SENTRY_ENDPOINT

    """
    monkeypatch.setenv("SENTRY_ENDPOINT", "https://sentry.com/foo")
    stela_reload()
    yield
    monkeypatch.delenv("SENTRY_ENDPOINT", raising=False)


def test_sentry_not_initialized(mocker, monkeypatch):
    """Test if Sentry is not initialized when endpoint is unavailable."""
    monkeypatch.delenv("SENTRY_ENDPOINT")
    stela_reload()
    sentry_mock = mocker.patch("interface.initializers.sentry.sentry_sdk")
    initialize_sentry()
    sentry_mock.assert_not_called()


def test_sentry_initialized(mocker):
    """Test if Sentry is initialized when endpoint is available."""
    sentry_mock = mocker.patch("interface.initializers.sentry.sentry_sdk")
    toml_data = {"tool": {"poetry": {"version": "1.0.0"}}}
    mocker.patch.object(toml, "load", return_value=toml_data)
    initialize_sentry()
    sentry_mock.init.assert_called_with(
        dsn="https://sentry.com/foo",
        integrations=ANY,
        environment=settings.stela_options.current_environment,
        release="1.0.0",
    )
