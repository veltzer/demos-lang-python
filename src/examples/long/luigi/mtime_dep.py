"""
This is an example of how to use luigi to get "make" like functionality regarding dependencies.

Lets explain:
by default luigi only updates targets which *DO NOT EXIST*, with no relation to time stamps.
That means that if the output file of a task exists, it will not be recreated even if the time
stamp of the input has changed and the input is now newer than the target.

This could be altered by overriding the "complete" method of luigi.Task.
References:
http://stackoverflow.com/questions/28793832/can-luigi-rerun-tasks-when-the-task-dependencies-become-out-of-date
"""

import os.path
import time

import luigi


def mtime(path):
    return time.ctime(os.path.getmtime(path))


class DepTask(luigi.Task):
    def complete(self):
        """Flag this task as incomplete if any requirement is incomplete or has been updated more
        recently than this task"""

        # assuming 1 output
        if not os.path.exists(self.output()[0].path):
            return False

        self_mtime = mtime(self.output()[0].path)

        # the below assumes a list of requirements, each with a single output
        for el in self.requires():
            if not el.complete():
                return False
            output = el.output()
            if mtime(output.path) > self_mtime:
                return False

        return True


class FileExists(luigi.Task):
    filename = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.filename)

    def run(self):
        pass


class CountLines(DepTask):
    def requires(self):
        """
        What is the input to this task?
        This is an array because there could be many inputs to one task.
        """
        return [FileExists(filename="input.txt")]

    def output(self):
        """
        Where will this Task produce output?
        This is just a single output.
        """
        return luigi.LocalTarget("output.txt")

    def run(self):
        """
        How do I run this Task?
        """
        count = 0
        for i in self.input():
            with i.open() as f_in:
                while f_in.readline():
                    count += 1
        with self.output().open("w") as f_out:
            f_out.write(str(count))


# luigi.run()
luigi.run(main_task_cls=CountLines, local_scheduler=True)
# luigi.run(["--local-scheduler","CountLines"])
