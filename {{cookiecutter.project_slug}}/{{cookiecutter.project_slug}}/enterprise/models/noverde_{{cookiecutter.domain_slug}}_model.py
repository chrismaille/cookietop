from enterprise.models.{{cookiecutter.domain_slug}}_model import {{cookiecutter.domain_class}}Model
from enterprise.rules.noverde_mixin import NoverdeMixin


class Noverde{{cookiecutter.domain_class}}Model(NoverdeMixin, {{cookiecutter.domain_class}}Model):
    pass
