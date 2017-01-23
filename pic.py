from PIL import Image
import glob, os

mini = (180, 120)
# size = (960, 640)

def resizeimg():
	n = glob.glob('*.jpg')
	for infile in n:
		file, ext = os.path.splitext(infile)
		# reducida = Image.open(infile).resize(size)
		# reducida.save(infile)
		im = Image.open(infile)
		im.thumbnail(mini)
		directory = "test/test1/{}".format(file)
		
		im.save("{}.jpg".format(directory))


resizeimg()