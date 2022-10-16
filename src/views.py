from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.



@csrf_exempt
def index(request):
    if request.method == 'GET':
        session_id = request.GET.get('sessionId')
        service_code = request.GET.get('serviceCode')
        admission_number = request.GET.get('admissionnumber')
        text = request.GET.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to QuickSoma. Enter your admission\n"
            # response .= "1. My Account \n"
            response += "1. My Admission Number"

        elif text == "1":
            response = "END My Admission number is {0}".format(admission_number)



        elif text == "1":
            response = "CON Get smarter in Mathematics today with QuickSoma \n"
            response += "1. Choose topic for revision\n"
        elif text == "1*1":
            response = "CON  Topics\n"
            response += "1. Area\n"
            response += "2. Indices \n"
        elif text == "1*1*1":
            response = "CON  Attempt the following questions \n"
            response += "1. What is the area of a square whose side is 6cm (Tip:Area=s*s) \n"
          
        elif text == "1*1*1*1":
            response += "CON 1. Choose the correct answer\n"
        elif text == "1*1*1*1*1":
            response = "CON Choose the type of bill you pay \n"
            response += "1. 20cm \n"
            response += "2. 38cm \n"
            response += "3. 36cm^2 \n"
            response += "4. 40cm^2 \n"
        elif text == "1*1*1*1*1*3":
            response = "CON Congratulations for revising with QuickSoma.The correct answer is 36cm^2.To continue revising press 0 to go back to revision questions \n"
         
            
        return HttpResponse(response)
    return HttpResponse({"message": "this method requires a POST request"})