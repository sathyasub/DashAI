from fastai.vision import *
from core.databunch import DashDatabunch
from fastai.data_block import *
from path import Path



# Only tested with Mnist
class DashVisionDatabunch:

	@staticmethod
	def create_vision_databunch(response):
		path = Path('./')

		src = DashVisionDatabunch.get_itemlist(response["vision"])
		src = DashDatabunch.split_databunch(response, src)
		src = DashDatabunch.label_databunch(response, src)

		# Add test

		#for now
		src = src.transform(get_transforms(), tfm_y=True)


		return DashDatabunch.create_databunch(response, src, collate_fn = bb_pad_collate)

	@staticmethod
	def get_itemlist(response):
		# path = Path('data/mnist_tiny')
		# if response["subtask"] == "classification-single-label":
		if response["subtask"] == "object-detection":
			return ObjectItemList.from_folder(path = response["input"]["from_folder"]["path"])
		if response["input"]["method"] == "from_folder":
			return ImageList.from_folder(response["input"]["from_folder"])
		if response["input"]["method"] == "from_csv":
			return ImageList.from_csv(response["input"]["from_csv"])
			
	