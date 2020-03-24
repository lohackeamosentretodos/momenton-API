from django.urls import include, path
from rest_framework import routers
from .views import (
	NegocioViewSet,
	SexoViewSet,
	PersonaViewSet,
	ClienteViewSet,
	TurnoViewSet,
	DuenioViewSet,
	NegocioDuenioViewSet,
	RubroViewSet,
	NegocioRubroViewSet,
	UsuarioViewSet,
	PerfilViewSet,
	PerfilUsuarioViewSet,
)

app_name='mi_turno_seguro'

router = routers.DefaultRouter()
router.register('negocio', NegocioViewSet)
router.register('sexo', SexoViewSet)
router.register('persona', PersonaViewSet)
router.register('cliente', ClienteViewSet)
router.register('turno', TurnoViewSet)
router.register('duenio', DuenioViewSet)
router.register('negocio_duenio', NegocioDuenioViewSet)
router.register('rubro', RubroViewSet)
router.register('negocio_rubro', NegocioRubroViewSet)
router.register('usuario', UsuarioViewSet)
router.register('perfil', PerfilViewSet)
router.register('perfil_usuario', PerfilUsuarioViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
]