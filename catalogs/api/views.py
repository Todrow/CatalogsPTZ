from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Detail, Folder, IMG, Hot_point, Count_details
from .serializers import DetailSerializer, FolderSerializer, IMGSerializer, Hot_pointSerializer, Count_detailsSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()          # Сохраняем нового пользователя
            login(request, user)        # Выполняем вход
            return redirect('home')     # Перенаправляем на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Проверяем учетные данные
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)     # Выполняем вход
                return redirect('home')  # Перенаправляем на главную страницу
    return render(request, 'login.html', {'form': form})

# class UserRegistration(APIView):
#     def post(self, request):
#         serializer = UserSerializer()
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"status": "User created", "id": user.id}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailViewSet(APIView):
    """Представление для деталей"""
    # queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['folder__tag', 'folder__VIN', 'folder__parent']
    search_fields = ['name', 'designation']
    ordering_fields = ['count_details__count']
    def post(self, request):
        serializer_for_detail = self.serializer_class(
            data=request.data, many=False)
        serializer_for_detail.is_valid(raise_exception=True)
        serializer_for_detail.save()
        return Response(data=serializer_for_detail.data, status=status.HTTP_201_CREATED)

class FolderCreateSet(APIView):
    serializer_class = FolderSerializer

    def post(self, request):
        serializer_for_folder = self.serializer_class(data=request.data, many=False)
        serializer_for_folder.is_valid(raise_exception=True)
        serializer_for_folder.save()
        return Response(data=serializer_for_folder.data, status=status.HTTP_201_CREATED)

class FolderView(APIView):
    serializer_class = FolderSerializer

    def get(self, request):
        qureyset = Folder.objects.all()
        serializer_for_folder = self.serializer_class(instance=qureyset, many=True)
        return Response(data=serializer_for_folder.data, status=status.HTTP_200_OK)
        
    