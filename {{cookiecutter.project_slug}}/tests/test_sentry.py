from unittest.mock import ANY, MagicMock

import pkg_resources
import pytest
from stela import settings, stela_reload

from initializers.sentry import initialize_sentry


@pytest.fixture(autouse=True)
def before_tests(monkeypatch):
    monkeypatch.setenv("SENTRY_ENDPOINT", "https://sentry.com/foo")
    stela_reload()
    yield
    monkeypatch.delenv("SENTRY_ENDPOINT", raising=False)


def test_sentry_not_initialized(mocker, monkeypatch):
    monkeypatch.delenv("SENTRY_ENDPOINT")
    stela_reload()
    sentry_mock = mocker.patch("initializers.sentry.sentry_sdk")
    initialize_sentry()
    sentry_mock.assert_not_called()


def test_sentry_initialized(mocker, monkeypatch):
    sentry_mock = mocker.patch("initializers.sentry.sentry_sdk")
    mocked_distribution = MagicMock()
    mocked_distribution.version = "1.0.0"
    mocker.patch.object(
        pkg_resources, "get_distribution", return_value=mocked_distribution
    )
    initialize_sentry()
    sentry_mock.init.assert_called_with(
        dsn="https://sentry.com/foo",
        integrations=ANY,
        environment=settings.stela_options.current_environment,
        release="1.0.0",
    )
