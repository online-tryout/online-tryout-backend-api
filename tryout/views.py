import os
import pika
from django.http import JsonResponse
from urllib.parse import urlparse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def health_check(request):
    return JsonResponse({'message': 'tryout api is running'}, status=200)

@csrf_exempt
def create_tryout(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        success = publish_to_rabbitmq(message=body_unicode)
        if success:
            return JsonResponse({'message': 'success to publish into rabbit mq'}, status=200)
        else:
            return JsonResponse({'message': 'failed to publish into rabbit mq'}, status=500)
    else:
        return JsonResponse({'message': 'only post requests are allowed for this endpoint'}, status=405)



def publish_to_rabbitmq(message) -> bool:
    rabbit_source = os.getenv('RABBIT_SOURCE')
    
    parsed_url = urlparse(rabbit_source)
    credentials = pika.PlainCredentials(parsed_url.username, parsed_url.password)
    port = parsed_url.port or 5672
    parameters = pika.ConnectionParameters(parsed_url.hostname, port, '/', credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    queue_name = "parsing-sheets-queue"
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    connection.close()

    return True
