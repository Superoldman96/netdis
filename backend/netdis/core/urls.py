from django.urls import path
from .views import test_view, binary_ingest, probe, funcs, blocks, disasms, task, func_graph, proj_to_file

urlpatterns = [
    path('test/', test_view, name='test'),
    path('binary_ingest/', binary_ingest, name='binary_ingest'),
    path('probe/', probe, name='probe'),
    
    path('funcs/', funcs, name='funcs'),
    path('blocks/', blocks, name='funcs'),
    path('disasms/', disasms, name='disasms'),
    
    path('task/<int:id>', task, name='task'),
    
    path('func_graph/', func_graph, name='func_graph'),
    
    path('proj/', test_view, name='proj'),
    path('func/', test_view, name='func'),
    path('block/', test_view, name='block'),
    path('disasm/', test_view, name='disasm'),
    path('proj_to_file', proj_to_file, name='proj_to_file')
]

# funcs/ - return functions by project id
# blocks/ - return blocks by function id
# disasms/ - return disasm by block id

# proj/ - return project info by id
# func/ - return function info by id
# block/ - return block info by id
# disasm/ - return disasm info by id

# return file id from project