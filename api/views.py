from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Passport, Qualification, Document
from .serializers import (
    PassportSerializer,
    QualificationSerializer,
    DocumentSerializer,
    )


class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all().select_related("qualification")
    serializer_class = PassportSerializer


class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().select_related("qualification")
    serializer_class = DocumentSerializer


@api_view(['POST'])
def accepte_regulations(request, qual_id):
    qualification = get_object_or_404(Qualification, id=qual_id)
    rule_one = request.POST.get('rule_one', qualification.rule_one)
    rule_two = request.POST.get('rule_two', qualification.rule_two)
    rule_three = request.POST.get('rule_three', qualification.rule_three)
    if qualification.status == '1':
        qualification.rule_one = rule_one
        qualification.rule_two = rule_two
        qualification.rule_three = rule_three
        if rule_one and rule_two and rule_three:
            qualification.status = '2'
            qualification.save()
            return Response('Regulations accepted',
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Not all regulation accepted',
                            status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def qualification_finish(request, qual_id):
    qualification = get_object_or_404(Qualification, id=qual_id)
    print(qualification.status)
    if qualification.status != '2':
        return Response(status=status.HTTP_403_FORBIDDEN)
    decision = request.POST.get('decision', 'DE')
    qualification.status = decision
    qualification.save()
    return Response('Decision accepted', status=status.HTTP_202_ACCEPTED)
