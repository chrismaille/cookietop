import pytest


# noinspection PyUnresolvedReferences
def test_bad_project_name():
    with pytest.raises(SystemExit) as sys_exit:
        import hooks.pre_gen_project  # noqa: F401

        assert sys_exit.value.code == 1
