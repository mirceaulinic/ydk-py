


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'ProcessesMemory.Nodes.Node.JobIds.JobId' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes.Node.JobIds.JobId',
            False, 
            [
            _MetaInfoClassMember('job-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Job Id
                ''',
                'job_id',
                'Cisco-IOS-XR-procmem-oper', True),
            _MetaInfoClassMember('data-seg-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Data Segment Size
                ''',
                'data_seg_size',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('jid', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Job ID
                ''',
                'jid',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('malloc-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Malloced Memory Size
                ''',
                'malloc_size',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process name
                ''',
                'name',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('stack-seg-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Stack Segment Size
                ''',
                'stack_seg_size',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('text-seg-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Text Segment Size
                ''',
                'text_seg_size',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'job-id',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.procmem.Cisco_IOS_XR_procmem_oper'
        ),
    },
    'ProcessesMemory.Nodes.Node.JobIds' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes.Node.JobIds',
            False, 
            [
            _MetaInfoClassMember('job-id', REFERENCE_LIST, 'JobId' , 'ydk.models.procmem.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes.Node.JobIds.JobId', 
                [], [], 
                '''                Job Id
                ''',
                'job_id',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'job-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.procmem.Cisco_IOS_XR_procmem_oper'
        ),
    },
    'ProcessesMemory.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-procmem-oper', True),
            _MetaInfoClassMember('job-ids', REFERENCE_CLASS, 'JobIds' , 'ydk.models.procmem.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes.Node.JobIds', 
                [], [], 
                '''                List of jobs
                ''',
                'job_ids',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.procmem.Cisco_IOS_XR_procmem_oper'
        ),
    },
    'ProcessesMemory.Nodes' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.procmem.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes.Node', 
                [], [], 
                '''                Node ID
                ''',
                'node',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.procmem.Cisco_IOS_XR_procmem_oper'
        ),
    },
    'ProcessesMemory' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.procmem.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes', 
                [], [], 
                '''                List of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'processes-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.procmem.Cisco_IOS_XR_procmem_oper'
        ),
    },
}
_meta_table['ProcessesMemory.Nodes.Node.JobIds.JobId']['meta_info'].parent =_meta_table['ProcessesMemory.Nodes.Node.JobIds']['meta_info']
_meta_table['ProcessesMemory.Nodes.Node.JobIds']['meta_info'].parent =_meta_table['ProcessesMemory.Nodes.Node']['meta_info']
_meta_table['ProcessesMemory.Nodes.Node']['meta_info'].parent =_meta_table['ProcessesMemory.Nodes']['meta_info']
_meta_table['ProcessesMemory.Nodes']['meta_info'].parent =_meta_table['ProcessesMemory']['meta_info']
