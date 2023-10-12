import module_checker  # type: ignore

# this works
# module_checker.check_lib("libacl.so")
# this works
# module_checker.check_lib("libc.so.6")
# this fails
# module_checker.check_lib("libthisisanerror.so")
# this should fail
module_checker.check_lib("./libadd_wrap.so")

# debug code
# module_checker.load_lib("./libadd_wrap.so")
# while True:
#     signal.pause()
