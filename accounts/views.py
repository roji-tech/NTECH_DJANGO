from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from accounts.serializers import UserCreateSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
# Create your views here.
User = get_user_model()


class RegistrationView(CreateView):
    # fields = ["username", "first_name", "last_name", "email", "password"]
    form_class = UserCreationForm
    success_url = "/"
    template_name = "accounts/register.html"
    queryset = User.objects .all()
    # http_method_names

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print("GET request received")
        # return render(request, "accounts/register.html", {"form": self.get_form()})
        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print("POST request received with data:")
        # super().post(request, *args, **kwargs)
        User.objects.create_user(
            username=request.POST.get("username"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            password=request.POST.get("password1")
        )
        return render(request, "accounts/register.html", {"form": self.get_form()})


@method_decorator(login_required, name="dispatch")
class UsersList(ListView):
    queryset = User.objects.all()
    template_name = "accounts/users.html"
    # context_object_name = "users"


def user_detail(request, pk):
    if request.method == "POST":
        print("POST request received for user detail")
        # Handle POST request if needed
        pass

    if request.method == "GET":
        print("GET request received for user detail")
        # Handle GET request if needed
        pass

    user = User.objects.get(pk=pk)
    return render(request, "accounts/user_detail.html", {"user": user})


def users(req):
    data = []

    if req.method == "POST":
        print("POST request received for users")
        # Handle POST request if needed
        pass

    if req.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        data = serializer.data
        print("GET request received for users")
        # Handle GET request if needed
        print("Data serialized:", data)
        print("Users retrieved:", users)
        pass

    return render(req, "accounts/users.html", {"users": User.objects.all(), "data": data})


@api_view(["POST"])
def get_users(req):
    if req.method == "GET":
        users = User.objects.order_by("-date_joined")
        serializer = UserSerializer(users, many=True)
        data = serializer.data
        return Response(data, status=200)
    else:
        return HttpResponse("Method not allowed", status=405)


class UserAPIView(APIView):
    def get(self, request: HttpRequest):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ["get", "post", "delete", "put"]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = self.request.data["password"]
        serializer.validated_data["password"] = make_password(password)
        return super().perform_create(serializer)

    # def get_serializer_class(self):
    #     if self.request.method == "POST":
    #         return UserCreateSerializer

    #     return UserSerializer

    # def get_queryset(self):
    #     return User.objects.all()
