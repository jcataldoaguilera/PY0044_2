from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    list_tareas = Tarea.objects.filter(eliminada= False)
    array_tareas = []

    for tarea in list_tareas:
        subtareas = tarea.subtarea_set.filter(eliminada= False)
        dict_tareas = {
            'tarea':tarea,
            'subtareas':subtareas
        }
        array_tareas.append(dict_tareas)

    return array_tareas

def crear_nueva_tarea(desc='', delt=False):
    tarea = Tarea(descripcion=desc, eliminada=delt)
    tarea.save()

def crear_sub_tarea(tid, desc='', delt=False):
    tarea_fk = Tarea.objects.get(pk=tid)
    subtarea = Tarea(descripcion=desc, eliminada=delt, tarea=tarea_fk)
    subtarea.save()

def elimina_tarea(tid):
    tarea = Tarea.objects.get(pk=tid)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea():
    pass

def imprimir_en_pantalla():
    pass