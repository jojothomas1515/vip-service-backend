import random
import string

from sqlalchemy import UniqueConstraint
from sqlmodel import Field

from common import UUIDModel, TimestampModel


def get_random_string(length):
    """
    create a random alphaNumeric string to be used as the apikey
    @param length: used to specify the  length of the required
    alphaNum string
    """
    letters = string.ascii_lowercase
    numbers = string.digits
    alphaNum = letters + numbers
    result_str = "".join(random.choice(alphaNum) for i in range(length))
    return result_str


class ApiKey(UUIDModel, TimestampModel, table=True):
    __tablename__ = "apikey"
    __table_args__ = (UniqueConstraint("apikey"),)
    apikey: str = Field(default=get_random_string(30))

    user_id: str = Field(default=None, foriegn_key="user.id")

    def __repr__(self):
        return f"apikey: {self.apikey}"
