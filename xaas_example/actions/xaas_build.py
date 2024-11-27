"""
This is a very basic example of how you could leverage Connection Infos in
CloudBolt to connect to an external system to provision something. There is no
functional code here, the framework will need to be filled in. This is what
CloudBolt refers to as Anything as a Service (XaaS).

Pre-requisites:
- Create a connection info (Admin > Connection Info) in CloudBolt That is
  labeled with "xaas"

Documentation and further examples can be found below:
https://docs.cloudbolt.io/articles/#!cloudbolt-latest-docs/advanced-option-returns
https://docs.cloudbolt.io/articles/#!cloudbolt-latest-docs/resources-for-writing-plug-ins
https://docs.cloudbolt.io/articles/#!cloudbolt-latest-docs/plug-in-parameterization
https://docs.cloudbolt.io/articles/#!cloudbolt-latest-docs/plug-in-examples

And from the Django documentation:
https://docs.djangoproject.com/en/4.0/ref/models/querysets/

This plugin shows how to:
1. Pass variables in to a CloudBolt Plugin
2. Use generated options to create a dropdown list of Connection Infos labeled
   "xaas"
3. Use the run method as the insertion point to this plugin in a CloudBolt
   Blueprint
4. Gather URL, username and password from a Connection Info
5. Show how to do something, and write parameters back to the created resource
6. These parameters can then be used to delete the things that were created
   from the blueprint
"""
from c2_wrapper import create_custom_field
from common.methods import set_progress
from infrastructure.models import CustomField
from utilities.models import ConnectionInfo

CONN_INFO_ID = "{{endpoint}}"
INPUT_1 = "{{input_1}}"
INPUT_2 = "{{input_2}}"
CONN_INFO_LABEL = "xaas"


def generate_options_for_endpoint(server=None, **kwargs):
    conn_infos = ConnectionInfo.objects.filter(labels__name=CONN_INFO_LABEL)
    options = [(ci.id, ci.name) for ci in conn_infos]
    if not options:
        options = [('', f'------No Connection Infos Found with Label "{CONN_INFO_LABEL}"------')]
    return options


def run(job, resource: None, **kwargs):
    if resource:
        try:
            set_progress(f'kwargs: {kwargs}')
            resource_id = create_resource()
            save_info_to_resource(resource, resource_id)
            return "SUCCESS", "", ""
        except Exception as err:
            return "FAILURE", err, ""
    else:
        return "FAILURE", "Resource not found", ""


def create_resource():
    base_url, username, password = get_conn_info_data()
    set_progress(f'Submitting request against: {base_url}')
    """
    This action could look something more like the following, note it is using 
    the global parameters set for input_1 and input_2 to pass in to the 
    post function. Instead of basic auth, you could also use token based auth. 
    You can also construct this to handle async REST calls to check the status 
    of a request until it is complete: 
    
    import requests
    from requests.auth import HTTPBasicAuth
    path = '/api/createResource/'
    verify_certs = True
    json_payload = {
        "input_1": INPUT_1,
        "input_2": INPUT_2
    }
    response = requests.post(
        f'{base_url}{path},
        auth=HTTPBasicAuth(username, password),
        verify=verify_certs,
        json=json_payload
    )
    response.raise_for_status()
    response_json = response.json()
    resource_id = response_json["id"]
    """
    resource_id = "1"
    return resource_id


def save_info_to_resource(resource, resource_id):
    """
    Save the Connection Info ID and the created Resource ID to the Resource in
    CloudBolt. If more than one element is created, you could save multiple
    IDs and other metadata to the Resource.
    """
    cf = create_custom_field("xaas_conn_info", "XaaS Connection Info", "STR",
                             description="Connection Info for XaaS",
                             show_as_attribute=True)
    resource.set_value_for_custom_field(cf.name, CONN_INFO_ID)
    cf = create_custom_field("xaas_resource_id", "XaaS Resource ID", "STR",
                             description="ID for the created XaaS network",
                             show_as_attribute=True)
    resource.set_value_for_custom_field(cf.name, resource_id)


def get_conn_info_data():
    ci = ConnectionInfo.objects.get(id=CONN_INFO_ID)
    username = ci.username
    password = ci.password
    base_url = f'{ci.protocol}://{ci.ip}'
    if ci.port:
        base_url = f'{base_url}:{ci.port}'
    return base_url, username, password
