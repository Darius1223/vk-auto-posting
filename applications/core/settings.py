import os

from applications.core import utils

VK_VERSION = "5.131"
VK_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
VK_OWNER_ID = os.getenv("GROUP_ID")

VK_CLIENT = utils.VKClient(
    access_token=VK_ACCESS_TOKEN,
    owner_id=VK_OWNER_ID,
)
