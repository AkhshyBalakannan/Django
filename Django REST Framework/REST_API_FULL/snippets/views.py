from snippets.models import Snippet
from django.contrib.auth.models import User
from .serializers import UserSerializer, SnippetSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse


# THIS FUNCTION IS TO HIT THE API ENDPOINT AS ONE WHOLE
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

# ------------------------------------------------------------------------------------------------
# note THE ABOVE API_ROOT FUNC IS COMMENTED BUT STILL WORKS BECAUSE OF DEFAULT ROUTER USED IN URL
# ---------------------------------------------------------------------------------------------------


#from rest_framework import viewsets
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import permissions
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
