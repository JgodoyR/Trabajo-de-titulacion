from rest_framework import serializers
import App.models as models

class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Roles
        fields = (
            'id',
            'nombre')

class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuarios
        fields = (
            'id',
            'rol',
            'nombres',
            'paterno',
            'materno',
            'correo',
            'password',
            'rut',
            'last_login'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create( self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class TecnologiasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tecnologias
        fields = (
            'id',
            'nombre',
            'descripcion')

class ClasesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Clases
        fields = (
            'id',
            'tecnologia',
            'titulo',
            'descripcion')

class EjerciciosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Ejercicios
        fields = (
            'id',
            'tecnologia',
            'nombre',
            'enunciado',
            'respuesta1',
            'respuesta2')

class Usuario_EjercicioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Usuario_Ejercicio
        fields = (
            'id',
            'usuario',
            'ejercicio',
            'tiempo',
            'estado',
            'respuesta')

class Usuario_ClaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Usuario_Clase
        fields = (
            'id',
            'usuario',
            'clase',
            'estado',
            'tiempo')

# Cruz

class UsuariosCruzSerializer(serializers.ModelSerializer):
    rol = RolesSerializer(read_only=True)

    class Meta:
        model = models.Usuarios
        fields = (
            'id',
            'rol',
            'nombres',
            'paterno',
            'materno',
            'correo',
            'password',
            'rut',
            'last_login'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create( self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EjercicioCruzSerializer(serializers.ModelSerializer):
    tecnologia = TecnologiasSerializer(read_only=True)
    
    class Meta:
        model = models.Ejercicios
        fields = (
            'id',
            'tecnologia',
            'nombre',
            'enunciado',
            'respuesta1',
            'respuesta2')

class ClasesCruzSerializer(serializers.ModelSerializer):
    tecnologia = TecnologiasSerializer(read_only=True)
    
    class Meta:
        model = models.Clases
        fields = (
            'id',
            'tecnologia',
            'titulo',
            'descripcion')

class Usuario_EjercicioCruzSerializer(serializers.ModelSerializer):
    usuario = UsuariosSerializer(read_only=True)
    ejercicio = EjerciciosSerializer(read_only=True)
    
    class Meta:
        model = models.Usuario_Ejercicio
        fields = (
            'id',
            'usuario',
            'ejercicio',
            'tiempo',
            'estado',
            'respuesta')

class Usuario_ClaseCruzSerializer(serializers.ModelSerializer):
    usuario = UsuariosSerializer(read_only=True)
    clase = ClasesSerializer(read_only=True)

    class Meta:
        model = models.Usuario_Clase
        fields = (
            'id',
            'usuario',
            'clase',
            'estado',
            'tiempo')

# Personalizados

class UsuariosPasswordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Usuarios
        fields = (
            'id',
            'password'
            )

    def create( self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UsuariosPasswordlessSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuarios
        fields = (
            'id',
            'rol',
            'nombres',
            'paterno',
            'materno',
            'correo',
            'rut'
        )