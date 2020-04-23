"""Create {{cookiecutter.domain}} State Machine.

This is very simple Step Functions example.

Current Flow:

<1. Find Step>
        |-> <Instance Exists?>
                    |-No->  <2a. Create Step> -|-->> <Success>
                    |-Yes-> <2b. Update Step> -|

Check on AWS Step Function console for detailed view.
"""
