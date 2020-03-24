# -*- coding: utf-8 -*-
from rest_framework import serializers
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

class NegocioSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Negocio
		fields = ['idNegocio', 'nombre', 'direccion', 'cupoClientes', 'intervalosMinutos', 'horaRestringidaInicio', 'horaRestringidaFin', 'justificativoHoraRestringida', 'latitud', 'longitud']

class SexoSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Sexo
		fields = ['idSexo', 'sexo']

class PersonaSerializer(serializers.HyperlinkedModelSerializer):

	sexo = SexoSerializer(read_only=True)

	class Meta:
		model = Persona
		fields = ['idPersona', 'nombre', 'dni', 'sexo', 'direccion', 'telefono', 'latitud', 'longitud']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):

	idPersona = PersonaSerializer(read_only=True)

	class Meta:
		model = Cliente
		fields = ['idCliente', 'idPersona']

class TurnoSerializer(serializers.HyperlinkedModelSerializer):

	idNegocio = NegocioSerializer(read_only=True)
	idCliente = ClienteSerializer(read_only=True)

	class Meta:
		model = Turno
		fields = ['idTurnos', 'idNegocio', 'idCliente', 'horarioInicio', 'horarioFin']

class DuenioSerializer(serializers.HyperlinkedModelSerializer):

	idPersona = PersonaSerializer(read_only=True)

	class Meta:
		model = Duenio
		fields = ['idDuenios', 'idPersona']

class NegocioDuenioSerializer(serializers.HyperlinkedModelSerializer):

	idNegocio = NegocioSerializer(read_only=True)
	idDuenio = DuenioSerializer(read_only=True)

	class Meta:
		model = NegocioDuenio
		fields = ['idNegocioDuenio', 'idNegocio', 'idDuenio']

class RubroSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Rubro
		fields = ['idRubro', 'descripcion']

class NegocioRubroSerializer(serializers.HyperlinkedModelSerializer):

	idRubro = RubroSerializer(read_only=True)
	idNegocio = NegocioSerializer(read_only=True)

	class Meta:
		model = NegocioRubro
		fields = ['idRubroNegocio', 'idRubro', 'idNegocio']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Usuario
		fields = ['idUsuario', 'usuario', 'userPassword']

class PerfilSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Perfil
		fields = ['isPerfil', 'descripcion']

class PerfilUsuarioSerializer(serializers.HyperlinkedModelSerializer):

	idPerfil = PerfilSerializer(read_only=True)
	idUsuario = UsuarioSerializer(read_only=True)

	class Meta:
		model = PerfilUsuario
		fields = ['idPerfilUsuario', 'idPerfil', 'idUsuario']

