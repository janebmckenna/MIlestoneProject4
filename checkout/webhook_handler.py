from django.http import HttpResponse


class StripeWH_Handler:
    """ 
    Handle stripe webhooks
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ 
        Handle webhook events
        """
        return HttpResponse(
            content = f'Unhandled Webhook recieved: {event["type"]}',
            status = 200
        )
    
    def handle_payment_intent_succeeded(self, event):
        """ 
        Handle susccesful payment webhook event
        """
        intent = event.data.objects
        print(intent)
        return HttpResponse(
            content = f'Webhook recieved: {event["type"]}',
            status = 200
        )
    
    def handle_payment_intent_payment_failed(self, event):
        """ 
        Handle unsusccesful payment webhook event
        """
        return HttpResponse(
            content = f'Webhook recieved: {event["type"]}',
            status = 200
        )