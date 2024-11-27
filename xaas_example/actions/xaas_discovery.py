"""
Sample Discovery Plugin for XaaS Example Blueprint. This creates two sample
resources for each Connection Info labeled "xaas".
"""
from common.methods import set_progress
from utilities.models import ConnectionInfo

RESOURCE_IDENTIFIER = 'xaas_resource_id'
CONN_INFO_LABEL = "xaas"


def discover_resources(**kwargs):
    discovered_resources = []
    conn_infos = ConnectionInfo.objects.filter(labels__name=CONN_INFO_LABEL)
    for conn_info in conn_infos:
        set_progress('Discovering XaaS Resources')
        discovered_resources = get_resources_for_conn_info(
            conn_info,
            discovered_resources
        )

    return discovered_resources


def get_resources_for_conn_info(conn_info, discovered_resources):
    """
    This function is where you would use the connection info to connect to an
    external service and get a list of resources. You would then loop through
    each resource and create a dictionary with the relevant keys.
    :param conn_info:
    :param discovered_resources:
    :return:
    """
    discovered_resources.append({
        "name": f"XaaS Example 2",
        "xaas_resource_id": "2",
        "xaas_conn_info": conn_info.id})
    discovered_resources.append({
        "name": f"XaaS Example 3",
        "xaas_resource_id": "3",
        "xaas_conn_info": conn_info.id})
    return discovered_resources
