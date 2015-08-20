"""
ProbLog command-line interface.

Copyright 2015 KU Leuven, DTAI Research Group

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


problog_tasks = {}
problog_tasks['prob'] = 'problog.tasks.probability'
problog_tasks['mpe'] = 'problog.tasks.mpe'
problog_tasks['sample'] = 'problog.tasks.sample'
problog_tasks['ground'] = 'problog.tasks.ground'
problog_tasks['lfi'] = '../../learning/lfi.py'

problog_default_task = 'prob'

from problog.util import load_module


def run_task(argv):
    """Execute a task in ProbLog.
    If the first argument is a known task name, that task is executed.
    Otherwise the default task is executed.

    :param argv: list of arguments for the task
    :return: result of the task (typically None)
    """
    if argv[0] in problog_tasks:
        task = argv[0]
        args = argv[1:]
    else:
        task = problog_default_task
        args = argv
    return load_task(task).main(args)


def load_task(name):
    """Load the module for executing the given task.

    :param name: task name
    :type name: str
    :return: loaded module
    :rtype: module
    """
    return load_module(problog_tasks[name])
