from flask import request
from flask_login import current_user
from flask_potion import ModelResource
from flask_potion.routes import Route
from flask_potion.instances import Instances

from pgscm.db import models


class RoleResource(ModelResource):
    class Meta:
        model = models.Role

    @Route.GET('', rel="instances")
    def instances(self, **kwargs):
        return self.manager.paginated_instances(**kwargs)
    instances.request_schema = instances.response_schema = Instances()

class UserResource(ModelResource):
    class Meta:
        model = models.User


def init_resources(api):
    api.add_resource(RoleResource)
    api.add_resource(UserResource)
