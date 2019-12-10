'''
@Author: Dandan Shan
@Date: 2019-10-08 00:44:39
@LastEditTime: 2019-10-10 04:05:06
@Descripation: 
'''
from PIL import Image



def resize(path, name):
    image = Image.open(path)
    print(image.size)
    image = image.resize((260*4, 195*4)).convert('RGB')
    image.save(f'./images/{name}.jpg')

# image = Image.open('/home/dandans/public_html/dandan.webpage/images/M.jpg')
# image = image.resize((920/425*195, 195))
# image = image.crop((65, 0, 390-65, 195))
# image.save('/home/dandans/public_html/dandan.webpage/images/M_new.jpg')
# print(image.size)
resize('images/CV_UMich.png', 'CV_UMich_new')