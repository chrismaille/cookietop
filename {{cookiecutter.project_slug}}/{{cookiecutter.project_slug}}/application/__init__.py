"""Application Layer.

This layer process the project User Cases.

This is the place for:
    * Handlers
    * Tasks
    * Schemas

Workflow
========
    (From) Payload -> (Call) Schema -> (Get) RuleModel -> (Run) User Cases.
"""

from interface.initializers.debugger import initialize_debug

initialize_debug()
