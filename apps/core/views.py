from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


@require_POST
def callback_view(request: HttpRequest) -> HttpResponse:
    data = request.POST
    type = data.get("type")
    group_id = data.get("group_id")
    print(f"{type=} {group_id=}")
    return HttpResponse("OK")
