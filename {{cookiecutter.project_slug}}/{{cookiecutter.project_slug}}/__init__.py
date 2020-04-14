"""{{cookiecutter.project_name}} Project.

Main domain: {{cookiecutter.domain}}
Description: {{cookiecutter.project_description}}

Project Structure
-----------------

Project structure are loosely based on
Clean Architecture, in three main Layers:

The Interface Layer
===================
This Layer contain all code need to **interact
with AWS services.**
All AWS and Third Party libraries are handled here.


The Application Layer
=====================
This layer contain all code needed to
 process domain **User Cases**.
All Handlers, Tasks and Schemas are defined here.


The Enterprise Layer
====================
This layer contain all code about **Enterprise and
Business Rules** for Noverde and his Partners.
Primary Entity, his Models and all Rules Validation are defined here.


Workflow
========

    |Layer          | Flow                                  |
    |---------------|---------------------------------------|
    | Interface     | (From) AWS -> (Receive) Payload       |
    | Application   | (From) Payload -> (Call) Schema ->    |
    |               | (Get) RuleModel -> (Run) User Cases   |
    | Enterprise    | (From) User Cases -> (Run) Validate ->|
    |               | (Persist) Model -> (Communicate) Event|

"""
from interface.initializers.log import initialize_log
from interface.initializers.sentry import initialize_sentry

initialize_sentry()  # Load first
initialize_log()
