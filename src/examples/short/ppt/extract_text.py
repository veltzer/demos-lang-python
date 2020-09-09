"""
Extract text from a ppt file

References:
- https://www.syncfusion.com/kb/8672/how-to-extract-text-from-a-powerpoint-presentation
- https://python-pptx.readthedocs.io/en/latest/#user-guide
"""
import json
import types
from collections.abc import Iterable
from itertools import islice
from pprint import pprint

from pptx import Presentation
import sys

from pptx.enum.shapes import MSO_SHAPE_TYPE
from var_dump import var_dump


def dump(obj, level=0):
    try:
        for a in dir(obj):
            # print(a)
            if a.startswith("_"):
                continue
            if a in {"adjustments", "auto_shape_type"}:
                continue
            val = getattr(obj, a)
            # print(type(val))
            if type(val) in {int, float, str, list, dict, set}:
                print(level*' ', val)
            else:
                dump(val, level=level+1)
    except TypeError:
        print(str(type(obj)))
    except AttributeError:
        print(str(type(obj)))


def dump_obj(obj, level=0):
    if hasattr(obj, '__dict__'):
        for key, value in obj.__dict__.items():
            if isinstance(value, (int, float, str, list, dict, set)):
                print(" " * level + "%s -> %s" % (key, value))
            else:
                dump_obj(value, level + 2)


def default_func(obj):
    try:
        return dir(obj)
        # return obj.__dict__
    except TypeError:
        return str(type(obj))
    except AttributeError:
        return str(type(obj))


def dump_json(obj):
    # json.dump(obj, fp=sys.stdout, indent=2, default=default_func)
    json.dump(obj, fp=sys.stdout, indent=2)


def object_to_members_or_string(obj):
    try:
        if hasattr(obj, "__dict__"):
            return vars(obj)
        return str(obj)
    except TypeError:
        return str(obj)


def flat_dump(obj) -> None:
    """
    Dump object to stdout. Only dumps the immediate members of the object
    :param obj:
    """
    print("===========start dump=======")
    try:
        for x in dir(obj):
            if x.startswith("_"):
                continue
            try:
                v = getattr(obj , x)
            except Exception:
                v = "AttributeError"
            print(f"{x} -> {v}")
    except Exception:
        print("Cannot flat_dump")


input_filename = sys.argv[1]

presentation = Presentation(input_filename)
slides = presentation.slides
for slide_number, slide in enumerate(islice(slides, None)):
    print(f"slide number {slide_number}")
    if slide.name != "":
        print(f"slide.name {slide.name}")
    # This block extracts hyperlinks
    for v in slide.part.rels.values():
        target: str = v.target_ref
        if target.startswith(".."):
            continue
        print(v.target_ref)
    for shape in slide.shapes:
        if shape.shape_type == MSO_SHAPE_TYPE.PLACEHOLDER:
            print(shape.shape_type)
            print(shape.text)
        if shape.shape_type == MSO_SHAPE_TYPE.TEXT_BOX:
            print(shape.shape_type)
            print(shape.text)
        if shape.shape_type == MSO_SHAPE_TYPE.TABLE:
            print(shape.shape_type)
            for row in shape.table.rows:
                for cell in row.cells:
                    print(cell.text)
