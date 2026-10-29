"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os
import sys
import json

base_path = tmp_global_obj["basepath"]
module_root = os.path.join(base_path, "modules", "EventViewer")
libs_path = os.path.join(module_root, "libs")

# Rutas necesarias para encontrar eventViewerObject y los módulos de pywin32
paths_to_add = [
    module_root,
    libs_path,
    os.path.join(libs_path, "win32"),
    os.path.join(libs_path, "win32", "lib"),
]

for p in paths_to_add:
    if os.path.isdir(p) and p not in sys.path:
        sys.path.append(p)

# Registro de DLLs compiladas de pywin32
dll_dir = os.path.join(libs_path, "pywin32_system32")
if os.path.isdir(dll_dir) and hasattr(os, "add_dll_directory"):
    try:
        os.add_dll_directory(dll_dir)
    except Exception:
        pass

from eventViewerObject import get_event_logs

module = GetParams("module")

if module == "get_event_logs":
    output_var = GetParams("output_var")

    try:
        result_json = get_event_logs(
            log_name=GetParams("log_name"),
            source_filter=GetParams("source_filter"),
            event_id=GetParams("event_id"),
            event_type=GetParams("event_type"),
            message_filter=GetParams("message_filter"),
            start_time=GetParams("start_time"),
            end_time=GetParams("end_time"),
            max_records=GetParams("max_records"),
        )

        result_data = json.loads(result_json)

        if output_var:
            SetVar(output_var, result_data)
        else:
            print(result_json)

    except Exception as e:
        PrintException()
        raise e
