from model.core import ModelCore
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text

import os


class SRACore(ModelCore):
	tfhub_handle_preprocess = "https://tfhub.dev/tensorflow/bert_en_cased_preprocess/3"
	tfhub_handle_encoder = "https://tfhub.dev/tensorflow/bert_en_cased_L-12_H-768_A-12/3"

	def build_model(self):
		input = tf.keras.layers.InputLayer([1], dtype=tf.strings)

		bert_preprocess_model = hub.KerasLayer(SRACore.tfhub_handle_preprocess)
		text_preprocessed = bert_preprocess_model(input)
		bert_model = hub.KerasLayer(SRACore.tfhub_handle_encoder)
		output = bert_model(text_preprocessed)

		self.model = tf.keras.Model(inputs=[input], outputs=[output])

	def read_data(self):
		for file in os.listdir():
			# Check whether file is in text format or not
			if file.endswith(".txt"):
				file_path = os.path.join(self._data_path, file)

				# call read text file function
				contents = ""

				with open(file_path, "r", encoding="utf8") as f:
					contents = f.read()

				self._data_all.append({'input': [contents]})
