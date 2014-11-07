import os

from contracts import contract

from procgraph.utils import system_cmd_result, CmdException

from .metadata import read_extra_metadata_for, ffmpeg_get_metadata
from .timestamps import TIMESTAMP_FIELD, timestamp_from_iso
from contracts.utils import raise_wrapped


@contract(returns='dict(str:*)')
def pg_video_info(filename):
    """
          Returns a dictionary, with fields:
        
            metadata
            
            width, height
            fps
            length 
            
            timestamp # start timestamp
                        
            extra_mencoder_info
                
        Tries to read precise timestamp from metadata; otherwise 
        it tries from the .timestamps file; otherwise from the file's mtime.
    """

    info = mplayer_identify(filename)
    
    info['metadata'] = ffmpeg_get_metadata(filename)
        
    extra_md = read_extra_metadata_for(filename)
    
    info['metadata'].update(extra_md)
    
    precise = info['metadata'].get(TIMESTAMP_FIELD, None)
    if precise is None:
        # logger.info('No precise timestamp in metadata found for %s' % filename)
        timestamp = os.path.getmtime(filename)
    else:
        # logger.info('Precise timestamp found for %s' % filename)
        timestamp = timestamp_from_iso(precise)
        
    timestamps = filename + '.timestamps'
    if os.path.exists(timestamps):
        # logger.info('Reading timestamps from %r.' % timestamps)
        f = open(timestamps)
        line = f.readline()
        # print('frist line: %s' % line)
        timestamp = float(line)
        # print('timestamp: %s' % timestamp)


    info['timestamp'] = timestamp
    
    return info



def mplayer_identify(filename):
    """
        Returns a dictionary, with fields:
        
            width, height
            fps
            length 
            
            extra_mencoder_info
    
    """
    keys = ["ID_VIDEO_WIDTH", "ID_VIDEO_HEIGHT",
            "ID_VIDEO_FPS", "ID_LENGTH"]
    id_width, id_height, id_fps, id_length = keys

    args = ('mplayer -identify -vo null -ao null -frames 0'.split()
            + [filename])
    
    try:
        try:
            res = system_cmd_result('.', args,
                      display_stdout=False,
                      display_stderr=False,
                      raise_on_error=True,
                      capture_keyboard_interrupt=False)
        except CmdException:
            raise
            
        output = res.stdout
    
        info = {}
        for line in output.split('\n'):
            if line.startswith('ID_'):
                key, value = line.split('=', 1)
                try:  # interpret numbers if possible
                    value = eval(value)
                except:
                    pass
                info[key] = value
    
    
        for k in keys:
            if not k in info:
                msg = ('Could not find key %r in properties %s.' % 
                      (k, sorted(info.keys())))
                raise Exception(msg)
    
        if id_length == 0:
            msg = 'I could not find find the length of this video.'
            msg += (' I ran:\n\t%s\n and this is the output:\n' % 
                   (" ".join(args), output))
            raise Exception(msg)
    except Exception as e:
        raise_wrapped(Exception, e, "Could not identify movie", 
                      filename=filename)

    res = {}
    res['width'] = info[id_width]
    res['height'] = info[id_height]
    res['fps'] = info[id_fps]
    res['length'] = info[id_length]
    res['extra_mencoder_info'] = info
    return res
