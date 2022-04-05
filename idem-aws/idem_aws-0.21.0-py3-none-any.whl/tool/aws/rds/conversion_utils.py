from collections import OrderedDict
from typing import Any
from typing import Dict
from typing import List

"""
Util functions to convert raw resource state from AWS EC2 to present input format.
"""


def convert_raw_db_subnet_group_to_present(
    hub, resource: Dict[str, Any], tags: List = None, idem_resource_name: str = None
) -> Dict[str, Any]:
    new_resource = {}
    db_subnet_group_id = resource.get("DBSubnetGroupName")
    describe_parameters = OrderedDict(
        {
            "DBSubnetGroupDescription": "db_subnet_group_description",
            "DBSubnetGroupArn": "db_subnet_group_arn",
        }
    )
    new_resource = {"name": db_subnet_group_id, "resource_id": db_subnet_group_id}
    for parameter_old_key, parameter_new_key in describe_parameters.items():
        if resource.get(parameter_old_key) is not None:
            new_resource[parameter_new_key] = resource.get(parameter_old_key)
    if resource.get("Subnets"):
        subnets = []
        for each_subnet in resource.get("Subnets"):
            subnets.append(each_subnet.get("SubnetIdentifier"))

        new_resource["subnets"] = subnets
    if tags:
        new_resource["tags"] = tags
    return new_resource


def convert_raw_db_cluster_to_present(
    hub, raw_resource: Dict[str, Any], idem_resource_name: str = None
) -> Dict[str, Any]:

    resource_parameters = OrderedDict(
        {
            "AvailabilityZones": "availability_zone",
            "BackupRetentionPeriod": "backup_retention_period",
            "CharacterSetName": "character_set_name",
            "DatabaseName": "database_name",
            "DBClusterIdentifier": "db_cluster_identifier",
            "Engine": "engine",
            "EngineVersion": "engine_version",
            "Port": "port",
            "MasterUsername": "master_username",
            "PreferredBackupWindow": "preferred_backup_window",
            "PreferredMaintenanceWindow": "preferred_maintenance_window",
            "ReplicationSourceIdentifier": "replication_source_identifier",
            "StorageEncrypted": "storage_encrypted",
            "KmsKeyId": "kms_key_id",
            "BacktrackWindow": "backtrack_window",
            "EnableCloudwatchLogsExports": "enable_cloudwatch_logs_exports",
            "EngineMode": "engine_mode",
            "DeletionProtection": "deletion_protection",
            "CopyTagsToSnapshot": "copy_tags_to_snapshot",
            "DBClusterInstanceClass": "db_cluster_instance_class",
            "AllocatedStorage": "allocated_storage",
            "StorageType": "storage_type",
            "Iops": "iops",
            "PubliclyAccessible": "publicly_accessible",
            "AutoMinorVersionUpgrade": "auto_minor_version_upgrade",
            "MonitoringInterval": "monitoring_interval",
            "MonitoringRoleArn": "monitoring_role_arn",
            "PerformanceInsightsKMSKeyId": "performance_insights_kms_key_id",
            "PerformanceInsightsRetentionPeriod": "performance_insights_retention_period",
            "DBClusterParameterGroup": "db_cluster_parameter_group_name",
            "TagList": "tags",
            "ScalingConfigurationInfo": "scaling_configuration",
        }
    )
    resource_id = raw_resource.get("DBClusterIdentifier")
    resource_translated = {"name": idem_resource_name, "resource_id": resource_id}
    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource:
            resource_translated[parameter_present] = raw_resource.get(parameter_raw)

    if raw_resource.get("VpcSecurityGroups"):
        vpc_security_group_id = []
        for vpc_security_group in raw_resource.get("VpcSecurityGroups"):
            if "VpcSecurityGroupId" in vpc_security_group:
                vpc_security_group_id.append(
                    vpc_security_group.get("VpcSecurityGroupId")
                )
        resource_translated["vpc_security_group_ids"] = vpc_security_group_id

    if raw_resource.get("DBSubnetGroup"):
        db_subnet_group = raw_resource.get("DBSubnetGroup")
        if "DBSubnetGroupName" in db_subnet_group:
            resource_translated["db_subnet_group_name"] = db_subnet_group.get(
                "DBSubnetGroupName"
            )

    if raw_resource.get("DBClusterOptionGroupMemberships"):
        for option_group_membership in raw_resource.get(
            "DBClusterOptionGroupMemberships"
        ):
            resource_translated["option_group_name"] = option_group_membership.get(
                "DBClusterOptionGroupName"
            )
            break

    if raw_resource.get("DomainMemberships"):
        for domain_membership in raw_resource.get("DomainMemberships"):
            resource_translated["domain"] = domain_membership.get("Domain")
            resource_translated["domain_iam_role_name"] = domain_membership.get(
                "IAMRoleName"
            )
            break

    return resource_translated
