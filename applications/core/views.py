import json

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from loguru import logger

from applications.core import entities
from applications.core.settings import VK_CLIENT


@require_POST
@csrf_exempt
def callback_view(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    type_req = data.get("type")
    group_id = data.get("group_id")
    logger.debug(f"{type_req=} {group_id=}")

    if type_req == "confirmation":
        logger.info("Is confirmation request")
        if group_id == 72502097:
            return HttpResponse("1b1b9ed1")
        else:
            return HttpResponseBadRequest("Group ID is not corrected")
    elif type_req == "wall_post_new":
        logger.info("Is wall_post_new request")
        post_data = data.get("object")
        post = entities.VKPost(**post_data)
        logger.debug(f"{post=}")

        if post.post_type == "suggest":
            VK_CLIENT.wall_post(post_id=post.id, from_group=1)

    return HttpResponse("OK")
