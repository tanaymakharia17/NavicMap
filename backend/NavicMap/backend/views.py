
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *
from bson import ObjectId
from .optimal_path import *
import time


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    print("hello")
    if request.method == "POST":
        start_time = time.time()
        path = Path(
            startX=request.data["startX"],
            startY=request.data["startY"],
            endX=request.data["endX"],
            endY=request.data["endY"],
        )

        cnt = 100
        while cnt > 0:
            cnt -= 1
            ans = path.getOptimalPath()
        print(ans[0])
        response = {"path": ans[0], "distance": ans[1]}
        print("--- %s seconds ---" % (time.time() - start_time))
        return JsonResponse(response)

