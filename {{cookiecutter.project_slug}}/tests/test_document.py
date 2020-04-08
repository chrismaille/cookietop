from uuid import uuid4

import arrow
import pytest
from pynamodb.exceptions import DoesNotExist

from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


@pytest.mark.parametrize("model_uuid", [
        "90e5c60d601543208a9e8b7e915ce2a9",
        "90e5c60d601543208a9e8b7e915ce2a9"
    ])
def test_save_document(model_uuid):
    with pytest.raises(DoesNotExist):
        test_instance = Noverde{{cookiecutter.domain_class}}Document.get(hash_key=model_uuid)
    # assert test_instance is None
    
    data = {
        "uuid": model_uuid,
        "created": arrow.utcnow().datetime,
        "rule": EnterpriseResources.noverde}
    new_instance = Noverde{{cookiecutter.domain_class}}Document(**data)
    new_instance.save()

    test_instance = Noverde{{cookiecutter.domain_class}}Document.get(hash_key=model_uuid)
    assert test_instance.uuid is not None
    assert test_instance is not None
