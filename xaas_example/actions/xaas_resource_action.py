"""
This is a very basic example of how to add a Day-2 action to a Resource in
CloudBolt. This Day-2 action prompts the requester to enter their email address
and then sends an email to that address including the Resource ID and the
Connection Info ID.

Prerequisites:
CloudBolt must be configured to send emails. See the following documentation
for more information on how to set up your SMTP information:
https://docs.cloudbolt.io/articles/cloudbolt-latest-docs/email/a/h2__1320815144

"""
from utilities.mail import email

EMAIL_ADDRESS = "{{email_address}}"

def run(job, resource: None, **kwargs):
    conn_info_id = resource.get_cfv_for_custom_field("xaas_conn_info").value
    resource_id = resource.get_cfv_for_custom_field("xaas_resource_id").value
    email(
        recipients=[EMAIL_ADDRESS],
        context={
            'subject': 'XaaS Day-2 Action',
            'message': f'Your XaaS Resource ID is {resource_id} and your '
                       f'Connection Info ID is {conn_info_id}',
        }
    )
    return "SUCCESS", "", ""
