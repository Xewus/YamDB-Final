from api import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import SignupView, TokenView, UserViewSet

app_name = 'api'
API_VERSION_1 = 'v1/'

router_v1 = DefaultRouter()
router_v1.register(
    'users',
    UserViewSet,
    basename='users')
router_v1.register(
    'categories',
    views.CategoryViewSet,
    basename='categories')
router_v1.register(
    'genres',
    views.GenreViewSet,
    basename='genres')
router_v1.register(
    'titles',
    views.TitleViewSet,
    basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='review')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='comment')


auth_urls = [
    path('signup/', SignupView.as_view()),
    path('token/', TokenView.as_view())
]

urlpatterns = [
    path(API_VERSION_1, include(router_v1.urls)),
    path(API_VERSION_1 + 'auth/', include(auth_urls)),
]