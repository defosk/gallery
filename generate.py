import glob
from pathlib import Path


def create(folder_dir):
    images = []
    images.extend(glob.iglob(f'{folder_dir}/*'))
    images.extend(glob.iglob(f'{folder_dir}/**/*'))
    gallery_list = []
    for idx, image in enumerate(images):
        # check if the image ends with png or jpg or jpeg
        if (image.endswith(".png") or image.endswith(".jpg") or image.endswith(".jpeg")):
            path = image.replace(folder_dir, '').lstrip('/')
            item = f'''
                <a id="item-{idx}" href="/img/{path}" data-pswp-width="1200" data-pswp-height="600">
                    <img id="item-{idx}-image" class="lozad" data-src="/preview?img_path={path}" alt=""/>
                    <div id="item-{idx}-loader" class="lds-facebook"><div></div><div></div><div></div></div>
                </a>
                
            '''
            gallery_list.append(item)
    gallery_html = ' '.join(gallery_list)
    html = Path('tmp.html').read_text()
    html = html.replace('{{gallery_html}}', gallery_html)
    file = open(f'{folder_dir}/index.html', 'w')
    file.write(html)
