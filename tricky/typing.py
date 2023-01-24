import sys

if sys.version_info > (3, 7):
    class Bool(str): ...  # noqa: E701

    class String(str): ...  # noqa: E701

    class Integer(int): ...  # noqa: E701

    class Float(str): ...  # noqa: E701

    class List(list): ...  # noqa: E701

if sys.version_info > (3, 8):
    print(sys.version)

if sys.version_info > (3, 9):
    print(sys.version_info)
