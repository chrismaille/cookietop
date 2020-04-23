{%- if cookiecutter.database == "RDS" or cookiecutter.database == "Both" -%}
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_model import *  # noqa: F401, F403
{% endif %}