import typing as t

AnyObject = t.TypeVar('AnyObject')
AnyDefault = t.TypeVar('AnyDefault')
AnyAttribute = t.TypeVar('AnyAttribute')


def preserve_attr(
    object_to_preserve: AnyObject,
    attribute: AnyAttribute,
    default: AnyDefault = None,
) -> t.Optional[AnyAttribute]:
    """Function is used to return attribute of specified object
    or returns None, or a value specified in default

    :param object_to_preserve: Object which attribute would be returned
    :param attribute: Any attribute of any object which must be in specified object
    :param default: Returns "default" value instead of "None"
    :return:
    """
    if hasattr(object_to_preserve, attribute) is True:
        return getattr(object_to_preserve, attribute)
    if hasattr(object_to_preserve, attribute) is False:
        return default
