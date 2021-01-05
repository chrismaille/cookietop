"""{{cookiecutter.project_name}} Project.

Main domain: {{cookiecutter.project_name}}
Description: {{cookiecutter.project_description}}  # noqa: E501

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
This layer contain all Rule models.
Unique microservice model/entity is created here.


Workflow
========

    |Layer          | Flow                                  |
    |---------------|---------------------------------------|
    | Interface     | (From) AWS -> (Receive) Payload       |
    | Application   | (From) Payload -> (Call) Schema ->    |
    |               | (Get) Model -> (Run) User Cases   |
    | Enterprise    | (From) User Cases -> (Run) Validate ->|
    |               | (Persist) Model -> (Communicate) Event|

"""
from interface.initializers.sentry import initialize_sentry

initialize_sentry()  # Load first
