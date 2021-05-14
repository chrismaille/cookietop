from stela import settings
from helpers.get_now import get_time_now
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.attributes import UTCDateTimeAttribute


class {{cookiecutter.model_name_camel}}CreatedIndex(GlobalSecondaryIndex):  # type: ignore
    class Meta:
        index_name = "created_date_index"
        read_capacity_units = settings["project.capacity.read"]
        write_capacity_units = settings["project.capacity.write"]
        projection = AllProjection()

    created_at = UTCDateTimeAttribute(default=get_time_now, hash_key=True)
