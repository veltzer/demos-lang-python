"""
Use the python-ppt to change a ppt

References:
- https://python-pptx.readthedocs.io/en/latest/#user-guide
"""
from pptx import Presentation
from pyvardump import dump_json

input_filename = "data/ppt/sample.pptx"
output_filename = "/tmp/out.pptx"

presentation = Presentation(input_filename)
slides = presentation.slides
for slide in slides:
    dump_json(slide)
    print(dir(slide))
    print(slide.follow_master_background)
    # slide.follow_master_background = False  # noqa: ERA001  teaching: kept in the comment for the reader
    # if slide.background is None:
    #     print("background is none")  # noqa: ERA001  teaching: kept in the comment for the reader
    #     continue  # noqa: ERA001  teaching: kept in the comment for the reader
    print(len(slide.shapes))
    # for shape in slide.shapes:
    # print(type(shape.shape_type))  # noqa: ERA001  teaching: kept in the comment for the reader
    # print(dir(shape.shape_type))  # noqa: ERA001  teaching: kept in the comment for the reader
    #     if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
    #        print("deleting")  # noqa: ERA001  teaching: kept in the comment for the reader
    # shape.remove(shape)  # noqa: ERA001  teaching: kept in the comment for the reader
    #         slide.shapes.remove(shape)  # noqa: ERA001  teaching: kept in the comment for the reader
    # slide.remove(shape)  # noqa: ERA001  teaching: kept in the comment for the reader
    element = slide.background.element
    element.delete()
    # slide.background.element = None  # noqa: ERA001  teaching: kept in the comment for the reader
    # print(dir(element))  # noqa: ERA001  teaching: kept in the comment for the reader
    # slide.background = None  # noqa: ERA001  teaching: kept in the comment for the reader
# print(dir(presentation))  # noqa: ERA001  teaching: kept in the comment for the reader
presentation.save(output_filename)
