# Blueprint Extensibility
This is a very basic example of how you could leverage Connection Infos in CloudBolt to connect to an external system, in this case Cisco ACI. This blueprint does not include the calls to ACI, but provides the building blocks necessary to get started with reaching out to an external system.

### Prerequisites
Create a connection info (Admin > Connection Info) in CloudBolt That is labeled with "aci"

Documentation and further examples for extending CloudBolt can be found below:
- https://docs.cloudbolt.io/articles/#!cloudbolt-latest-docs/advanced-option-returns
- https://docs.cloudbolt.io/articles/#!cloudbolt-latest-docs/resources-for-writing-plug-ins
- https://docs.cloudbolt.io/articles/#!cloudbolt-latest-docs/plug-in-parameterization
- https://docs.cloudbolt.io/articles/#!cloudbolt-latest-docs/plug-in-examples

From the Django documentation:
- https://docs.djangoproject.com/en/4.0/ref/models/querysets/

### This Blueprint shows how to:
- Pass a variable (aci) in to a CloudBolt Plugin
- Use generated options to create a dropdown list of Connection Infos labeled "aci"
- Use the run method as the insertion point to this plugin in a CloudBolt Blueprint
- Gather URL, username and password from a Connection Info
- Show how to do something, and write parameters back to the created resource
- These parameters can then be used to delete the things that were created from the blueprint
- Delete the created resource using the ID and Connection Info ID stored during provisioning. 

### To import the Blueprint in to a CloudBolt instance:
1. Download the aci_sample.zip file
2. Navigate to the *Catalog* tab
3. Select *Upload Blueprint*
4. Upload the aci_sample.zip file