from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .serializers import (
	NegocioSerializer,
	SexoSerializer,
	PersonaSerializer,
	ClienteSerializer,
	TurnoSerializer,
	DuenioSerializer,
	NegocioDuenioSerializer,
	RubroSerializer,
	NegocioRubroSerializer,
	UsuarioSerializer,
	PerfilSerializer,
	PerfilUsuarioSerializer,
)

from .models import (
	Negocio,
	Sexo,
	Persona,
	Cliente,
	Turno,
	Duenio,
	NegocioDuenio,
	Rubro,
	NegocioRubro,
	Usuario,
	Perfil,
	PerfilUsuario,
)

#ViewSets para la API

class NegocioViewSet(viewsets.ModelViewSet):
	queryset = Negocio.objects.all()
	serializer_class = NegocioSerializer
	permission_classes = [DjangoModelPermissions]

class SexoViewSet(viewsets.ModelViewSet):
	queryset = Sexo.objects.all()
	serializer_class = SexoSerializer
	permission_classes = [DjangoModelPermissions]

class PersonaViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer
	permission_classes = [DjangoModelPermissions]

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	permission_classes = [DjangoModelPermissions]

class TurnoViewSet(viewsets.ModelViewSet):
	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer
	permission_classes = [DjangoModelPermissions]

class DuenioViewSet(viewsets.ModelViewSet):
	queryset = Duenio.objects.all()
	serializer_class = DuenioSerializer
	permission_classes = [DjangoModelPermissions]

class NegocioDuenioViewSet(viewsets.ModelViewSet):
	queryset = NegocioDuenio.objects.all()
	serializer_class = NegocioDuenioSerializer
	permission_classes = [DjangoModelPermissions]

class RubroViewSet(viewsets.ModelViewSet):
	queryset = Rubro.objects.all()
	serializer_class = RubroSerializer
	permission_classes = [DjangoModelPermissions]

class NegocioRubroViewSet(viewsets.ModelViewSet):
	queryset = NegocioRubro.objects.all()
	serializer_class = NegocioRubroSerializer
	permission_classes = [DjangoModelPermissions]

class UsuarioViewSet(viewsets.ModelViewSet):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer
	permission_classes = [DjangoModelPermissions]

class PerfilViewSet(viewsets.ModelViewSet):
	queryset = Perfil.objects.all()
	serializer_class = PerfilSerializer
	permission_classes = [DjangoModelPermissions]

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
	queryset = PerfilUsuario.objects.all()
	serializer_class = PerfilUsuarioSerializer
	permission_classes = [DjangoModelPermissions]


