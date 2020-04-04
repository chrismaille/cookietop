from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model


def test_save_model():
    data = {"rule": EnterpriseResources.noverde}
    new_instance = Noverde{{cookiecutter.domain_class}}Model(**data)
    assert new_instance.id is None
    new_instance.save()
    assert new_instance.id is not None

    test_instance = Noverde{{cookiecutter.domain_class}}Model.query().filter_by(id=new_instance.id).one()
    assert test_instance is not None
