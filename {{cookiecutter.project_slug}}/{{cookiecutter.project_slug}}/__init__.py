"""{{cookiecutter.project_name}} Project.

Main domain: {{cookiecutter.domain}}
Description: {{cookiecutter.project_description}}

Project Structure
-----------------

Project structure are loosely based on
Clean Architecture, in three main Layers:

The Interface Layer
===================
This Layer regards about our **interaction
with AWS services.**
All code need to interact with AWS services are here.

Workflow: AWS Infrastructure -> Data Payload

The Application Layer
=====================
This layer regards about Domain **User Cases**.
All handlers are defined here.

Workflow: Data Payload -> Call Handler -> Get Schema -> Get RuleModel -> Execute User Case

The Enterprise Layer
====================
This layer regards about **Enterprise and
Business Rules** for Noverde and his Partners.
All models and Rules are defined here.

Workflow: Execute User Case -> Validate -> Persist -> Communicate
"""
from interface.initializers.log import initialize_log
from interface.initializers.sentry import initialize_sentry

initialize_sentry()  # Load first
initialize_log()
