from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def indexapi(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def loginapi(request):
    if request.method == 'POST':
        return Response({"message": "Post Request", "data": request.data})
    return Response({"message": "Get Request"})


