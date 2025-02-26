from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.forms import CustomUserCreationForm
from users.models import CustomUser, Pref
from users.serializers import PrefectureSerializer, UserSerializer


# problem 1: using django form
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect("success")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


# problem 1: using django form
def success(request):
    return render(request, "users/success.html")


# common to problem 1,2,3
class PrefectureListView(ModelViewSet):
    queryset = Pref.objects.all()
    serializer_class = PrefectureSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Check if password is provided
        if "password" in request.data:
            # Hash the password before saving
            request.data["password"] = make_password(request.data["password"])

        # Call the superclass to handle create
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # other methods like update and destry can be kept here
