# from transformers import pipeline
# from PIL import Image

# # Initialize the image classification pipeline
# # classifier = pipeline("image-classification")
# # Alternatively you can define what model should the pipeline use, sometimes it requires that you login with your token
# classifier = pipeline("image-classification", model="ind4rk/mushrooms", token="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")

# #print(classifier.model)

# def classify_image(image):
#     results = classifier(image)
#     # Get the top prediction
#     top_result = results[0]
#     label = top_result['label']
#     score = top_result['score']
#     return f"Label: {label}, Confidence: {score:.2f}"

# image = Image.open("/mnt/boletus-rex-veris-300x300.png")

# print("Predicted class:", classify_image(image))


# from transformers import pipeline
# from PIL import Image
# #image_path = "https://farm5.staticflickr.com/4007/4322154488_997e69e4cf_z.jpg"
# image_path = "/mnt/boletus-rex-veris-300x300.png"
# pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
# pillow_mask = pipe(image_path, return_mask = True) # outputs a pillow mask
# pillow_image = pipe(image_path) # applies mask on input and returns a pillow image

# # Guardar la máscara de segmentación (si la tienes)
# if pillow_mask:
#     pillow_mask.save("mask.png")  # Guarda la máscara como una imagen PNG

# pillow_image = pillow_image.convert('RGB')
# # Guardar la imagen segmentada
# pillow_image.save("segmented_image.jpg")  # Guarda la imagen segmentada como JPEG



from transformers import pipeline
from PIL import Image
import os

# Directorio donde se encuentran los archivos
directorio = "mushrooms"
destino = "resultado"

        
for root, dirs, files in os.walk(directorio):
    count = 1
    for file in files:
        if file.endswith(('.jpg', '.jpeg', '.png')):  # Ajusta las extensiones según tus necesidades
            ruta_completa = os.path.join(root, file)
            try:
                # extension = os.path.splitext(file)[1]
                # Obtener el directorio contenedor
                directorio = os.path.dirname(ruta_completa)
                # Obtener solo el nombre de la carpeta
                nombre_carpeta = os.path.basename(directorio)

                # Crear el nuevo nombre
                # new_filename = f"{directorio}{count}{extension}"
                # # Construir las rutas completas de los archivos
                # old_filepath = os.path.join(directorio, file)
                # new_filepath = os.path.join(directorio, new_filename)
                # # Renombrar el archivo
                # os.rename(old_filepath, new_filepath)
                # count += 1
                # print(new_filepath)
                #image_path = "/mnt/boletus-rex-veris-300x300.png"
                old_filepath = os.path.join(directorio, file)
                pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
                pillow_mask = pipe(old_filepath, return_mask = True) # outputs a pillow mask
                pillow_image = pipe(old_filepath) # applies mask on input and returns a pillow image

                # Guardar la máscara de segmentación (si la tienes)
                # if pillow_mask:
                #     pillow_mask.save("mask.png")  # Guarda la máscara como una imagen PNG

                #pillow_image = pillow_image.convert('RGB')

                os.makedirs(f"/mnt/{destino}/{nombre_carpeta}", exist_ok=True)

                # Guardar la imagen segmentada
                pillow_image.save(f"/mnt/{destino}/{nombre_carpeta}/{nombre_carpeta}{count}.png")  # Guarda la imagen segmentada como JPEG
                count += 1

            except OSError as e:
                print(f"Error al procesar {ruta_completa}: {e}")
