.. _story_runnerindex:

Story Runner
.....................

A runner attribute of the archivist instance allows running scenarios from
a dictionary. Usually the dictionary is read from a yaml or json file.

.. literalinclude:: ../../archivist/cmds/runner/run.py
   :language: python


This functionality is also available as a CLI 'archivist_runner'. After 
installation of the python wheel execute

.. code-block:: shell

   $ archivist_runner -h

to elucidate options.

To invoke this command:

    - obtain bearer token and put in file 'credentials/token'
    - choose which yaml file to use
    - get the URL of your Archivist instance

Execute:

.. code-block:: shell

   $ archivist_runner \
         -u https://app.rkvst.io \
         -t credentials/token \
         functests/test_resources/richness_story.yaml

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   generic
   assets_count
   assets_create
   assets_create_if_not_exists
   assets_list
   compliance_compliant_at
   compliance_policies_create
   composite_estate_info
   events_count
   events_create
   events_list
   locations_count
   
   compliance_policies_demo
   compliance_policies_demo_dynamic_tolerance
   compliance_policies_demo_richness
   door_entry_demo
   estate_info_demo