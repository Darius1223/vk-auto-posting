from urllib.parse import urlencode

import requests
from loguru import logger

import applications.core.settings as settings


class VKClient:
    """VK Api utils"""

    def __init__(self, access_token: str, owner_id: str):
        if not access_token:
            raise NotImplementedError("Access token is None")
        self._access_token = access_token
        if not owner_id:
            raise NotImplementedError("Owner ID is None")
        self._owner_id = owner_id

        self._api_version = settings.VK_VERSION

    def _create_params(self, **kwargs) -> str:
        params = kwargs
        params["v"] = self._api_version
        params["access_token"] = self._access_token
        params["owner_id"] = self._owner_id
        return urlencode(kwargs)

    def _create_request_url(self, method: str, **kwargs) -> str:
        params = self._create_params(**kwargs)
        url = f"https://api.vk.com/method/{method}?{params}"
        return url

    def wall_post(self, post_id: int, from_group: int):
        method = "wall.post"
        if not post_id:
            raise NotImplementedError("Post ID is None")
        url = self._create_request_url(method=method, post_id=post_id, from_group=from_group)
        response = requests.post(url)
        logger.info(f"{response=}")
