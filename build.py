from pybuilder.core import use_plugin, init
use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")      # Análisis estático de estilo
use_plugin("python.coverage")    # Auditoría de ejecución de código
use_plugin("python.distutils")   # Empaquetado

name = "BioGuard_Inventory"
default_task = "publish"

@init
def set_properties(project):
    # Umbral de rechazo: El build fallará si la cobertura es < 100%
    project.set_property("coverage_break_build", True)
    project.set_property("coverage_threshold_warn", 100)

    # Política de Estilo: El build fallará ante errores de formato PEP8
    project.set_property("flake8_break_build", True)
    project.set_property("flake8_verbose_output", True)
