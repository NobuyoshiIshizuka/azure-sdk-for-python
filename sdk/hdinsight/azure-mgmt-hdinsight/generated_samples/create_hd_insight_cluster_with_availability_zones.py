# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.hdinsight import HDInsightManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hdinsight
# USAGE
    python create_hd_insight_cluster_with_availability_zones.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HDInsightManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subId",
    )

    response = client.clusters.begin_create(
        resource_group_name="rg1",
        cluster_name="cluster1",
        parameters={
            "properties": {
                "clusterDefinition": {
                    "configurations": {
                        "ambari-conf": {
                            "database-name": "{ambari database name}",
                            "database-server": "{sql server name}.database.windows.net",
                            "database-user-name": "**********",
                            "database-user-password": "**********",
                        },
                        "gateway": {
                            "restAuthCredential.isEnabled": True,
                            "restAuthCredential.password": "**********",
                            "restAuthCredential.username": "admin",
                        },
                        "hive-env": {
                            "hive_database": "Existing MSSQL Server database with SQL authentication",
                            "hive_database_name": "{hive metastore name}",
                            "hive_database_type": "mssql",
                            "hive_existing_mssql_server_database": "{hive metastore name}",
                            "hive_existing_mssql_server_host": "{sql server name}.database.windows.net",
                            "hive_hostname": "{sql server name}.database.windows.net",
                        },
                        "hive-site": {
                            "javax.jdo.option.ConnectionDriverName": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
                            "javax.jdo.option.ConnectionPassword": "**********!",
                            "javax.jdo.option.ConnectionURL": "jdbc:sqlserver://{sql server name}.database.windows.net;database={hive metastore name};encrypt=true;trustServerCertificate=true;create=false;loginTimeout=300;sendStringParametersAsUnicode=true;prepareSQL=0",
                            "javax.jdo.option.ConnectionUserName": "**********",
                        },
                        "oozie-env": {
                            "oozie_database": "Existing MSSQL Server database with SQL authentication",
                            "oozie_database_name": "{oozie metastore name}",
                            "oozie_database_type": "mssql",
                            "oozie_existing_mssql_server_database": "{oozie metastore name}",
                            "oozie_existing_mssql_server_host": "{sql server name}.database.windows.net",
                            "oozie_hostname": "{sql server name}.database.windows.net",
                        },
                        "oozie-site": {
                            "oozie.db.schema.name": "oozie",
                            "oozie.service.JPAService.jdbc.driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
                            "oozie.service.JPAService.jdbc.password": "**********",
                            "oozie.service.JPAService.jdbc.url": "jdbc:sqlserver://{sql server name}.database.windows.net;database={oozie metastore name};encrypt=true;trustServerCertificate=true;create=false;loginTimeout=300;sendStringParametersAsUnicode=true;prepareSQL=0",
                            "oozie.service.JPAService.jdbc.username": "**********",
                        },
                    },
                    "kind": "hadoop",
                },
                "clusterVersion": "3.6",
                "computeProfile": {
                    "roles": [
                        {
                            "hardwareProfile": {"vmSize": "standard_d3"},
                            "name": "headnode",
                            "osProfile": {
                                "linuxOperatingSystemProfile": {
                                    "password": "**********",
                                    "sshProfile": {"publicKeys": [{"certificateData": "**********"}]},
                                    "username": "sshuser",
                                }
                            },
                            "targetInstanceCount": 2,
                            "virtualNetworkProfile": {
                                "id": "/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/vnetname",
                                "subnet": "/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/vnetname/subnets/vnetsubnet",
                            },
                        },
                        {
                            "hardwareProfile": {"vmSize": "standard_d3"},
                            "name": "workernode",
                            "osProfile": {
                                "linuxOperatingSystemProfile": {
                                    "password": "**********",
                                    "sshProfile": {"publicKeys": [{"certificateData": "**********"}]},
                                    "username": "sshuser",
                                }
                            },
                            "targetInstanceCount": 2,
                            "virtualNetworkProfile": {
                                "id": "/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/vnetname",
                                "subnet": "/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/vnetname/subnets/vnetsubnet",
                            },
                        },
                    ]
                },
                "osType": "Linux",
                "storageProfile": {
                    "storageaccounts": [
                        {
                            "container": "containername",
                            "isDefault": True,
                            "key": "storage account key",
                            "name": "mystorage",
                        }
                    ]
                },
            },
            "zones": ["1"],
        },
    ).result()
    print(response)


# x-ms-original-file: specification/hdinsight/resource-manager/Microsoft.HDInsight/stable/2021-06-01/examples/CreateHDInsightClusterWithAvailabilityZones.json
if __name__ == "__main__":
    main()
