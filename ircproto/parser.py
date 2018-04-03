from .events import Mask


def mask_from_group(grp):
    try:
        nick, rest = grp.split('!')
        username, host = rest.split('@')
        return Mask(nick=nick, user=username, host=username)
    except (AttributeError, ValueError):
        return None


def arguments_from_group(grp):
    # thanks python-irclib
    if not grp:
        return []

    main, sep, ext = grp.partition(" :")
    arguments = main.split()
    if sep:
        arguments.append(ext)

    return arguments
