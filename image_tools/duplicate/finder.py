from imagededup.methods import PHash
phasher = PHash()

encodings = phasher.encode_images(image_dir='path/to/image/directory')

duplicates = phasher.find_duplicates(encoding_map=encodings)
