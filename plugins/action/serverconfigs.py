# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
__metaclass__ = type

import sys

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        # command = module_return['command']
        if self._task.environment and any(self._task.environment):
            self._display.warning('This module does not support the environment keyword')

        result = super(ActionModule, self).run(tmp, task_vars)
        # del tmp  # tmp no longer has any effect
        params = self._task.args
        params['host'] = str(task_vars['inventory_hostname'])
        params['port'] = str(task_vars['nsr_port'])
        params['username'] = str(task_vars['nsr_user'])
        params['password'] = task_vars.get('nsr_pass', False)
        module_name = 'dellemc.networker.serverconfigs'

        if self._play_context.check_mode:
            # in --check mode, always skip this module execution
            result['skipped'] = True
            return result

        module_return = self._execute_module(module_name=module_name,
                                             module_args=params,
                                             task_vars=task_vars, tmp=tmp)
        if not module_return.get('failed'):
            result['msg'] = module_return['msg']
            result['changed'] = module_return['changed']
            result['failed'] = module_return['failed']
        else:
            result['msg'] = module_return
            result['failed'] = module_return['failed']

        return result
