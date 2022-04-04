from datetime import datetime, timedelta
import os.path
import uuid
from unittest import mock, skipIf

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.test import override_settings
from django.urls import reverse
from django.utils.timezone import make_aware, now
from rest_framework import status

from nautobot.dcim.models import (
    Device,
    DeviceRole,
    DeviceType,
    Manufacturer,
    Rack,
    RackGroup,
    RackRole,
    Site,
)
from nautobot.extras.api.views import JobViewSet
from nautobot.extras.choices import JobExecutionType, SecretsGroupAccessTypeChoices, SecretsGroupSecretTypeChoices
from nautobot.extras.models import (
    ComputedField,
    ConfigContext,
    ConfigContextSchema,
    CustomField,
    CustomLink,
    ExportTemplate,
    GitRepository,
    GraphQLQuery,
    ImageAttachment,
    JobLogEntry,
    JobResult,
    Relationship,
    RelationshipAssociation,
    ScheduledJob,
    Secret,
    SecretsGroup,
    SecretsGroupAssociation,
    Status,
    Tag,
    Webhook,
)
from nautobot.extras.jobs import Job, BooleanVar, IntegerVar, StringVar, ObjectVar
from nautobot.utilities.testing import APITestCase, APIViewTestCases
from nautobot.utilities.testing.utils import disable_warnings


User = get_user_model()


THIS_DIRECTORY = os.path.dirname(__file__)


class AppTest(APITestCase):
    def test_root(self):
        url = reverse("extras-api:api-root")
        response = self.client.get("{}?format=api".format(url), **self.header)

        self.assertEqual(response.status_code, 200)


#
#  Computed Fields
#


class ComputedFieldTest(APIViewTestCases.APIViewTestCase):
    model = ComputedField
    brief_fields = [
        "content_type",
        "description",
        "display",
        "fallback_value",
        "id",
        "label",
        "slug",
        "template",
        "url",
        "weight",
    ]
    create_data = [
        {
            "content_type": "dcim.site",
            "slug": "cf4",
            "label": "Computed Field 4",
            "template": "{{ obj.name }}",
            "fallback_value": "error",
        },
        {
            "content_type": "dcim.site",
            "slug": "cf5",
            "label": "Computed Field 5",
            "template": "{{ obj.name }}",
            "fallback_value": "error",
        },
        {
            "content_type": "dcim.site",
            "slug": "cf6",
            "label": "Computed Field 6",
            "template": "{{ obj.name }}",
        },
        {
            "content_type": "dcim.site",
            "label": "Computed Field 7",
            "template": "{{ obj.name }}",
            "fallback_value": "error",
        },
    ]
    update_data = {
        "content_type": "dcim.site",
        "slug": "cf1",
        "label": "My Computed Field",
    }
    bulk_update_data = {
        "description": "New description",
    }
    slug_source = "label"

    @classmethod
    def setUpTestData(cls):
        site_ct = ContentType.objects.get_for_model(Site)

        ComputedField.objects.create(
            slug="cf1",
            label="Computed Field One",
            template="{{ obj.name }}",
            fallback_value="error",
            content_type=site_ct,
        ),
        ComputedField.objects.create(
            slug="cf2",
            label="Computed Field Two",
            template="{{ obj.name }}",
            fallback_value="error",
            content_type=site_ct,
        ),
        ComputedField.objects.create(
            slug="cf3",
            label="Computed Field Three",
            template="{{ obj.name }}",
            fallback_value="error",
            content_type=site_ct,
        )

        cls.site = Site.objects.create(name="Site 1", slug="site-1")

    def test_computed_field_include(self):
        """Test that explicitly including a computed field behaves as expected."""
        self.add_permissions("dcim.view_site")
        url = reverse("dcim-api:site-detail", kwargs={"pk": self.site.pk})

        # First get the object without computed fields.
        response = self.client.get(url, **self.header)
        self.assertNotIn("computed_fields", response.json())

        # Now get it with computed fields.
        params = {"include": "computed_fields"}
        response = self.client.get(url, data=params, **self.header)
        self.assertIn("computed_fields", response.json())


class ConfigContextTest(APIViewTestCases.APIViewTestCase):
    model = ConfigContext
    brief_fields = ["display", "id", "name", "url"]
    create_data = [
        {
            "name": "Config Context 4",
            "data": {"more_foo": True},
        },
        {
            "name": "Config Context 5",
            "data": {"more_bar": False},
        },
        {
            "name": "Config Context 6",
            "data": {"more_baz": None},
        },
    ]
    bulk_update_data = {
        "description": "New description",
    }

    @classmethod
    def setUpTestData(cls):
        ConfigContext.objects.create(name="Config Context 1", weight=100, data={"foo": 123})
        ConfigContext.objects.create(name="Config Context 2", weight=200, data={"bar": 456})
        ConfigContext.objects.create(name="Config Context 3", weight=300, data={"baz": 789})

    def test_render_configcontext_for_object(self):
        """
        Test rendering config context data for a device.
        """
        manufacturer = Manufacturer.objects.create(name="Manufacturer 1", slug="manufacturer-1")
        devicetype = DeviceType.objects.create(manufacturer=manufacturer, model="Device Type 1", slug="device-type-1")
        devicerole = DeviceRole.objects.create(name="Device Role 1", slug="device-role-1")
        site = Site.objects.create(name="Site-1", slug="site-1")
        device = Device.objects.create(name="Device 1", device_type=devicetype, device_role=devicerole, site=site)

        # Test default config contexts (created at test setup)
        rendered_context = device.get_config_context()
        self.assertEqual(rendered_context["foo"], 123)
        self.assertEqual(rendered_context["bar"], 456)
        self.assertEqual(rendered_context["baz"], 789)

        # Add another context specific to the site
        configcontext4 = ConfigContext(name="Config Context 4", data={"site_data": "ABC"})
        configcontext4.save()
        configcontext4.sites.add(site)
        rendered_context = device.get_config_context()
        self.assertEqual(rendered_context["site_data"], "ABC")

        # Override one of the default contexts
        configcontext5 = ConfigContext(name="Config Context 5", weight=2000, data={"foo": 999})
        configcontext5.save()
        configcontext5.sites.add(site)
        rendered_context = device.get_config_context()
        self.assertEqual(rendered_context["foo"], 999)

        # Add a context which does NOT match our device and ensure it does not apply
        site2 = Site.objects.create(name="Site 2", slug="site-2")
        configcontext6 = ConfigContext(name="Config Context 6", weight=2000, data={"bar": 999})
        configcontext6.save()
        configcontext6.sites.add(site2)
        rendered_context = device.get_config_context()
        self.assertEqual(rendered_context["bar"], 456)

    def test_schema_validation_pass(self):
        """
        Given a config context schema
        And a config context that conforms to that schema
        Assert that the config context passes schema validation via full_clean()
        """
        schema = ConfigContextSchema.objects.create(
            name="Schema 1", slug="schema-1", data_schema={"type": "object", "properties": {"foo": {"type": "string"}}}
        )
        self.add_permissions("extras.add_configcontext")

        data = {"name": "Config Context with schema", "weight": 100, "data": {"foo": "bar"}, "schema": str(schema.pk)}
        response = self.client.post(self._get_list_url(), data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_201_CREATED)
        self.assertEqual(response.data["schema"]["id"], str(schema.pk))

    def test_schema_validation_fails(self):
        """
        Given a config context schema
        And a config context that *does not* conform to that schema
        Assert that the config context fails schema validation via full_clean()
        """
        schema = ConfigContextSchema.objects.create(
            name="Schema 1", slug="schema-1", data_schema={"type": "object", "properties": {"foo": {"type": "integer"}}}
        )
        self.add_permissions("extras.add_configcontext")

        data = {
            "name": "Config Context with bad schema",
            "weight": 100,
            "data": {"foo": "bar"},
            "schema": str(schema.pk),
        }
        response = self.client.post(self._get_list_url(), data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_400_BAD_REQUEST)


class ConfigContextSchemaTest(APIViewTestCases.APIViewTestCase):
    model = ConfigContextSchema
    brief_fields = ["display", "id", "name", "slug", "url"]
    create_data = [
        {
            "name": "Schema 4",
            "slug": "schema-4",
            "data_schema": {"type": "object", "properties": {"foo": {"type": "string"}}},
        },
        {
            "name": "Schema 5",
            "slug": "schema-5",
            "data_schema": {"type": "object", "properties": {"bar": {"type": "string"}}},
        },
        {
            "name": "Schema 6",
            "slug": "schema-6",
            "data_schema": {"type": "object", "properties": {"buz": {"type": "string"}}},
        },
        {
            "name": "Schema 7",
            "data_schema": {"type": "object", "properties": {"buz": {"type": "string"}}},
        },
    ]
    bulk_update_data = {
        "description": "New description",
    }
    choices_fields = []
    slug_source = "name"

    @classmethod
    def setUpTestData(cls):
        ConfigContextSchema.objects.create(
            name="Schema 1", slug="schema-1", data_schema={"type": "object", "properties": {"foo": {"type": "string"}}}
        ),
        ConfigContextSchema.objects.create(
            name="Schema 2", slug="schema-2", data_schema={"type": "object", "properties": {"bar": {"type": "string"}}}
        ),
        ConfigContextSchema.objects.create(
            name="Schema 3", slug="schema-3", data_schema={"type": "object", "properties": {"baz": {"type": "string"}}}
        ),


class ContentTypeTest(APITestCase):
    @override_settings(EXEMPT_VIEW_PERMISSIONS=["contenttypes.contenttype"])
    def test_list_objects(self):
        contenttype_count = ContentType.objects.count()

        response = self.client.get(reverse("extras-api:contenttype-list"), **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], contenttype_count)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["contenttypes.contenttype"])
    def test_get_object(self):
        contenttype = ContentType.objects.first()

        url = reverse("extras-api:contenttype-detail", kwargs={"pk": contenttype.pk})
        self.assertHttpStatus(self.client.get(url, **self.header), status.HTTP_200_OK)


class CreatedUpdatedFilterTest(APITestCase):
    def setUp(self):
        super().setUp()

        self.site1 = Site.objects.create(name="Test Site 1", slug="test-site-1")
        self.rackgroup1 = RackGroup.objects.create(site=self.site1, name="Test Rack Group 1", slug="test-rack-group-1")
        self.rackrole1 = RackRole.objects.create(name="Test Rack Role 1", slug="test-rack-role-1", color="ff0000")
        self.rack1 = Rack.objects.create(
            site=self.site1,
            group=self.rackgroup1,
            role=self.rackrole1,
            name="Test Rack 1",
            u_height=42,
        )
        self.rack2 = Rack.objects.create(
            site=self.site1,
            group=self.rackgroup1,
            role=self.rackrole1,
            name="Test Rack 2",
            u_height=42,
        )

        # change the created and last_updated of one
        Rack.objects.filter(pk=self.rack2.pk).update(
            last_updated=make_aware(datetime(2001, 2, 3, 1, 2, 3, 4)),
            created=make_aware(datetime(2001, 2, 3)),
        )

    def test_get_rack_created(self):
        self.add_permissions("dcim.view_rack")
        url = reverse("dcim-api:rack-list")
        response = self.client.get("{}?created=2001-02-03".format(url), **self.header)

        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["id"], str(self.rack2.pk))

    def test_get_rack_created_gte(self):
        self.add_permissions("dcim.view_rack")
        url = reverse("dcim-api:rack-list")
        response = self.client.get("{}?created__gte=2001-02-04".format(url), **self.header)

        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["id"], str(self.rack1.pk))

    def test_get_rack_created_lte(self):
        self.add_permissions("dcim.view_rack")
        url = reverse("dcim-api:rack-list")
        response = self.client.get("{}?created__lte=2001-02-04".format(url), **self.header)

        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["id"], str(self.rack2.pk))

    def test_get_rack_last_updated(self):
        self.add_permissions("dcim.view_rack")
        url = reverse("dcim-api:rack-list")
        response = self.client.get("{}?last_updated=2001-02-03%2001:02:03.000004".format(url), **self.header)

        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["id"], str(self.rack2.pk))

    def test_get_rack_last_updated_gte(self):
        self.add_permissions("dcim.view_rack")
        url = reverse("dcim-api:rack-list")
        response = self.client.get("{}?last_updated__gte=2001-02-04%2001:02:03.000004".format(url), **self.header)

        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["id"], str(self.rack1.pk))

    def test_get_rack_last_updated_lte(self):
        self.add_permissions("dcim.view_rack")
        url = reverse("dcim-api:rack-list")
        response = self.client.get("{}?last_updated__lte=2001-02-04%2001:02:03.000004".format(url), **self.header)

        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["id"], str(self.rack2.pk))


class CustomFieldTest(APIViewTestCases.APIViewTestCase):
    model = CustomField
    brief_fields = ["display", "id", "name", "url"]
    create_data = [
        {
            "content_types": ["dcim.site"],
            "name": "cf4",
            "type": "date",
        },
        {
            "content_types": ["dcim.site"],
            "name": "cf5",
            "type": "url",
        },
        {
            "content_types": ["dcim.site"],
            "name": "cf6",
            "type": "select",
        },
    ]
    update_data = {
        "content_types": ["dcim.site"],
        "name": "cf1",
        "label": "foo",
    }
    bulk_update_data = {
        "description": "New description",
    }
    choices_fields = ["filter_logic", "type"]

    @classmethod
    def setUpTestData(cls):
        site_ct = ContentType.objects.get_for_model(Site)

        custom_fields = (
            CustomField.objects.create(name="cf1", type="text"),
            CustomField.objects.create(name="cf2", type="integer"),
            CustomField.objects.create(name="cf3", type="boolean"),
        )
        for cf in custom_fields:
            cf.content_types.add(site_ct)


class CustomLinkTest(APIViewTestCases.APIViewTestCase):
    model = CustomLink
    brief_fields = ["content_type", "display", "id", "name", "url"]
    create_data = [
        {
            "content_type": "dcim.site",
            "name": "api-test-4",
            "text": "API customlink text 4",
            "target_url": "http://api-test-4.com/test4",
            "weight": 100,
            "new_window": False,
        },
        {
            "content_type": "dcim.site",
            "name": "api-test-5",
            "text": "API customlink text 5",
            "target_url": "http://api-test-5.com/test5",
            "weight": 100,
            "new_window": False,
        },
        {
            "content_type": "dcim.site",
            "name": "api-test-6",
            "text": "API customlink text 6",
            "target_url": "http://api-test-6.com/test6",
            "weight": 100,
            "new_window": False,
        },
    ]
    choices_fields = ["button_class"]

    @classmethod
    def setUpTestData(cls):
        obj_type = ContentType.objects.get_for_model(Site)

        CustomLink.objects.create(
            content_type=obj_type,
            name="api-test-1",
            text="API customlink text 1",
            target_url="http://api-test-1.com/test1",
            weight=100,
            new_window=False,
        )
        CustomLink.objects.create(
            content_type=obj_type,
            name="api-test-2",
            text="API customlink text 2",
            target_url="http://api-test-2.com/test2",
            weight=100,
            new_window=False,
        )
        CustomLink.objects.create(
            content_type=obj_type,
            name="api-test-3",
            text="API customlink text 3",
            target_url="http://api-test-3.com/test3",
            weight=100,
            new_window=False,
        )


class ExportTemplateTest(APIViewTestCases.APIViewTestCase):
    model = ExportTemplate
    brief_fields = ["display", "id", "name", "url"]
    create_data = [
        {
            "content_type": "dcim.device",
            "name": "Test Export Template 4",
            "template_code": "{% for obj in queryset %}{{ obj.name }}\n{% endfor %}",
        },
        {
            "content_type": "dcim.device",
            "name": "Test Export Template 5",
            "template_code": "{% for obj in queryset %}{{ obj.name }}\n{% endfor %}",
        },
        {
            "content_type": "dcim.device",
            "name": "Test Export Template 6",
            "template_code": "{% for obj in queryset %}{{ obj.name }}\n{% endfor %}",
        },
    ]
    bulk_update_data = {
        "description": "New description",
    }
    choices_fields = ["owner_content_type", "content_type"]

    @classmethod
    def setUpTestData(cls):
        ct = ContentType.objects.get_for_model(Device)

        ExportTemplate.objects.create(
            content_type=ct,
            name="Export Template 1",
            template_code="{% for obj in queryset %}{{ obj.name }}\n{% endfor %}",
        )
        ExportTemplate.objects.create(
            content_type=ct,
            name="Export Template 2",
            template_code="{% for obj in queryset %}{{ obj.name }}\n{% endfor %}",
        )
        ExportTemplate.objects.create(
            content_type=ct,
            name="Export Template 3",
            template_code="{% for obj in queryset %}{{ obj.name }}\n{% endfor %}",
        )


# Override the JOB_LOGS to None so that the Log Objects are created in the default database.
# This change is required as JOB_LOGS is a `fake` database pointed at the default. The django
# database cleanup will fail and cause tests to fail as this is not a real database.
@mock.patch("nautobot.extras.models.models.JOB_LOGS", None)
class GitRepositoryTest(APIViewTestCases.APIViewTestCase):
    model = GitRepository
    brief_fields = ["display", "id", "name", "url"]
    bulk_update_data = {
        "branch": "develop",
    }
    choices_fields = ["provided_contents"]
    slug_source = "name"

    @classmethod
    def setUpTestData(cls):
        secrets_groups = (
            SecretsGroup.objects.create(name="Secrets Group 1", slug="secrets-group-1"),
            SecretsGroup.objects.create(name="Secrets Group 2", slug="secrets-group-2"),
        )

        cls.repos = (
            GitRepository(
                name="Repo 1",
                slug="repo-1",
                remote_url="https://example.com/repo1.git",
                secrets_group=secrets_groups[0],
            ),
            GitRepository(
                name="Repo 2",
                slug="repo-2",
                remote_url="https://example.com/repo2.git",
                secrets_group=secrets_groups[0],
            ),
            GitRepository(name="Repo 3", slug="repo-3", remote_url="https://example.com/repo3.git"),
        )
        for repo in cls.repos:
            repo.save(trigger_resync=False)

        cls.create_data = [
            {
                "name": "New Git Repository 1",
                "slug": "new-git-repository-1",
                "remote_url": "https://example.com/newrepo1.git",
                "secrets_group": secrets_groups[1].pk,
            },
            {
                "name": "New Git Repository 2",
                "slug": "new-git-repository-2",
                "remote_url": "https://example.com/newrepo2.git",
                "secrets_group": secrets_groups[1].pk,
            },
            {
                "name": "New Git Repository 3",
                "slug": "new-git-repository-3",
                "remote_url": "https://example.com/newrepo3.git",
                "secrets_group": secrets_groups[1].pk,
            },
            {
                "name": "New Git Repository 4",
                "remote_url": "https://example.com/newrepo3.git",
                "secrets_group": secrets_groups[1].pk,
            },
        ]

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[])
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_git_sync_no_celery_worker(self, mock_get_worker_count):
        """Git sync cannot be triggered if Celery is not running."""
        mock_get_worker_count.return_value = 0
        self.add_permissions("extras.add_gitrepository")
        self.add_permissions("extras.change_gitrepository")
        url = reverse("extras-api:gitrepository-sync", kwargs={"pk": self.repos[0].id})
        response = self.client.post(url, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(response.data["detail"], "Unable to process request: Celery worker process not running.")

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[])
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_git_sync_nonexistent_repo(self, mock_get_worker_count):
        """Git sync request handles case of a nonexistent repository."""
        mock_get_worker_count.return_value = 1
        self.add_permissions("extras.add_gitrepository")
        self.add_permissions("extras.change_gitrepository")
        url = reverse("extras-api:gitrepository-sync", kwargs={"pk": "11111111-1111-1111-1111-111111111111"})
        response = self.client.post(url, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_404_NOT_FOUND)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[])
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_git_sync_without_permissions(self, mock_get_worker_count):
        """Git sync request verifies user permissions."""
        mock_get_worker_count.return_value = 1
        url = reverse("extras-api:gitrepository-sync", kwargs={"pk": self.repos[0].id})
        response = self.client.post(url, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[])
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_git_sync_with_permissions(self, mock_get_worker_count):
        """Git sync request can be submitted successfully."""
        mock_get_worker_count.return_value = 1
        self.add_permissions("extras.add_gitrepository")
        self.add_permissions("extras.change_gitrepository")
        url = reverse("extras-api:gitrepository-sync", kwargs={"pk": self.repos[0].id})
        response = self.client.post(url, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)

    def test_create_with_plugin_provided_contents(self):
        """Test that `provided_contents` published by a plugin works."""
        self.add_permissions("extras.add_gitrepository")
        self.add_permissions("extras.change_gitrepository")
        url = self._get_list_url()
        data = {
            "name": "plugin_test",
            "slug": "plugin-test",
            "remote_url": "https://localhost/plugin-test",
            "provided_contents": ["dummy_plugin.textfile"],
        }
        response = self.client.post(url, data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_201_CREATED)
        self.assertEqual(list(response.data["provided_contents"]), data["provided_contents"])


class GraphQLQueryTest(APIViewTestCases.APIViewTestCase):
    model = GraphQLQuery
    brief_fields = ["display", "id", "name", "url"]

    create_data = [
        {
            "name": "graphql-query-4",
            "slug": "graphql-query-4",
            "query": "{ query: sites {name} }",
        },
        {
            "name": "graphql-query-5",
            "slug": "graphql-query-5",
            "query": '{ devices(role: "edge") { id, name, device_role { name slug } } }',
        },
        {
            "name": "Graphql Query 6",
            "query": '{ devices(role: "edge") { id, name, device_role { name slug } } }',
        },
    ]
    slug_source = "name"

    @classmethod
    def setUpTestData(cls):
        cls.graphqlqueries = (
            GraphQLQuery(
                name="graphql-query-1",
                slug="graphql-query-1",
                query="{ sites {name} }",
            ),
            GraphQLQuery(
                name="graphql-query-2",
                slug="graphql-query-2",
                query='{ devices(role: "edge") { id, name, device_role { name slug } } }',
            ),
            GraphQLQuery(
                name="graphql-query-3",
                slug="graphql-query-3",
                query="""
query ($device: [String!]) {
  devices(name: $device) {
    config_context
    name
    position
    serial
    primary_ip4 {
      id
      primary_ip4_for {
        id
        name
      }
    }
    tenant {
      name
    }
    tags {
      name
      slug
    }
    device_role {
      name
    }
    platform {
      name
      slug
      manufacturer {
        name
      }
      napalm_driver
    }
    site {
      name
      slug
      vlans {
        id
        name
        vid
      }
      vlan_groups {
        id
      }
    }
    interfaces {
      description
      mac_address
      enabled
      name
      ip_addresses {
        address
        tags {
          id
        }
      }
      connected_circuit_termination {
        circuit {
          cid
          commit_rate
          provider {
            name
          }
        }
      }
      tagged_vlans {
        id
      }
      untagged_vlan {
        id
      }
      cable {
        termination_a_type
        status {
          name
        }
        color
      }
      tagged_vlans {
        site {
          name
        }
        id
      }
      tags {
        id
      }
    }
  }
}""",
            ),
        )

        for query in cls.graphqlqueries:
            query.full_clean()
            query.save()

    def test_run_saved_query(self):
        """Exercise the /run/ API endpoint."""
        self.add_permissions("extras.add_graphqlquery")
        self.add_permissions("extras.change_graphqlquery")
        self.add_permissions("extras.view_graphqlquery")

        url = reverse("extras-api:graphqlquery-run", kwargs={"pk": self.graphqlqueries[0].pk})
        response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)
        self.assertEqual({"data": {"sites": []}}, response.data)

        url = reverse("extras-api:graphqlquery-run", kwargs={"pk": self.graphqlqueries[2].pk})
        response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)
        self.assertEqual({"data": {"devices": []}}, response.data)


# TODO: Standardize to APIViewTestCase (needs create & update tests)
class ImageAttachmentTest(
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
):
    model = ImageAttachment
    brief_fields = ["display", "id", "image", "name", "url"]
    choices_fields = ["content_type"]

    @classmethod
    def setUpTestData(cls):
        ct = ContentType.objects.get_for_model(Site)

        site = Site.objects.create(name="Site 1", slug="site-1")

        ImageAttachment.objects.create(
            content_type=ct,
            object_id=site.pk,
            name="Image Attachment 1",
            image="http://example.com/image1.png",
            image_height=100,
            image_width=100,
        )
        ImageAttachment.objects.create(
            content_type=ct,
            object_id=site.pk,
            name="Image Attachment 2",
            image="http://example.com/image2.png",
            image_height=100,
            image_width=100,
        )
        ImageAttachment.objects.create(
            content_type=ct,
            object_id=site.pk,
            name="Image Attachment 3",
            image="http://example.com/image3.png",
            image_height=100,
            image_width=100,
        )


class JobTest(APITestCase):
    class TestJob(Job):
        class Meta:
            name = "Test job"

        var1 = StringVar()
        var2 = IntegerVar(required=True)  # explicitly stated, though required=True is the default in any case
        var3 = BooleanVar()
        var4 = ObjectVar(model=DeviceRole)

        def run(self, data, commit=True):
            self.log_debug(message=data["var1"])
            self.log_info(message=data["var2"])
            self.log_success(message=data["var3"])
            self.log_warning(message=data["var4"])

            return "Job complete"

    def get_test_job_class(self, class_path):
        if class_path == "local/test_api/TestJob":
            return self.TestJob
        raise Http404

    def setUp(self):
        super().setUp()

        # Monkey-patch the API viewset's _get_job_class method to return our test class above
        JobViewSet._get_job_class = self.get_test_job_class

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"], JOBS_ROOT=THIS_DIRECTORY)
    def test_list_jobs_anonymous(self):
        url = reverse("extras-api:job-list")
        response = self.client.get(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[], JOBS_ROOT=THIS_DIRECTORY)
    def test_list_jobs_without_permission(self):
        url = reverse("extras-api:job-list")
        with disable_warnings("django.request"):
            response = self.client.get(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[], JOBS_ROOT=THIS_DIRECTORY)
    @skipIf(
        "dummy_plugin" not in settings.PLUGINS,
        "dummy_plugin not in settings.PLUGINS",
    )
    def test_list_jobs_with_permission(self):
        self.add_permissions("extras.view_job")
        url = reverse("extras-api:job-list")
        response = self.client.get(url, **self.header)

        self.assertHttpStatus(response, status.HTTP_200_OK)
        # At a minimum, the job provided by the dummy plugin should be present
        self.assertNotEqual(response.data, [])
        self.assertIn(
            "plugins/dummy_plugin.jobs/DummyJob",
            [job["id"] for job in response.data],
        )

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"], JOBS_ROOT=THIS_DIRECTORY)
    def test_get_job_anonymous(self):
        url = reverse("extras-api:job-detail", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.get(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[], JOBS_ROOT=THIS_DIRECTORY)
    def test_get_job_without_permission(self):
        url = reverse("extras-api:job-detail", kwargs={"class_path": "local/test_api/TestJob"})
        with disable_warnings("django.request"):
            response = self.client.get(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[], JOBS_ROOT=THIS_DIRECTORY)
    def test_get_job_with_permission(self):
        self.add_permissions("extras.view_job")
        # Try GET to permitted object
        url = reverse("extras-api:job-detail", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.get(url, **self.header)

        self.assertHttpStatus(response, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.TestJob.name)
        self.assertEqual(response.data["vars"]["var1"], "StringVar")
        self.assertEqual(response.data["vars"]["var2"], "IntegerVar")
        self.assertEqual(response.data["vars"]["var3"], "BooleanVar")

        # Try GET to non-existent object
        url = reverse("extras-api:job-detail", kwargs={"class_path": "local/test_api/NoSuchJob"})
        response = self.client.get(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_404_NOT_FOUND)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[], JOBS_ROOT=THIS_DIRECTORY)
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_job_without_permission(self, mock_get_worker_count):
        """Job run request enforces user permissions."""
        mock_get_worker_count.return_value = 1
        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        with disable_warnings("django.request"):
            response = self.client.post(url, {}, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_job_no_worker(self, mock_get_worker_count):
        """Job run cannot be requested if Celery is not running."""
        mock_get_worker_count.return_value = 0
        self.add_permissions("extras.run_job")
        device_role = DeviceRole.objects.create(name="role", slug="role")
        job_data = {
            "var1": "FooBar",
            "var2": 123,
            "var3": False,
            "var4": device_role.pk,
        }

        data = {
            "data": job_data,
            "commit": True,
        }

        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.post(url, data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(response.data["detail"], "Unable to process request: Celery worker process not running.")

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"], JOBS_ROOT=THIS_DIRECTORY)
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_job_object_var(self, mock_get_worker_count):
        """Job run requests can reference objects by their primary keys."""
        mock_get_worker_count.return_value = 1
        self.add_permissions("extras.run_job")
        device_role = DeviceRole.objects.create(name="role", slug="role")
        job_data = {
            "var1": "FooBar",
            "var2": 123,
            "var3": False,
            "var4": device_role.pk,
        }

        data = {
            "data": job_data,
            "commit": True,
            "schedule": {
                "name": "test",
                "interval": "future",
                "start_time": str(datetime.now() + timedelta(minutes=1)),
            },
        }

        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.post(url, data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)

        job = ScheduledJob.objects.last()
        self.assertEqual(job.kwargs["data"]["var4"], str(device_role.pk))

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"], JOBS_ROOT=THIS_DIRECTORY)
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_job_object_var_lookup(self, mock_get_worker_count):
        """Job run requests can reference objects by their attributes."""
        mock_get_worker_count.return_value = 1
        self.add_permissions("extras.run_job")
        device_role = DeviceRole.objects.create(name="role", slug="role")
        job_data = {
            "var1": "FooBar",
            "var2": 123,
            "var3": False,
            "var4": {"name": "role"},
        }

        self.assertEqual(
            self.TestJob.deserialize_data(job_data),
            {"var1": "FooBar", "var2": 123, "var3": False, "var4": device_role},
        )

        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.post(url, {"data": job_data}, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"], JOBS_ROOT=THIS_DIRECTORY)
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_job_future(self, mock_get_worker_count):
        mock_get_worker_count.return_value = 1
        self.add_permissions("extras.run_job")
        d = DeviceRole.objects.create(name="role", slug="role")
        data = {
            "data": {"var1": "x", "var2": 1, "var3": False, "var4": d.pk},
            "commit": True,
            "schedule": {
                "start_time": str(datetime.now() + timedelta(minutes=1)),
                "interval": "future",
                "name": "test",
            },
        }

        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.post(url, data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"], JOBS_ROOT=THIS_DIRECTORY)
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_job_future_past(self, mock_get_worker_count):
        mock_get_worker_count.return_value = 1
        self.add_permissions("extras.run_job")
        d = DeviceRole.objects.create(name="role", slug="role")
        data = {
            "data": {"var1": "x", "var2": 1, "var3": False, "var4": d.pk},
            "commit": True,
            "schedule": {
                "start_time": str(datetime.now() - timedelta(minutes=1)),
                "interval": "future",
                "name": "test",
            },
        }

        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.post(url, data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_400_BAD_REQUEST)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"], JOBS_ROOT=THIS_DIRECTORY)
    @mock.patch("nautobot.extras.api.views.get_worker_count")
    def test_run_job_interval(self, mock_get_worker_count):
        mock_get_worker_count.return_value = 1
        self.add_permissions("extras.run_job")
        d = DeviceRole.objects.create(name="role", slug="role")
        data = {
            "data": {"var1": "x", "var2": 1, "var3": False, "var4": d.pk},
            "commit": True,
            "schedule": {
                "start_time": str(datetime.now() + timedelta(minutes=1)),
                "interval": "hourly",
                "name": "test",
            },
        }

        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.post(url, data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[], JOBS_ROOT=THIS_DIRECTORY)
    def test_run_job_with_invalid_data(self):
        self.add_permissions("extras.run_job")

        data = {
            "data": "invalid",
            "commit": True,
        }

        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.post(url, data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"errors": ["Job data needs to be a dict"]})

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[], JOBS_ROOT=THIS_DIRECTORY)
    def test_run_job_with_wrong_data(self):
        self.add_permissions("extras.run_job")
        job_data = {
            "var1": "FooBar",
            "var2": 123,
            "var3": False,
            "var5": "wrong",
        }

        data = {
            "data": job_data,
            "commit": True,
        }

        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.post(url, data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"errors": {"var5": ["Job data contained an unknown property"]}})

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[], JOBS_ROOT=THIS_DIRECTORY)
    def test_run_job_with_missing_data(self):
        self.add_permissions("extras.run_job")

        job_data = {
            "var1": "FooBar",
            "var3": False,
        }

        data = {
            "data": job_data,
            "commit": True,
        }

        url = reverse("extras-api:job-run", kwargs={"class_path": "local/test_api/TestJob"})
        response = self.client.post(url, data, format="json", **self.header)
        self.assertHttpStatus(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"errors": {"var2": ["This field is required."], "var4": ["This field is required."]}}
        )


class JobResultTest(APITestCase):
    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_delete_job_result_anonymous(self):
        url = reverse("extras-api:jobresult-detail", kwargs={"pk": 1})
        response = self.client.delete(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[])
    def test_delete_job_result_without_permission(self):
        url = reverse("extras-api:jobresult-detail", kwargs={"pk": 1})
        with disable_warnings("django.request"):
            response = self.client.delete(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[])
    def test_delete_job_result_with_permission(self):
        self.add_permissions("extras.delete_jobresult")
        job_result = JobResult.objects.create(
            name="test",
            job_id=uuid.uuid4(),
            obj_type=ContentType.objects.get_for_model(GitRepository),
        )
        url = reverse("extras-api:jobresult-detail", kwargs={"pk": job_result.pk})
        response = self.client.delete(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_204_NO_CONTENT)


class JobLogEntryTest(
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
):
    model = JobLogEntry
    brief_fields = [
        "absolute_url",
        "created",
        "grouping",
        "id",
        "job_result",
        "log_level",
        "log_object",
        "message",
        "url",
    ]
    choices_fields = []

    @classmethod
    def setUpTestData(cls):
        cls.job_result = JobResult.objects.create(
            name="test",
            job_id=uuid.uuid4(),
            obj_type=ContentType.objects.get_for_model(GitRepository),
        )

        for log_level in ("debug", "info", "success", "warning"):
            JobLogEntry.objects.create(
                log_level=log_level,
                grouping="run",
                job_result=cls.job_result,
                message=f"I am a {log_level} log.",
            )

    def test_list_job_logs_from_job_results_detail(self):
        """Test `logs` endpoint from `JobResult` detail."""
        self.add_permissions("extras.view_jobresult")
        url = reverse("extras-api:jobresult-logs", kwargs={"pk": self.job_result.pk})
        response = self.client.get(url, **self.header)
        self.assertEqual(len(response.json()), JobLogEntry.objects.count())

    def test_options_objects_returns_display_and_value(self):
        """Overridden because this test case is not applicable to this viewset."""

    def test_options_returns_expected_choices(self):
        """Overridden because this test case is not applicable to this viewset."""


class ScheduledJobTest(
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
):
    model = ScheduledJob
    brief_fields = ["interval", "name", "start_time"]
    choices_fields = []

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="user1", is_active=True)
        ScheduledJob.objects.create(
            name="test1",
            task="-",
            job_class="-",
            interval=JobExecutionType.TYPE_IMMEDIATELY,
            user=user,
            approval_required=True,
            start_time=now(),
        )
        ScheduledJob.objects.create(
            name="test2",
            task="-",
            job_class="-",
            interval=JobExecutionType.TYPE_IMMEDIATELY,
            user=user,
            approval_required=True,
            start_time=now(),
        )
        ScheduledJob.objects.create(
            name="test3",
            task="-",
            job_class="-",
            interval=JobExecutionType.TYPE_IMMEDIATELY,
            user=user,
            approval_required=True,
            start_time=now(),
        )

    def test_options_objects_returns_display_and_value(self):
        """Overriden because this test case is not applicable to this viewset"""

    def test_options_returns_expected_choices(self):
        """Overriden because this test case is not applicable to this viewset"""


class JobApprovalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="user1", is_active=True)
        cls.scheduled_job = ScheduledJob.objects.create(
            name="test",
            task="-",
            job_class="-",
            interval=JobExecutionType.TYPE_IMMEDIATELY,
            user=user,
            approval_required=True,
            start_time=now(),
        )

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_approve_job_anonymous(self):
        url = reverse("extras-api:scheduledjob-approve", kwargs={"pk": 1})
        response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_approve_job_without_permission(self):
        url = reverse("extras-api:scheduledjob-approve", kwargs={"pk": 1})
        with disable_warnings("django.request"):
            response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_approve_job_same_user(self):
        self.add_permissions("extras.run_job")
        self.add_permissions("extras.add_scheduledjob")
        scheduled_job = ScheduledJob.objects.create(
            name="test",
            task="-",
            job_class="-",
            interval=JobExecutionType.TYPE_IMMEDIATELY,
            user=self.user,
            approval_required=True,
            start_time=now(),
        )
        url = reverse("extras-api:scheduledjob-approve", kwargs={"pk": scheduled_job.pk})
        response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_approve_job(self):
        self.add_permissions("extras.run_job")
        self.add_permissions("extras.add_scheduledjob")
        url = reverse("extras-api:scheduledjob-approve", kwargs={"pk": self.scheduled_job.pk})
        response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_approve_job_in_past(self):
        self.add_permissions("extras.run_job")
        self.add_permissions("extras.add_scheduledjob")
        user = User.objects.get(username="user1")
        scheduled_job = ScheduledJob.objects.create(
            name="test",
            task="-",
            job_class="-",
            interval=JobExecutionType.TYPE_FUTURE,
            one_off=True,
            user=user,
            approval_required=True,
            start_time=now(),
        )
        url = reverse("extras-api:scheduledjob-approve", kwargs={"pk": scheduled_job.pk})
        response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_400_BAD_REQUEST)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_approve_job_in_past_force(self):
        self.add_permissions("extras.run_job")
        self.add_permissions("extras.add_scheduledjob")
        user = User.objects.get(username="user1")
        scheduled_job = ScheduledJob.objects.create(
            name="test",
            task="-",
            job_class="-",
            interval=JobExecutionType.TYPE_FUTURE,
            one_off=True,
            user=user,
            approval_required=True,
            start_time=now(),
        )
        url = reverse("extras-api:scheduledjob-approve", kwargs={"pk": scheduled_job.pk})
        response = self.client.post(url + "?force=true", **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_deny_job_without_permission(self):
        url = reverse("extras-api:scheduledjob-deny", kwargs={"pk": 1})
        with disable_warnings("django.request"):
            response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_deny_job(self):
        self.add_permissions("extras.run_job")
        self.add_permissions("extras.add_scheduledjob")
        url = reverse("extras-api:scheduledjob-deny", kwargs={"pk": self.scheduled_job.pk})
        response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)
        self.assertIsNone(ScheduledJob.objects.filter(pk=self.scheduled_job.pk).first())

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_dry_run_job_without_permission(self):
        url = reverse("extras-api:scheduledjob-dry-run", kwargs={"pk": 1})
        with disable_warnings("django.request"):
            response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_dry_run_job(self):
        self.add_permissions("extras.run_job")
        self.add_permissions("extras.add_scheduledjob")
        url = reverse("extras-api:scheduledjob-deny", kwargs={"pk": self.scheduled_job.pk})
        response = self.client.post(url, **self.header)
        self.assertHttpStatus(response, status.HTTP_200_OK)


class RelationshipTest(APIViewTestCases.APIViewTestCase):
    model = Relationship
    brief_fields = ["display", "id", "name", "slug", "url"]

    create_data = [
        {
            "name": "Device VLANs",
            "slug": "device-vlans",
            "type": "many-to-many",
            "source_type": "ipam.vlan",
            "destination_type": "dcim.device",
        },
        {
            "name": "Primary VLAN",
            "slug": "primary-vlan",
            "type": "one-to-many",
            "source_type": "ipam.vlan",
            "destination_type": "dcim.device",
        },
        {
            "name": "Primary Interface",
            "slug": "primary-interface",
            "type": "one-to-one",
            "source_type": "dcim.device",
            "source_label": "primary interface",
            "destination_type": "dcim.interface",
            "destination_hidden": True,
        },
        {
            "name": "Relationship 1",
            "type": "one-to-one",
            "source_type": "dcim.device",
            "source_label": "primary interface",
            "destination_type": "dcim.interface",
            "destination_hidden": True,
        },
    ]

    bulk_update_data = {
        "destination_filter": {"role": {"slug": "controller"}},
    }
    choices_fields = ["destination_type", "source_type", "type"]
    slug_source = "name"

    @classmethod
    def setUpTestData(cls):
        site_type = ContentType.objects.get_for_model(Site)
        device_type = ContentType.objects.get_for_model(Device)

        Relationship(
            name="Related Sites",
            slug="related-sites",
            type="many-to-many",
            source_type=site_type,
            destination_type=site_type,
        ).validated_save()
        Relationship(
            name="Unrelated Sites",
            slug="unrelated-sites",
            type="many-to-many",
            source_type=site_type,
            destination_type=site_type,
        ).validated_save()
        Relationship(
            name="Devices found elsewhere",
            slug="devices-elsewhere",
            type="many-to-many",
            source_type=site_type,
            destination_type=device_type,
        ).validated_save()


class RelationshipAssociationTest(APIViewTestCases.APIViewTestCase):
    model = RelationshipAssociation
    brief_fields = ["destination_id", "display", "id", "relationship", "source_id", "url"]
    choices_fields = ["destination_type", "source_type"]

    @classmethod
    def setUpTestData(cls):
        site_type = ContentType.objects.get_for_model(Site)
        device_type = ContentType.objects.get_for_model(Device)

        cls.relationship = Relationship(
            name="Devices found elsewhere",
            slug="elsewhere-devices",
            type="many-to-many",
            source_type=site_type,
            destination_type=device_type,
        )
        cls.relationship.validated_save()
        cls.sites = (
            Site.objects.create(name="Empty Site", slug="empty"),
            Site.objects.create(name="Occupied Site", slug="occupied"),
            Site.objects.create(name="Another Empty Site", slug="another-empty"),
        )
        manufacturer = Manufacturer.objects.create(name="Manufacturer 1", slug="manufacturer-1")
        devicetype = DeviceType.objects.create(manufacturer=manufacturer, model="Device Type 1", slug="device-type-1")
        devicerole = DeviceRole.objects.create(name="Device Role 1", slug="device-role-1")
        cls.devices = (
            Device.objects.create(name="Device 1", device_type=devicetype, device_role=devicerole, site=cls.sites[1]),
            Device.objects.create(name="Device 2", device_type=devicetype, device_role=devicerole, site=cls.sites[1]),
            Device.objects.create(name="Device 3", device_type=devicetype, device_role=devicerole, site=cls.sites[1]),
        )

        RelationshipAssociation(
            relationship=cls.relationship,
            source_type=site_type,
            source_id=cls.sites[0].pk,
            destination_type=device_type,
            destination_id=cls.devices[0].pk,
        ).validated_save()
        RelationshipAssociation(
            relationship=cls.relationship,
            source_type=site_type,
            source_id=cls.sites[0].pk,
            destination_type=device_type,
            destination_id=cls.devices[1].pk,
        ).validated_save()
        RelationshipAssociation(
            relationship=cls.relationship,
            source_type=site_type,
            source_id=cls.sites[0].pk,
            destination_type=device_type,
            destination_id=cls.devices[2].pk,
        ).validated_save()

        cls.create_data = [
            {
                "relationship": cls.relationship.pk,
                "source_type": "dcim.site",
                "source_id": cls.sites[2].pk,
                "destination_type": "dcim.device",
                "destination_id": cls.devices[0].pk,
            },
            {
                "relationship": cls.relationship.pk,
                "source_type": "dcim.site",
                "source_id": cls.sites[2].pk,
                "destination_type": "dcim.device",
                "destination_id": cls.devices[1].pk,
            },
            {
                "relationship": cls.relationship.pk,
                "source_type": "dcim.site",
                "source_id": cls.sites[2].pk,
                "destination_type": "dcim.device",
                "destination_id": cls.devices[2].pk,
            },
        ]


class SecretTest(APIViewTestCases.APIViewTestCase):
    model = Secret
    brief_fields = ["display", "id", "name", "slug", "url"]
    bulk_update_data = {}

    create_data = [
        {
            "name": "NAPALM Username",
            "provider": "environment-variable",
            "description": "Username for all NAPALM devices",
            "parameters": {
                "variable": "NAPALM_USERNAME",
            },
        },
        {
            "name": "NAPALM Password",
            "provider": "environment-variable",
            "parameters": {
                "variable": "NAPALM_PASSWORD",
            },
        },
        {
            "name": "GitHub Token for My Repository",
            "slug": "github-token-my-repository",
            "provider": "text-file",
            "parameters": {
                "path": "/github-tokens/user/myusername.txt",
            },
        },
    ]
    slug_source = "name"

    @classmethod
    def setUpTestData(cls):
        secrets = (
            Secret(
                name="api-test-1",
                provider="environment-variable",
                parameters={"variable": "API_TEST_1"},
            ),
            Secret(
                name="api-test-2",
                provider="environment-variable",
                parameters={"variable": "API_TEST_2"},
            ),
            Secret(
                name="api-test-3",
                provider="environment-variable",
                parameters={"variable": "API_TEST_3"},
            ),
        )

        for secret in secrets:
            secret.validated_save()


class SecretsGroupTest(APIViewTestCases.APIViewTestCase):
    model = SecretsGroup
    brief_fields = ["display", "id", "name", "slug", "url"]
    bulk_update_data = {}

    slug_source = "name"

    @classmethod
    def setUpTestData(cls):
        secrets = (
            Secret.objects.create(
                name="secret-1", provider="environment-variable", parameters={"variable": "SOME_VAR"}
            ),
            Secret.objects.create(
                name="secret-2", provider="environment-variable", parameters={"variable": "ANOTHER_VAR"}
            ),
        )

        secrets_groups = (
            SecretsGroup.objects.create(name="Group A", slug="group-a"),
            SecretsGroup.objects.create(name="Group B", slug="group-b"),
            SecretsGroup.objects.create(name="Group C", slug="group-c", description="Some group"),
        )

        SecretsGroupAssociation.objects.create(
            secret=secrets[0],
            group=secrets_groups[0],
            access_type=SecretsGroupAccessTypeChoices.TYPE_GENERIC,
            secret_type=SecretsGroupSecretTypeChoices.TYPE_SECRET,
        )
        SecretsGroupAssociation.objects.create(
            secret=secrets[1],
            group=secrets_groups[1],
            access_type=SecretsGroupAccessTypeChoices.TYPE_GENERIC,
            secret_type=SecretsGroupSecretTypeChoices.TYPE_SECRET,
        )

        cls.create_data = [
            {
                "name": "Secrets Group 1",
                "slug": "secrets-group-1",
                "description": "First Secrets Group",
            },
            {
                "name": "Secrets Group 2",
                "description": "Second Secrets Group",
            },
            {
                "name": "Secrets Group 3",
                "description": "Third Secrets Group",
            },
        ]


class SecretsGroupAssociationTest(APIViewTestCases.APIViewTestCase):
    model = SecretsGroupAssociation
    brief_fields = ["access_type", "display", "id", "secret", "secret_type", "url"]
    bulk_update_data = {}
    choices_fields = ["access_type", "secret_type"]

    @classmethod
    def setUpTestData(cls):
        secrets = (
            Secret.objects.create(
                name="secret-1", provider="environment-variable", parameters={"variable": "SOME_VAR"}
            ),
            Secret.objects.create(
                name="secret-2", provider="environment-variable", parameters={"variable": "ANOTHER_VAR"}
            ),
            Secret.objects.create(
                name="secret-3", provider="environment-variable", parameters={"variable": "YET_ANOTHER"}
            ),
        )

        secrets_groups = (
            SecretsGroup.objects.create(name="Group A", slug="group-a"),
            SecretsGroup.objects.create(name="Group B", slug="group-b"),
            SecretsGroup.objects.create(name="Group C", slug="group-c", description="Some group"),
        )

        SecretsGroupAssociation.objects.create(
            secret=secrets[0],
            group=secrets_groups[0],
            access_type=SecretsGroupAccessTypeChoices.TYPE_GENERIC,
            secret_type=SecretsGroupSecretTypeChoices.TYPE_SECRET,
        )
        SecretsGroupAssociation.objects.create(
            secret=secrets[1],
            group=secrets_groups[1],
            access_type=SecretsGroupAccessTypeChoices.TYPE_GENERIC,
            secret_type=SecretsGroupSecretTypeChoices.TYPE_SECRET,
        )
        SecretsGroupAssociation.objects.create(
            secret=secrets[2],
            group=secrets_groups[2],
            access_type=SecretsGroupAccessTypeChoices.TYPE_GENERIC,
            secret_type=SecretsGroupSecretTypeChoices.TYPE_SECRET,
        )

        cls.create_data = [
            {
                "group": secrets_groups[0].pk,
                "access_type": SecretsGroupAccessTypeChoices.TYPE_SSH,
                "secret_type": SecretsGroupSecretTypeChoices.TYPE_USERNAME,
                "secret": secrets[0].pk,
            },
            {
                "group": secrets_groups[1].pk,
                "access_type": SecretsGroupAccessTypeChoices.TYPE_SSH,
                "secret_type": SecretsGroupSecretTypeChoices.TYPE_USERNAME,
                "secret": secrets[1].pk,
            },
            {
                "group": secrets_groups[2].pk,
                "access_type": SecretsGroupAccessTypeChoices.TYPE_SSH,
                "secret_type": SecretsGroupSecretTypeChoices.TYPE_USERNAME,
                "secret": secrets[2].pk,
            },
        ]


class StatusTest(APIViewTestCases.APIViewTestCase):
    model = Status
    brief_fields = ["display", "id", "name", "slug", "url"]
    bulk_update_data = {
        "color": "000000",
    }

    create_data = [
        {
            "name": "Pizza",
            "slug": "pizza",
            "color": "0000ff",
            "content_types": ["dcim.device", "dcim.rack"],
        },
        {
            "name": "Oysters",
            "slug": "oysters",
            "color": "00ff00",
            "content_types": ["ipam.ipaddress", "ipam.prefix"],
        },
        {
            "name": "Bad combinations",
            "slug": "bad-combinations",
            "color": "ff0000",
            "content_types": ["dcim.device"],
        },
        {
            "name": "Status 1",
            "color": "ff0000",
            "content_types": ["dcim.device"],
        },
    ]
    slug_source = "name"

    @classmethod
    def setUpTestData(cls):
        """
        Since many `Status` objects are created as part of data migrations, we're
        testing against those. If this seems magical, it's because they are
        imported from `ChoiceSet` enum objects.

        This method is defined just so it's clear that there is no need to
        create test data for this test case.

        See `extras.management.create_custom_statuses` for context.
        """


class TagTest(APIViewTestCases.APIViewTestCase):
    model = Tag
    brief_fields = ["color", "display", "id", "name", "slug", "url"]
    create_data = [
        {
            "name": "Tag 4",
            "slug": "tag-4",
        },
        {
            "name": "Tag 5",
            "slug": "tag-5",
        },
        {
            "name": "Tag 6",
            "slug": "tag-6",
        },
    ]
    bulk_update_data = {
        "description": "New description",
    }

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="Tag 1", slug="tag-1")
        Tag.objects.create(name="Tag 2", slug="tag-2")
        Tag.objects.create(name="Tag 3", slug="tag-3")


class WebhookTest(APIViewTestCases.APIViewTestCase):
    model = Webhook
    brief_fields = ["display", "id", "name", "url"]
    create_data = [
        {
            "content_types": ["dcim.consoleport"],
            "name": "api-test-4",
            "type_create": True,
            "payload_url": "http://api-test-4.com/test4",
            "http_method": "POST",
            "http_content_type": "application/json",
            "ssl_verification": True,
        },
        {
            "content_types": ["dcim.consoleport"],
            "name": "api-test-5",
            "type_update": True,
            "payload_url": "http://api-test-5.com/test5",
            "http_method": "POST",
            "http_content_type": "application/json",
            "ssl_verification": True,
        },
        {
            "content_types": ["dcim.consoleport"],
            "name": "api-test-6",
            "type_delete": True,
            "payload_url": "http://api-test-6.com/test6",
            "http_method": "POST",
            "http_content_type": "application/json",
            "ssl_verification": True,
        },
    ]
    choices_fields = ["http_method"]

    @classmethod
    def setUpTestData(cls):
        webhooks = (
            Webhook(
                name="api-test-1",
                type_create=True,
                payload_url="http://api-test-1.com/test1",
                http_method="POST",
                http_content_type="application/json",
                ssl_verification=True,
            ),
            Webhook(
                name="api-test-2",
                type_update=True,
                payload_url="http://api-test-2.com/test2",
                http_method="POST",
                http_content_type="application/json",
                ssl_verification=True,
            ),
            Webhook(
                name="api-test-3",
                type_delete=True,
                payload_url="http://api-test-3.com/test3",
                http_method="POST",
                http_content_type="application/json",
                ssl_verification=True,
            ),
        )

        obj_type = ContentType.objects.get_for_model(DeviceType)

        for webhook in webhooks:
            webhook.save()
            webhook.content_types.set([obj_type])
