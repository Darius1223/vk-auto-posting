import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@require_POST
@csrf_exempt
def callback_view(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    type_ = data.get("type")
    group_id = data.get("group_id")
    print(f"{type_=} {group_id=}")

    if type_ == "confirmation" and group_id == 72502097:
        return HttpResponse("1b1b9ed1")

    return HttpResponse("OK")
