from rest_framework.response import Response

def response(data, status=200):
    return Response({
        "statusCode": status,
        "data": data
    }, status=status)