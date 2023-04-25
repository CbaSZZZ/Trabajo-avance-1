from tensorflow.python.ops.math_ops import sign
import cv2 as cv
import os
from google.colab.patches import cv2_imshow
import datetime


lista_personas = [{'identificacion' : 204820191 , 'nombre' : 'Maria Lisbeth Gamboa Durán', 'fecha de nacimiento' : '09/10/1972', 
          'nacionalidad' : 'Costarricense' , 'Gender' : 'female' , 'telefono' : {'numero1' : 88867325, 'numero2' : 24747024} , "emails" : 
          ['lisbethgamboad72@gmail.com'] ,'direccion' : 'Florencia, detras de la comancancia', 'estado_civil' : 'Casada', 
          'cantidad_hijos' : {'hijo1': {'genero' : 'male', 'fecha_nacimiento' : '03/10/2005'} , 'hijo2': {'genero' : 'male', 'fecha_nacimiento' : '10/08/2012'}}}, 
         
         {'identificacion' : 502940102 , 'nombre' : 'Lidieth Espinoza Coronado', 'fecha de nacimiento' : '14/05/1976', 
          'nacionalidad' : 'Costarricense' , 'Gender' : 'female' , 'telefono' : {'numero1' : 83166265} , "emails" : 
          ['lespinozac76@gmail.com'] ,'direccion' : 'Frente al cementerio de Florencia', 'estado_civil' : 'Soltera', 
          'cantidad_hijos' : {'hijo1': {'genero' : 'male', 'fecha_nacimiento' : '27/03/2003'} , 'hijo2': {'genero' : 'female', 'fecha_nacimiento' : '12/09/2012'}}}]


"""
Recibe una imgen y crea un diccionario con las emociones de los rostros

Args: Una foto

Return: Un diccionario con las emociones
"""
def generador_emociones(limg):
  img = cv.imread(limg)
  gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  faces_detected = face_haar_cascade.detectMultiScale(gray_image,1.32,5)
  im2Display = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  imTemp = im2Display.copy()
  for (x,y,w,h) in faces_detected:
    cv2.rectangle(img,(x,y), (x+w,y+h), (255,0,0), thickness=7)
    roi_gray=gray_image[y:y+w,x:x+h]
    roi_gray=cv2.resize(roi_gray,(48,48))
    image_pixels = tf.keras.preprocessing.image.img_to_array(roi_gray)
    image_pixels = np.expand_dims(image_pixels, axis = 0)
    image_pixels /= 255
    predictions = model.predict(image_pixels , verbose=0)
    max_index = np.argmax(predictions[0])
    emotion_detection = ('angry', 'disgust', 'fear', 'happyness', 'sadness', 'surprise', 'neutral')
    emotion_prediction = emotion_detection[max_index]
    frame_dic = dict(
      angry = predictions[0][0],
      disgust = predictions[0][1],
      fear = predictions[0][2],            
      happiness = predictions[0][3],
      sadness = predictions[0][4],
      surprise = predictions[0][5],
      neutral = predictions[0][6]) 
  return frame_dic
  

"""
Recibe la fecha de nacimiento de la lista de persona y la convierte en edad mediante datetime

Args: Fecha de nacimiento

Return: Edad de la persona
"""
def encontrar_edad():
  for item in lista_personas:
    fecha_nacimiento = datetime.datetime.strptime(item['fecha de nacimiento'] , '%d/%m/%Y')
    fecha_actual = datetime.datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
  return edad

entrevista_1 = []
entrevista_2 = []

for item in lista_personas:
  if item['identificacion'] == 204820191:
    ruta_carpeta = '/content/drive/MyDrive/Proyecto/Images/Fotos_Entrevista1'
    archivos = os.listdir(ruta_carpeta)
    lista_x = []
    lista_x.append(item['identificacion'])
    lista_x.append(item['nombre'])
    lista_x.append(item['Gender'])
    lista_x.append(encontrar_edad())
    entrevista_1.append(lista_x)
    for archivo in archivos:
      lista_x = []
      limg = os.path.join(ruta_carpeta, archivo)
      emotion = generador_emociones(limg)
      lista_x.append(emotion)
      entrevista_1.append(lista_x)
      cv2.destroyAllWindows()

  elif item['identificacion'] == 502940102:
    ruta_carpeta = '/content/drive/MyDrive/Proyecto/Images/Fotos_Entrevista2'
    archivos = os.listdir(ruta_carpeta)
    lista_x = []
    lista_x.append(item['identificacion'])
    lista_x.append(item['nombre'])
    lista_x.append(item['Gender'])
    lista_x.append(encontrar_edad())
    entrevista_2.append(lista_x)
    for archivo in archivos:
      lista_x = []
      limg = os.path.join(ruta_carpeta, archivo)
      emotion = generador_emociones(limg)
      lista_x.append(emotion)
      entrevista_2.append(lista_x)
      cv2.destroyAllWindows()

print(entrevista_1 , entrevista_2)