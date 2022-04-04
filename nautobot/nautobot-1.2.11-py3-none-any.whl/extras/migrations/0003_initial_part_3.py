# Generated by Django 3.1.7 on 2021-04-01 06:35

from django.db import migrations, models
import django.db.models.deletion
import nautobot.extras.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("tenancy", "0001_initial"),
        ("virtualization", "0001_initial"),
        ("dcim", "0004_initial_part_4"),
        ("extras", "0002_initial_part_2"),
    ]

    operations = [
        migrations.AddField(
            model_name="configcontext",
            name="cluster_groups",
            field=models.ManyToManyField(
                blank=True, related_name="_configcontext_cluster_groups_+", to="virtualization.ClusterGroup"
            ),
        ),
        migrations.AddField(
            model_name="configcontext",
            name="clusters",
            field=models.ManyToManyField(
                blank=True, related_name="_configcontext_clusters_+", to="virtualization.Cluster"
            ),
        ),
        migrations.AddField(
            model_name="configcontext",
            name="owner_content_type",
            field=models.ForeignKey(
                blank=True,
                default=None,
                limit_choices_to=nautobot.extras.utils.FeatureQuery("config_context_owners"),
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="configcontext",
            name="platforms",
            field=models.ManyToManyField(blank=True, related_name="_configcontext_platforms_+", to="dcim.Platform"),
        ),
        migrations.AddField(
            model_name="configcontext",
            name="regions",
            field=models.ManyToManyField(blank=True, related_name="_configcontext_regions_+", to="dcim.Region"),
        ),
        migrations.AddField(
            model_name="configcontext",
            name="roles",
            field=models.ManyToManyField(blank=True, related_name="_configcontext_roles_+", to="dcim.DeviceRole"),
        ),
        migrations.AddField(
            model_name="configcontext",
            name="sites",
            field=models.ManyToManyField(blank=True, related_name="_configcontext_sites_+", to="dcim.Site"),
        ),
        migrations.AddField(
            model_name="configcontext",
            name="tags",
            field=models.ManyToManyField(blank=True, related_name="_configcontext_tags_+", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="configcontext",
            name="tenant_groups",
            field=models.ManyToManyField(
                blank=True, related_name="_configcontext_tenant_groups_+", to="tenancy.TenantGroup"
            ),
        ),
        migrations.AddField(
            model_name="configcontext",
            name="tenants",
            field=models.ManyToManyField(blank=True, related_name="_configcontext_tenants_+", to="tenancy.Tenant"),
        ),
        migrations.AlterUniqueTogether(
            name="webhook",
            unique_together={("payload_url", "type_create", "type_update", "type_delete")},
        ),
        migrations.AlterIndexTogether(
            name="taggeditem",
            index_together={("content_type", "object_id")},
        ),
        migrations.AlterUniqueTogether(
            name="relationshipassociation",
            unique_together={("relationship", "source_type", "source_id", "destination_type", "destination_id")},
        ),
        migrations.AlterUniqueTogether(
            name="exporttemplate",
            unique_together={("content_type", "name", "owner_content_type", "owner_object_id")},
        ),
        migrations.AlterUniqueTogether(
            name="customfieldchoice",
            unique_together={("field", "value")},
        ),
        migrations.AlterUniqueTogether(
            name="configcontext",
            unique_together={("name", "owner_content_type", "owner_object_id")},
        ),
    ]
