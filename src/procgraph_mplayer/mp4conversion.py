from procgraph.utils import system_cmd_result, CmdException
import os


def convert_to_mp4(filename, mp4=None, quiet=True):
    """ 
        Creates a web-ready mp4 using ffmpeg.
    
        Needs either qtquickstart (from the python package) or qt-quickstart from ffmpeg.
        
        On ubuntu 12.04: need 'sudo apt-get install x264 libavcodec-extra-53'
        to install necessary codecs.
        You can see a list of supported presets by using: 'x264 --help'.
    
        
        (other packages that might be helpful: # libavdevice-extra-52  libavfilter-extra-0 
         libavformat-extra-52 libavutil-extra-49 libpostproc-extra-51 libswscale-extra-0)
       
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

    # Let's detect ffmpeg version
    res = system_cmd_result('.', ['ffmpeg', '-version'])
    ffmpeg_version = res.stdout.split('\n')[0]
    
    # SVN-r0.5.9-4:0.5.9-0ubuntu0.10.04.3
    
    # if 'ubuntu0.10.04.3' in ffmpeg_version:
    if '0.5' in ffmpeg_version:
        presets = ['-vpre', 'libx264-default']
    else:
        presets = ['-preset', 'medium']
        
    # print('Version string: %s' % ffmpeg_version)

    cmds = ['ffmpeg', '-y', '-i', filename,
            # TODO: detect whether we can use these presets
            # TODO: make presets configurable
            '-vcodec', 'libx264']
    cmds.extend(presets)
    cmds += ['-crf', '22',
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
