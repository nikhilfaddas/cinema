from rest_framework.routers import SimpleRouter
from .views import MoviesViewSet, ActorViewSet

simpleRouter = SimpleRouter()

simpleRouter.register('movie',MoviesViewSet)
simpleRouter.register('actor',ActorViewSet)

urlpatterns = simpleRouter.urls