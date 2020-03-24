from django.db import models

class Negocio(models.Model):
	idNegocio = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50, help_text='Ingresar nombre del negocio')
	direccion = models.CharField(max_length=200, help_text='Ingresar la direccion del negocio')
	cupoClientes = models.PositiveIntegerField(help_text='Ingresar el máximo de clientes que pueden ingresar')
	intervalosMinutos = models.PositiveIntegerField(help_text='Ingresar el intervalo entre tandas de clientes')
	horaRestringidaInicio = models.TimeField()
	horaRestringidaFin = models.TimeField()
	justificativoHoraRestringida = models.CharField(max_length=200, help_text='Ingresar el justificativo')
	latitud = models.CharField(max_length=50, help_text='Ingresar la latitud del negocio')
	longitud = models.CharField(max_length=50, help_text='Ingresar la longitud del negocio')
	

	class Meta:
		verbose_name='Negocio'
		verbose_name_plural='Negocios'

	def __str__(self):
		return '%s' % (self.nombre)

class Sexo(models.Model):
	idSexo = models.AutoField(primary_key=True)
	sexo = models.CharField(max_length=50, help_text='Ingresar el sexo')

	class Meta:
		verbose_name='Sexo'
		verbose_name_plural='Sexos'

	def __str__(self):
		return '%s' % (self.sexo)

class Persona(models.Model):
	idPersona = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50, help_text='Ingresar su nombre')
	dni = models.PositiveIntegerField(help_text='Ingresar su DNI')
	sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, help_text='Elija el sexo')
	direccion = models.CharField(max_length=200, help_text='Ingresar la direccion')
	telefono = models.CharField(max_length=20, help_text='Ingrese el numero de telefono')
	latitud = models.CharField(max_length=50, help_text='Ingresar la latitud')
	longitud = models.CharField(max_length=50, help_text='Ingresar la longitud')

	class Meta:
		verbose_name='Persona'
		verbose_name_plural='Personas'

	def __str__(self):
		return '%s - %s' % (self.nombre, self.dni)

class Cliente(models.Model):
	idCliente = models.AutoField(primary_key=True)
	idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE, help_text='Elija la persona')

	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'

	def __str__(self):
		return '%s' % (self.idPersona)

class Turno(models.Model):
	idTurnos = models.AutoField(primary_key=True)
	idNegocio = models.ForeignKey(Negocio, on_delete=models.CASCADE, help_text='Elija el negocio')
	idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, help_text='Elija el cliente')
	horarioInicio = models.TimeField()
	horarioFin = models.TimeField()

	class Meta:
		verbose_name='Turno'
		verbose_name_plural='Turnos'

	def __str__(self):
		return '%s - %s' % (self.idNegocio, self.idCliente)

class Duenio(models.Model):
	idDuenios = models.AutoField(primary_key=True)
	idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE, help_text='Elija la persona')

	class Meta:
		verbose_name='Duenio'
		verbose_name_plural='Duenios'

	def __str__(self):
		return '%s' % (self.idPersona)

class NegocioDuenio(models.Model):
	idNegocioDuenio = models.AutoField(primary_key=True)
	idNegocio = models.ForeignKey(Negocio, on_delete=models.CASCADE, help_text='Elija el negocio')
	idDuenio = models.ForeignKey(Duenio, on_delete=models.CASCADE, help_text='Elija el duenio')

	class Meta:
		verbose_name='Negocio dueño'
		verbose_name_plural='Negocios dueños'

	def __str__(self):
		return '%s - %s' % (self.idDuenio, self.idNegocio)

class Rubro(models.Model):
	idRubro = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=100, help_text='Ingresar la descripcion del rubro')

	class Meta:
		verbose_name='Rubro'
		verbose_name_plural='Rubros'

	def __str__(self):
		return '%s' % (self.descripcion)

class NegocioRubro(models.Model):
	idRubroNegocio = models.AutoField(primary_key=True)
	idRubro = models.ForeignKey(Rubro, on_delete=models.CASCADE, help_text='Elija el rubro')
	idNegocio = models.ForeignKey(Negocio, on_delete=models.CASCADE, help_text='Elija el negocio')

	class Meta:
		verbose_name='Rubro de negocio'
		verbose_name_plural='Rubros de negocios'

	def __str__(self):
		return '%s - %s' % (self.idNegocio, self.idRubro)

class Usuario(models.Model):
	idUsuario = models.AutoField(primary_key=True)
	usuario = models.CharField(max_length=50, help_text='Ingresar el nombre del usuario')
	userPassword = models.CharField(max_length=50, help_text='Ingresar la contraseña del usuario')

	class Meta:
		verbose_name='Usuario'
		verbose_name_plural='Usuarios'

	def __str__(self):
		return '%s' % (self.usuario)

class Perfil(models.Model):
	isPerfil = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=50, help_text='Ingresar la descripcion del perfil')

	class Meta:
		verbose_name='Perfil'
		verbose_name_plural='Perfiles'

	def __str__(self):
		return '%s' % (self.descripcion)

class PerfilUsuario(models.Model):
	idPerfilUsuario = models.AutoField(primary_key=True)
	idPerfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, help_text='Elija el perfil')
	idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, help_text='Elija el usuario')

	class Meta:
		verbose_name='Perfil de usuario'
		verbose_name_plural='Perfiles de usuarios'

	def __str__(self):
		return '%s - %s' % (self.idPerfil, self.idUsuario)

