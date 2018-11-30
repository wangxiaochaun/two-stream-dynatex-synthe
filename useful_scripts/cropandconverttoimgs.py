import os
from PIL import Image


def analyseImage(path):
    img = Image.open(path)
    results = {
        'size': img.size,
        'mode': 'full',
    }
    try:
        while True:
            if img.tile:
                tile = img.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2: ]
                if update_region_dimensions != img.size:
                    results['mode'] = 'partial'
                    break
            img.seek(img.tell() + 1)
    except EOFError:
        pass
    return results


def processImage(path):
    mode = analyseImage(path)['mode']

    img = Image.open(path)

    i = 0
    p = img.getpalette()
    last_frame = img.convert('RGBA')

    try:
        while True:
            print("Saving %s (%s) frame %d, %s %s" % (path, mode, i, img.size, img.tile))

            '''
            if the gif uses local color tables, each frame will have its own palette.
            if not, we need to apply the global palette to the new frame
            '''
            if not img.getpalette():
                img.putpalette(p)

            new_frame = Image.new('RGB', img.size)
            '''
            is this file a "partial"-mode GIF where frames update a region of a different size
            if so, we need to construct the new frame by pasting it op top of the preceding frame
            '''
            if mode == 'partial':
                new_frame.paste(last_frame)

            new_frame.paste(img, (0, 0), img.convert('RGBA'))
            new_frame = new_frame.crop((100, 0, 356, 256))
            new_frame = new_frame.convert("RGB")
            new_frame.save('%s-%d.png' % (''.join(os.path.basename(path).split('.')[: -1]), i), 'PNG')

            i += 1
            last_frame = new_frame
            img.seek(img.tell() + 1)
    except EOFError:
        pass

processImage('sea1.gif')
