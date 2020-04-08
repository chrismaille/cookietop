from uuid import uuid4

import arrow
import pytest
from pynamodb.exceptions import DoesNotExist

from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


@pytest.mark.parametrize(
    "model_uuid",
    ["eff8fbede0f04f3985d21f09ea9f1280", "eff8fbede0f04f3985d21f09ea9f1280"],
    ids=["First try", "Same Id again"],
)
def test_save_document(model_uuid):
    with pytest.raises(DoesNotExist):
        Noverde{{cookiecutter.domain_class}}Document.get(hash_key=model_uuid)

    data = {
        "uuid": model_uuid,
        "created": arrow.utcnow().datetime,
        "rule": EnterpriseResources.noverde,
    }
    new_instance = Noverde{{cookiecutter.domain_class}}Document(**data)
    new_instance.save()

    test_instance = Noverde{{cookiecutter.domain_class}}Document.get(hash_key=model_uuid)
    assert test_instance.uuid == model_uuid
