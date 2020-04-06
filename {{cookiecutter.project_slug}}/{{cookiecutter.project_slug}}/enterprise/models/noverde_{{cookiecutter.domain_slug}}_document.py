from enterprise.models.{{cookiecutter.domain_slug}}_document import {{cookiecutter.domain_class}}Document
from enterprise.rules.noverde_mixin import NoverdeMixin


class Noverde{{cookiecutter.domain_class}}Document(NoverdeMixin, {{cookiecutter.domain_class}}Document):
    pass
