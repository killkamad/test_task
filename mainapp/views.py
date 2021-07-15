from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

from .models import UserProfile, Record, Template, Status
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer, RecordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class RecordView(ListCreateAPIView):
    queryset = Record.objects.all().order_by('id')
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]


class ExportView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request):
        user = UserProfile.objects.get(user=request.user)
        template = Template.objects.all().order_by('-id').filter(user_id=user)[:1]
        lst = []
        file_name_final = []
        file_name = ''
        opt_1 = ''
        opt_2 = ''
        opt_3 = ''
        opt_4 = ''
        opt_5 = ''
        for j in template:
            file_name = j.file_name.split('__')
            opt_1 = j.option_one
            opt_2 = j.option_two
            opt_3 = j.option_three
            opt_4 = j.option_four
            opt_5 = j.option_five
        print(file_name)
        records = Record.objects.all().order_by('id').filter(user_id=user).values(opt_1, opt_2, opt_3, opt_4, opt_5)
        if records:
            file = Record.objects.all().order_by('id').filter(user_id=user)
            if file:
                file = file.values(*file_name)[0]
                for k, v in file.items():
                    print(k, v)
                    if k == 'created_at':
                        file_name_final.append(v.strftime("%y-%m-%d"))
                    elif k == 'status_id':
                        stat = Status.objects.get(id=v)
                        file_name_final.append(str(stat))
                    elif k == 'user_id':
                        us = UserProfile.objects.get(id=v)
                        file_name_final.append(str(us))
                    else:
                        file_name_final.append(str(v))
                file_name_final = '_'.join(file_name_final)
                print(file_name_final)

            for i in records:
                tst = []
                for k, v in i.items():
                    if k == 'created_at':
                        tst.append(v.strftime("%y-%m-%d"))
                    elif k == 'phone':
                        tst.append(v[:-3] + '***')
                    elif k == 'status_id':
                        stat = Status.objects.get(id=v)
                        tst.append(str(stat))
                    else:
                        tst.append(str(v))
                lst.append(tst)
            with open(f'{file_name_final}.csv', 'w') as f:
                f.write(f'{opt_1},{opt_2},{opt_3},{opt_4},{opt_5}\n')
                for i in lst:
                    f.write(','.join(i))
                    f.write('\n')
            return Response('OK')
        else:
            return Response('No records for this user')


class ConfigureView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request):
        user = UserProfile.objects.get(user=request.user)
        data = request.data
        temp = Template.objects.create(file_name=request.data.get('file_name'),
                                       option_one=data.get('option_one'),
                                       option_two=data.get('option_two'),
                                       option_three=data.get('option_three'),
                                       option_four=data.get('option_four'),
                                       option_five=data.get('option_five'),
                                       user_id=user)
        temp.save()
        return Response(request.data)
