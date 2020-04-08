from uuid import uuid4

import arrow
from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


def test_save_document():
    # data = {
    #     "uuid": str(uuid4()),
    #     "created": arrow.utcnow().datetime,
    #     "rule": EnterpriseResources.noverde}
    # new_instance = Noverde{{cookiecutter.domain_class}}Document(**data)
    # new_instance.save()

    # assert new_instance.uuid is not None
    # test_instance = Noverde{{cookiecutter.domain_class}}Document.uuid.get(new_instance.uuid)
    # assert test_instance is not None
    pass
