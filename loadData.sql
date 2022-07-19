\c TrabajoTitulo;

/* Roles */
INSERT INTO public."App_roles"(nombre)
	VALUES
	('Administrador'),
    ('Profesor'),
    ('Estudiante');

/* Usuarios */
INSERT INTO public."App_usuarios"(paterno,materno,nombres,correo,password,rut,rol_id,date_joined,email,first_name,is_active,is_staff,is_superuser,last_login,last_name)
	VALUES
	('Perez','Tapia','Hector Campos','hector.peta@gmail.com','pbkdf2_sha256$260000$qfaC787TvEGhP31n9mm6bR$H14G3FPfq126b1P4ZLGt65TrhqJqN5OSFZRrec4wHrs=','16267818-3', 3, '2020/10/10', 'asd', 'asd', False, False, False, '2022/06/06', 'asd'),
	('Gutierrez','Ruiz','Eduardo Ruiz','edsuru@live.cl','pbkdf2_sha256$260000$qfaC787TvEGhP31n9mm6bR$H14G3FPfq126b1P4ZLGt65TrhqJqN5OSFZRrec4wHrs=','12339396-1',3, '2020/10/10', 'asd', 'asd', False, False, False, '2022/06/06', 'asd'),
	('Ferrer','Gutierrez','Felipe Garrido','ferrerartu@smail.com','pbkdf2_sha256$260000$qfaC787TvEGhP31n9mm6bR$H14G3FPfq126b1P4ZLGt65TrhqJqN5OSFZRrec4wHrs=','12659418-6',3, '2020/10/10', 'asd', 'asd', False, False, False, '2022/06/04', 'asd'),
	('Pascual','Jimenez','Ximena Morales','ximenapascual@hotmail.cl','pbkdf2_sha256$260000$qfaC787TvEGhP31n9mm6bR$H14G3FPfq126b1P4ZLGt65TrhqJqN5OSFZRrec4wHrs=','18864964-5',3, '2020/10/10', 'asd', 'asd', False, False, False, '2022/06/05', 'asd'),
	('Mora','Saez','Maria Moreno','mamoreno@gmail.com','pbkdf2_sha256$260000$qfaC787TvEGhP31n9mm6bR$H14G3FPfq126b1P4ZLGt65TrhqJqN5OSFZRrec4wHrs=','24936172-0',3, '2020/10/10', 'asd', 'asd', False, False, False, '2022/06/06', 'asd');

/* Tecnologias */
INSERT INTO public."App_tecnologias" (nombre, descripcion)
	VALUES
	('Docker','Docker es un proyecto de código abierto que automatiza el despliegue de aplicaciones dentro de contenedores de software, proporcionando una capa adicional de abstracción y automatización de virtualización de aplicaciones en múltiples sistemas operativos.​'),
	('Git', 'Git es un software de control de versiones diseñado por Linus Torvalds, pensando en la eficiencia, la confiabilidad y compatibilidad del mantenimiento de versiones de aplicaciones cuando estas tienen un gran número de archivos de código fuente.'),
	('Minikube','Minikube es la solución ideal para pequeños proyectos basados ​en contenedores. Te permite, por ejemplo, configurar un clúster de Kubernetes en privado sin tener que trabajar directamente con todo un servidor o una nube.');
	/*('Jenkins','Jenkins es un servidor de automatización open source escrito en Java. Está basado en el proyecto Hudson y es, dependiendo de la visión, un fork del proyecto o simplemente un cambio de nombre.');*/

/* Ejercicios */
INSERT INTO public."App_ejercicios" (nombre, enunciado, respuesta1, respuesta2, tecnologia_id)
	VALUES
	('Descargar imagen','Escriba el comando que se utiliza para descargar una imagen que se encuentra en un repositorio, ya sea publico o privado.', 'docker pull', NULL, 1),
	('Inicia un nuevo repositorio', 'Escriba el comando que se utiliza para crear un nuevo repositorio.', 'git init', NULL, 2),
	('Iniciar un cluster','Escriba el comando para incializar un cluster.', 'minikube start', NULL, 3),
	('Mostrar imagenes','Escriba el comando que se utiliza para ver todas las imagenes disponibles localmente.', 'docker images', 'docker images -a', 1),
	('Anada un cambio al repositorio local', 'Escriba el comando que se utiliza para anadir un cambio en el repositorio local, el cual indica las actualizaciones que se le haran al repositorio remoto en la proxima confirmacion.', 'git add', NULL, 2),
	('Informacion de un cluster','Escriba el comando para obtener los detalles y el estado en que se encuentra el cluster.', 'kubectl cluster-info', NULL, 3),
	('Ejecutar un contenedor','Escriba el comando que se utiliza para ejecutar un contenedor.', 'docker run', NULL, 1),
	('Suba los cambios al repositorio remoto', 'Escriba el comando que se utiliza para enviar los cambios del repositorio local al repositorio remoto.', 'git commit', NULL, 2),
	('Ver los nodos de un cluster','Escriba el comando que permite observar los nodos que se encuentran dentro del cluster.', 'kubectl get nodes', NULL, 3);
	/*('Jenkins','Vivamus bibendum arcu mi, quis bibendum mauris facilisis ullamcorper. Phasellus vehicula neque tellus, non laoreet sapien laoreet quis. Proin scelerisque aliquet auctor. Nulla ac blandit erat, non porttitor enim. Vivamus venenatis, arcu sit amet lacinia volutpat, tortor diam suscipit mi, nec rhoncus eros leo in nulla. Vestibulum maximus, sem sed venenatis molestie.', 'chao', NULL, 4);*/

/* Clases */
INSERT INTO public."App_clases" (titulo, descripcion, tecnologia_id)
	VALUES
	('Conceptos basicos de Docker: Que es una imagen?','Una imagen es la representacion de una plantilla con instrucciones para crear un contenedor, donde se definen el conjunto de programas, librerias, sistema operativo, configuraciones, etc, que tendran que estar disponibles.', 1),
	('Conceptos basicos de Git: Que es el control de versiones?','Es la practica de rastrear y gestionar cambios en el codigo de software. Los sistemas de control de versiones son herramientas de software que ayudan a los equipos a gestionar los cambios en el codigo fuente a lo largo del tiempo.', 2),
	('Conceptos basicos de Minikube: Que es Kubernetes?','Es una plataforma de codigo abierto para automatizar la implementacion, el escalador y la administracion de aplicaciones de contenedores.', 3),
	('Conceptos basicos de Docker: Que es un contenedor?','Es una instancia ejecutable de una imagen. Esto se debe a que al ser plantillas no se pueden iniciar, reiniciar, etc., en cambio los contenedores si. Estos al iniciarse pueden modificar su estado, mientras que la imagen seguira siendo la misma.', 1),
	('Conceptos basicos de Git: Que es Git?','Es un sistema de control de versiones de codigo abierto y con una estructura distribuida, lo que le permite tener varios repositorios para albergar el historial de cambios que realizo cada desarrollador.', 2),
	('Conceptos basicos de Minikube: Que es un cluster?','Es el conjunto de nodos que Kubernetes administra.', 3),
	('Conceptos basicos de Docker: Que es Docker compose?','Es una utilidad que permite gestionar varios contenedores, formando un grupo de recursos. Lo que permite que compartan recursos, puertos, archivos, etc.', 1),
	('Conceptos basicos de Git: Que es un repositorio de Git?','Es un almacenamiento virtual de tu proyecto. Este te permite guardar versiones de tu codigo, a las cuales puedes acceder en cualquier momento.', 2),
	('Conceptos basicos de Minikube: Definicion de Minikube','Es una herramienta que facilita la tarea de inicializar Kubernetes de manera local.', 3);
	
/* Usuario_Ejercicio */
INSERT INTO public."App_usuario_ejercicio" (tiempo, estado, respuesta, ejercicio_id, usuario_id)
	VALUES
	(10000, 1, 'docker pull', 1, 1),
	(20000, 1, 'git init', 2, 1),
	(30000, 1, 'minikube', 3, 1),
	(10000, 1, 'docker images -a', 4, 1),
	(20000, 0, 'nose', 5, 1),
	(30000, 0, 'si', 6, 1),
	(10000, 0, 'a', 7, 1),
	(20000, 1, 'git commit', 8, 1),
	(30000, 1, 'si', 9, 1),
	(10000, 0, 'a', 1, 2),
	(50000, 1, 'b', 2, 2),
	(60000, 0, 'nose', 3, 2),
	(10000, 0, 'a', 4, 2),
	(50000, 1, 'b', 5, 2),
	(60000, 1, 'nose', 6, 2),
	(10000, 1, 'a', 7, 2),
	(50000, 1, 'b', 8, 2),
	(60000, 1, 'nose', 9, 2),
	(10200, 1, 'test', 1, 3),
	(40000, 1, 'a', 2, 3),
	(90000, 1, 'b', 3, 3),
	(10200, 1, 'test', 4, 3),
	(40000, 1, 'a', 5, 3),
	(90000, 1, 'b', 6, 3),
	(10200, 1, 'test', 7, 3),
	(40000, 1, 'a', 8, 3),
	(90000, 1, 'b', 9, 3),
	(110000, 1, 'si', 1, 4),
	(1000, 0, 'test', 2, 4),
	(60000, 0, 'a', 3, 4),
	(110000, 1, 'si', 4, 4),
	(1000, 1, 'test', 5, 4),
	(60000, 1, 'a', 6, 4),
	(110000, 1, 'si', 7, 4),
	(1000, 1, 'test', 8, 4),
	(60000, 1, 'a', 9, 4),
	(50500, 1, 'test', 1, 5),
	(70000, 1, 'a', 2, 5),
	(990000, 1, 'b', 3, 5),
	(50500, 1, 'test', 4, 5),
	(70000, 1, 'a', 5, 5),
	(990000, 1, 'b', 6, 5),
	(50500, 1, 'test', 7, 5),
	(70000, 1, 'a', 8, 5),
	(990000, 1, 'b', 9, 5);

/* Usuario_Clase */
INSERT INTO public."App_usuario_clase" (tiempo, estado, clase_id, usuario_id)
	VALUES
	(20000, 1, 1, 1),
	(20000, 1, 2, 1),
	(20000, 0, 3, 1),
	(20000, 1, 4, 1),
	(20000, 1, 5, 1),
	(20000, 0, 6, 1),
	(20000, 1, 7, 1),
	(20000, 0, 8, 1),
	(20000, 0, 9, 1),
	(20000, 1, 1, 2),
	(20000, 1, 2, 2),
	(20000, 1, 3, 2),
	(20000, 1, 4, 2),
	(20000, 1, 5, 2),
	(20000, 1, 6, 2),
	(20000, 1, 7, 2),
	(20000, 1, 8, 2),
	(20000, 1, 9, 2),
	(20000, 1, 1, 3),
	(20000, 1, 2, 3),
	(20000, 1, 3, 3),
	(20000, 1, 4, 3),
	(20000, 1, 5, 3),
	(20000, 1, 6, 3),
	(20000, 1, 7, 3),
	(20000, 1, 8, 3),
	(20000, 1, 9, 3),
	(20000, 1, 1, 4),
	(20000, 1, 2, 4),
	(20000, 1, 3, 4),
	(20000, 1, 4, 4),
	(20000, 1, 5, 4),
	(20000, 1, 6, 4),
	(20000, 1, 7, 4),
	(20000, 1, 8, 4),
	(20000, 1, 9, 4),
	(20000, 1, 1, 5),
	(20000, 1, 2, 5),
	(20000, 1, 3, 5),
	(20000, 1, 4, 5),
	(20000, 1, 5, 5),
	(20000, 1, 6, 5),
	(20000, 1, 7, 5),
	(20000, 1, 8, 5),
	(20000, 1, 9, 5);
	
END;

$$ LANGUAGE 'plpgsql';