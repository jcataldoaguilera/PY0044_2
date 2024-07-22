from .models import Curso, Profesor, Direccion, Estudiante

def crear_curso (code, name, vers):
    curso = Curso(codigo = code, nombre = name, version = vers)
    curso.save()
    return curso

def crear_profesor(rut, f_name, l_name, createdby):
    profesor = Profesor(rut = rut, nombre = f_name, apellido = l_name, creado_por = createdby)
    profesor.save()
    return profesor

def crear_estudiante(rut, f_name, l_name, b_date, createdby):
    estudiante = Estudiante(rut = rut, nombre = f_name, apellido = l_name, fecha_nac = b_date, creado_por = createdby)
    estudiante.save()
    return estudiante

def crear_direccion(pCalle, pNumero, pDepto, pComuna, pCiudad, pRegion, rut_estudiante):
    estudiante = Estudiante.objects.get(rut = rut_estudiante)
    direccion = Direccion(calle = pCalle, numero = pNumero, depto = pDepto, comuna = pComuna, ciudad = pCiudad, region = pRegion, estudiante = estudiante)
    direccion.save()
    return direccion

def obtiene_estudiante(rut_estudiante):
    return Estudiante.objects.get(rut = rut_estudiante)

def obtiene_profesor(rut_profesor):
    return Profesor.objects.get(rut = rut_profesor)

def obtiene_curso(cod_curso):
    return Curso.objects.get(codigo = cod_curso)

def agrega_profesor_a_curso(cod_curso, rut_profesor):
    curso = Curso.objects.get(codigo = cod_curso)
    profesor = Profesor.objects.get(rut = rut_profesor)
    profesor.cursos.add(curso)
    return curso

def agrega_cursos_a_estudiante(rut_estudiante, cod_curso):
    estudiante = Estudiante.objects.get(rut = rut_estudiante)
    curso = Curso.objects.get(codigo = cod_curso)
    estudiante.cursos.add(curso)
    return curso

def imprime_estudiante_cursos(rut):
    estudiante = Estudiante.objects.get(rut = rut)
    cursos = estudiante.cursos.all()
    return cursos