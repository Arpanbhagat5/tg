from django.http import HttpResponse


def home_view(request):
    return HttpResponse(
        "<h1>Welcome TG</h1>"
        "<p>For the Problem 1, go to <a href='http://localhost:8000/api/register/'>http://localhost:8000/api/register/</a></p>"
        "<p>For the Problem 2, go to <a href='http://localhost:3000/'>http://localhost:3000/</a></p>"
        "<p>For the Problem 3, go to <a href='http://localhost:8000/api/users/'>http://localhost:8000/api/users/</a></p>"
        "<p>For checking registred user data, go to <a href='http://localhost:8000/admin/'>http://localhost:8000/admin/</a></p>"
        "<p>For checking prefecture data, go to <a href='http://localhost:8000/api/prefectures/'>http://localhost:8000/api/prefectures/</a></p>"
    )
