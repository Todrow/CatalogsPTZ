from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Detail, Folder, IMG, Hot_point, Count_details
from .serializers import DetailSerializer, FolderCreateSerializer, FolderReadSerializer, IMGSerializer, Hot_pointSerializer, Count_detailsSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework import generics
# from django.contrib.auth import login, authenticate
# from .forms import SignUpForm, LoginForm


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()          # Сохраняем нового пользователя
#             login(request, user)        # Выполняем вход
#             return redirect('home')     # Перенаправляем на главную страницу
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


# def login_view(request):
#     form = LoginForm(data=request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             # Проверяем учетные данные
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)     # Выполняем вход
#                 return redirect('home')  # Перенаправляем на главную страницу
#     return render(request, 'login.html', {'form': form})

# class UserRegistration(APIView):
#     def post(self, request):
#         serializer = UserSerializer()
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"status": "User created", "id": user.id}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailViewSet(APIView):
    """Представление для деталей"""
    serializer_class = DetailSerializer
    # filter_backends = [DjangoFilterBackend,
    #                    filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['folder__tag', 'folder__VIN', 'folder__parent']
    # search_fields = ['name', 'designation']
    # ordering_fields = ['count_details__count']

    def post(self, request):
        serializer_for_detail = self.serializer_class(
            data=request.data, many=False)
        serializer_for_detail.is_valid(raise_exception=True)
        serializer_for_detail.save()
        return Response(data=serializer_for_detail.data, status=status.HTTP_201_CREATED)


class FolderCreateSet(APIView):
    serializer_class = FolderCreateSerializer

    def post(self, request):
        serializer_for_folder = self.serializer_class(
            data=request.data, many=False)
        serializer_for_folder.is_valid(raise_exception=True)
        serializer_for_folder.save()
        return Response(data=serializer_for_folder.data, status=status.HTTP_201_CREATED)


class FolderList(APIView):
    serializer_class = FolderReadSerializer

    def get(self, request):
        qureyset = Folder.objects.all()
        serializer_for_folder = self.serializer_class(
            instance=qureyset, many=True)
        return Response(data=serializer_for_folder.data, status=status.HTTP_200_OK)


class FolderGetById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderReadSerializer


class FolderGetByTag(APIView):
    serializer_class = FolderReadSerializer

    def get(self, request, folder_tag):
        try:
            qureyset = [Folder.objects.get(tag=folder_tag)]
            serializer_for_folder = self.serializer_class(
                instance=qureyset, many=True)
            return Response(data=serializer_for_folder.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

class FolderGetByVIN(APIView):
    serializer_class = FolderReadSerializer

    def get(self, request, vin):
        try:
            qureyset = [Folder.objects.get(VIN=vin)]
            serializer_for_folder = self.serializer_class(
                instance=qureyset, many=True)
            return Response(data=serializer_for_folder.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class IMGCreate(APIView):
    serializer_class = IMGSerializer

    def post(self, request):
        serializer_for_img = self.serializer_class(
            data=request.data, many=False)
        serializer_for_img.is_valid(raise_exception=True)
        serializer_for_img.save()
        return Response(data=serializer_for_img.data, status=status.HTTP_201_CREATED)


class IMGGetById(APIView):
    serializer_class = IMGSerializer

    def get(self, request, img_id):
        queryset = IMG.objects.get(id=img_id)
        serilaizer_for_img = self.serializer_class(
            instance=queryset, many=False)
        return Response(data=serilaizer_for_img.data, status=status.HTTP_200_OK)


class HotPointCreate(APIView):
    serializer_class = Hot_pointSerializer

    def post(self, request):
        serializer_for_hotpoint = self.serializer_class(
            data=request.data, many=False)
        serializer_for_hotpoint.is_valid(raise_exception=True)
        serializer_for_hotpoint.save()
        return Response(data=serializer_for_hotpoint.data, status=status.HTTP_201_CREATED)


class HotPointOnIMGList(APIView):
    serializer_class = Hot_pointSerializer

    def get(self, request, img_id):
        queryset = Hot_point.objects.filter(IMG=img_id)
        serializer_for_hotpoint = self.serializer_class(
            instance=queryset, many=True)
        return Response(data=serializer_for_hotpoint.data, status=status.HTTP_200_OK)


class TestDataCreate(APIView):

    def get(self, request, type_of_data):
        if type_of_data == 'shop':
            # Создаём главную папку
            home = Folder.objects.create()
            home.tag = 'home'
            home.save()

            # Создаём папку с сельскохозяйственной техникой
            agro = Folder.objects.create()
            agro.tag = 'agro'
            agro.parent.set([home])
            agro.description = {"name": "Сельскохозяйственная техника"}
            agro.save()
            # Генерируем сельскохозяйственную технику
            for i in range(5):
                trctr = Folder.objects.create()
                trctr.tag = 'card'
                trctr.parent.set([agro])
                trctr.description = {"name": f"K{i}"}
                trctr.save()

            # Создаём папку с Строительной техникой
            buil = Folder.objects.create()
            buil.tag = 'buil'
            buil.parent.set([home])
            buil.description = {"name": "Строительная техника"}
            buil.save()
            # Генерируем Строительную технику
            for i in range(5):
                trctr = Folder.objects.create()
                trctr.tag = 'card'
                trctr.parent.set([buil])
                trctr.description = {"name": f"K{i}"}
                trctr.save()

            # Создаём папку с Специальной техникой
            spec = Folder.objects.create()
            spec.tag = 'spec'
            spec.parent.set([home])
            spec.description = {"name": "Специальная техника"}
            spec.save()
            # Генерируем Специальную технику
            for i in range(5):
                trctr = Folder.objects.create()
                trctr.tag = 'card'
                trctr.parent.set([spec])
                trctr.description = {"name": f"K{i}"}
                trctr.save()
        return Response(status=status.HTTP_200_OK)
