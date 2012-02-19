import os
from procgraph.utils.calling_ext_program import system_cmd_result, CmdException


def convert_to_mp4(filename, mp4=None, quiet=True):
    """ Creates a web-ready mp4 using ffmpeg.
    
        need qtquickstart from 
    """

    basename, ext = os.path.splitext(filename)
    if ext == 'mp4':
        msg = 'Need a file that does not end in .mp4 (%r)' % filename
        raise ValueError(msg)

    if mp4 is None:
        mp4 = basename + '.mp4'

    # need .mp4 at the end otherwise ffmpeg gets confused
    tmp = basename + '.mp4.firstpass.mp4'

    if not os.path.exists(filename):
        raise ValueError("File does not exist: %s" % filename)

#    if (os.path.exists(mp4) and
#        (os.path.getmtime(mp4) > os.path.getmtime(filename))):
#        return

    if os.path.exists(tmp):
        os.unlink(tmp)
    if os.path.exists(mp4):
        os.unlink(mp4)

    cmds = ['ffmpeg', '-y', '-i', filename,
            # TODO: detect whether we can use these presets
            # TODO: make presets configurable
            '-vcodec', 'libx264',
            '-vpre',
            #'libx264-max',
            'libx264-default',
#            '-vpre', 'libx264-min',
            '-crf', '22',
            # '-threads', '1', # limit to one thread
             tmp]

    try:
        system_cmd_result('.', cmds,
                  display_stdout=not quiet,
                  display_stderr=not quiet,
                  raise_on_error=True,
                  capture_keyboard_interrupt=False)
    except CmdException as e:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    # TODO: check file exists

    system_cmd_result
    names = ['qtfaststart', 'qt-faststart']
    errors = []
    for name in names:
        cmd = [name, tmp, mp4]
        try:
            system_cmd_result('.', cmd,
                      display_stdout=False,
                      display_stderr=False,
                      raise_on_error=True,
                      capture_keyboard_interrupt=False)
            break
        except CmdException as e:
            errors.append(e)

    else:
        msg = ('Could not call either of %s. '
               'The file will not be ready for streaming.\n%s' %
               (names, errors))
        os.rename(tmp, mp4)

    if os.path.exists(tmp):
        os.unlink(tmp)
