import os
import subprocess


def convert_to_mp4(filename, mp4=None):
    """ Creates a web-ready mp4 using ffmpeg.
    
        need qtquickstart from 
    """

    basename, ext = os.path.splitext(filename)
    if ext == 'mp4':
        raise Exception('Need a file that does not end in .mp4 (%r)' %
                        filename)

    if mp4 is None:
        mp4 = basename + '.mp4'

    # need .mp4 at the end otherwise ffmpeg gets confused
    tmp = basename + '.mp4.firstpass.mp4'

    if not os.path.exists(filename):
        raise Exception("Filename %s does not exist." % filename)

    if (os.path.exists(mp4) and
        (os.path.getmtime(mp4) > os.path.getmtime(filename))):
        return

    if os.path.exists(tmp):
        os.unlink(tmp)
    if os.path.exists(mp4):
        os.unlink(mp4)

    cmds = ['ffmpeg', '-y', '-i', filename,
            # TODO: detect whether we can use these presets
            # TODO: make presets configurable
            '-vcodec', 'libx264',
            '-vpre', 'libx264-max',
            '-crf', '22',
            # '-threads', '1', # limit to one thread
             tmp]

    #print(" ".join(cmds))
    subprocess.check_call(cmds)

    # TODO: check file exists
    try:
        subprocess.check_call(['qtfaststart', tmp, mp4])
        #print('Succesfull call of qtfaststart.')
    except Exception as e:
        print("Could not call qtfaststart: %s" % e)

        try:
            # easy_install qtfaststart
            subprocess.check_call(['qt-faststart', tmp, mp4])
            #print('Succesfull call of qt-faststart.')
        except Exception as e:
            print("Could not call qtfaststart: %s" % e)
            #print("The file will not be ready for streaming.")
            os.rename(tmp, mp4)

    if os.path.exists(tmp):
        os.unlink(tmp)
