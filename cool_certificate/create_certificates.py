# coding: utf-8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont

import os

current_path = os.path.dirname(os.path.abspath(__file__))

def write_words_on_img(img_path, out_img_path, name, font_path, font_size, word_pos, word_color): 
	img = Image.open(img_path)
	draw = ImageDraw.Draw(img)
	#font = ImageFont.load_default().font
	font = ImageFont.truetype(font_path, font_size)
	#NOTE: django get parameter as unicode, so don't need to encode to unicode.
	draw.text(word_pos, name, word_color, font=font)
#	img = img.filter(ImageFilter.GaussianBlur(1))
	img.save(out_img_path)

def feiji(name):
	write_words_on_img(current_path+'/static/imgs/feiji.jpg', current_path+'/static/imgs/feiji_out.jpg', name, '/usr/share/fonts/ariauni.ttf', 20, (260,328), (69,97,119))

def chaojishuaige(name):
	write_words_on_img(current_path+'/static/imgs/chaojishuaige.jpg', current_path+'/static/imgs/chaojishuaige_out.jpg', name, '/usr/share/fonts/ariauni.ttf', 13, (348,125), (41, 45, 46))

def qianshui(name):
	write_words_on_img(current_path+'/static/imgs/qianshui.jpg', current_path+'/static/imgs/qianshui_out.jpg', name, '/usr/share/fonts/ariauni.ttf', 13, (350,135), (41, 45, 46))

if __name__ == '__main__':
	feiji('root')
	chaojishuaige('root')
	qianshui('root')
