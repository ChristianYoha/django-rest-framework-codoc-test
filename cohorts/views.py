from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cohorts.factories import CohortFactory
from cohorts.models import Cohort
from cohorts.serializers import CohortSerializer

# import custom permission "IsOnlySuperUserAndOwnerCanDelete" only the owner and superusers can delete a cohort
from commons.permissions import ReadOnly, IsOnlySuperUserAndOwnerCanDelete


class CohortViewSet(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer
    permission_classes = [IsOnlySuperUserAndOwnerCanDelete | ReadOnly]
