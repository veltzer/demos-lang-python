"""
This is a mixin solution to the modification time stamps mentioned before.
"""

import os.path
import time

import luigi


def mtime(path):
    return time.ctime(os.path.getmtime(path))


def to_list(obj):
    if type(obj) in (type(()), type([])):
        return obj
    else:
        return [obj]


class MTimeMixin:
    """
        Mixin that flags a task as incomplete if any requirement
        is incomplete or has been updated more recently than this task
        This is based on http://stackoverflow.com/a/29304506, but extends
        it to support multiple input / output dependencies.
    """

    def complete(self):

        if not all(os.path.exists(out.path) for out in to_list(self.output())):
            return False

        self_mtime = min(mtime(out.path) for out in to_list(self.output()))

        # the below assumes a list of requirements, each with a list of outputs. YMMV
        for el in to_list(self.requires()):
            if not el.complete():
                return False
            for output in to_list(el.output()):
                if mtime(output.path) > self_mtime:
                    return False

        return True


class FileExists(luigi.Task):
    filename = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.filename)

    def run(self):
        pass


# take heed - mixin order in python is SUPER critical...
class CountLines(MTimeMixin, luigi.Task):
    def requires(self):
        """
        What is the input to this task?
        This is an array because there could be many inputs to one task.
        """
        return [FileExists(filename='input.txt')]

    def output(self):
        """
        Where will this Task produce output?
        This is just a single output.
        """
        return luigi.LocalTarget('output.txt')

    def run(self):
        """
        How do I run this Task?
        """
        count = 0
        for i in self.input():
            with i.open() as f_in:
                while f_in.readline():
                    count += 1
        with self.output().open('w') as f_out:
            f_out.write(str(count))


# luigi.run()
luigi.run(main_task_cls=CountLines, local_scheduler=True)
# luigi.run(['--local-scheduler','CountLines'])
