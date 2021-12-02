from pdf2image import convert_from_path
from pylibdmtx.pylibdmtx import decode
from django.conf import settings
from time import sleep



def make_csv(file):
	kms = []
	linktofile = str(settings.MEDIA_ROOT) + "/" + file
	csv_dwn = str(settings.MEDIA_URL) + file[:-3] + "csv"
	csv_link = linktofile[:-3] + "csv"
	csv_file = open(csv_link, "w")
	images = convert_from_path(linktofile, 300)
	for i in range(len(images)):
		dec = decode(images[i], 172, 170)
		kms.append(dec)
		code = str(str(dec)[16:-55])
		csv_file.write(code[:31] + code[35:41] + code[45:] + "\n")
	csv_file.close()
	return csv_dwn
	
def make_csv_test(file):
	csv_dwn = str(settings.MEDIA_URL) + file[:-3] + "csv"
	sleep(3)
	return csv_dwn

#010466010514024521i?i.0X&=&w5Lj\x1d910094\x1d92lxYVX9l7dLCT/uqRUkvQ2OQKHWK9OqBcdLcwDPyk+OwwaklLY6wHQhG0Z466NxMLAksrecLEHRuzrv1fH8Sl5A==

# [Decoded(data=b'010466010514027621)ZPTsFWoUgqe,\x1d910094\x1d92ZCUruNv8/rQRlZyH/mZhkRY11D5aW4aLjpVn3DVxFIi7l9gV/pvguWxiVnpTRI0SFkNx1dPavcQYjiQ6DCSnNw==', rect=Rect(left=36, top=134, width=172, height=170))]
