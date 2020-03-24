from django.contrib import admin
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

@admin.register(Negocio)
class NegocioAdmin(admin.ModelAdmin):
	list_display = ['idNegocio', 'nombre', 'direccion', 'cupoClientes', 'intervalosMinutos', 'horaRestringidaInicio', 'horaRestringidaFin', 'justificativoHoraRestringida', 'latitud', 'longitud']

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
	list_display = ['idSexo', 'sexo']

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	list_display = ['idPersona', 'nombre', 'dni', 'sexo', 'direccion', 'telefono', 'latitud', 'longitud']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ['idCliente', 'idPersona']

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
	list_display = ['idTurnos', 'idNegocio', 'idCliente', 'horarioInicio', 'horarioFin']

@admin.register(Duenio)
class DuenioAdmin(admin.ModelAdmin):
	list_display = ['idDuenios', 'idPersona']

@admin.register(NegocioDuenio)
class NegocioDuenioAdmin(admin.ModelAdmin):
	list_display = ['idNegocioDuenio', 'idNegocio', 'idDuenio']

@admin.register(Rubro)
class RubroAdmin(admin.ModelAdmin):
	list_display = ['idRubro', 'descripcion']

@admin.register(NegocioRubro)
class NegocioRubroAdmin(admin.ModelAdmin):
	list_display = ['idRubroNegocio', 'idRubro', 'idNegocio']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['idUsuario', 'usuario', 'userPassword']

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
	list_display = ['isPerfil', 'descripcion']

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
	list_display = ['idPerfilUsuario', 'idPerfil', 'idUsuario']

