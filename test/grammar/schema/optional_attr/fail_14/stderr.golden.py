import sys
import os

import kclvm.kcl.error as kcl_error

cwd = os.path.dirname(os.path.realpath(__file__))

kcl_error.print_kcl_error_message(
    kcl_error.get_exception(err_type=kcl_error.ErrType.EvaluationError_TYPE,
                            file_msgs=[
                                kcl_error.ErrFileMsg(
                                    filename=os.path.join(cwd, "main.k"),
                                    line_no=10,
                                ),
                            ],
                            arg_msg="attribute 'a' of S is required and can't be None or Undefined")
    , file=sys.stdout
)
