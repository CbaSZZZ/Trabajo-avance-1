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
Recibe una foto a la que le agrega las cordenadas de la cara, emociones y un cuadrado donde detecte la cara

Args: Una foto de un rostro

Return: Devuelve una foto con las cordenadas de la cara, emociones y un cuadrado donde detecte la cara
"""
def analizar_imagen(limg):
  img = cv.imread(limg)
  gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  faces_detected = face_haar_cascade.detectMultiScale(gray_image,1.32,5)
  print("Ubicación del rostro:", faces_detected)
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
    print(frame_dic)
    print(emotion_prediction)
    ubicacion = (x,y)
    font = cv2.FONT_HERSHEY_TRIPLEX
    tamañoLetra = 2
    colorLetra = (221,82,196)
    grosorLetra = 7
    cv2.putText(imTemp, emotion_prediction, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
    pt1 = (x, y)
    pt2 = (x+w, y+h)
    color = (23,200,54)
    thickness = 10
    cv2.rectangle(imTemp, pt1, pt2, color, thickness)
    plt.imshow(imTemp)
    plt.show()


"""
Encuentra el mayor en una lista

Args: Una lista con numeros desordenados

Return: El mayor de esa lista
"""
def mayor_lista(lista):
    if len(lista)==0:
        return (None)
    else:
        mayor=lista[0]
        for x in lista[1:]:
            if x>mayor:
                mayor=x
        return(mayor) 

"""
Ordena una lista

Args: Una lista y el mayor temporal de esa lista

Return: Una nueva lista ordenada
"""
def ordenamiento_insercion(lista):
    nueva_lista = []
    while len(lista)>0:
        mayor=mayor_lista(lista)
        nueva_lista.insert(0,mayor)
        lista.remove(mayor)
    return nueva_lista



lista = []
for item in lista_personas:
  fecha_nacimiento = datetime.datetime.strptime(item['fecha de nacimiento'] , '%d/%m/%Y')
  fecha_actual = datetime.datetime.now()
  edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
  lista.append(edad)
mayor_lista(lista)
nueva_lista = ordenamiento_insercion(lista)
cont = 0
while cont < len(lista_personas):
  for persona in lista_personas:
    fecha_nacimiento = datetime.datetime.strptime(persona['fecha de nacimiento'] , '%d/%m/%Y')
    fecha_actual = datetime.datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    if nueva_lista == []:
      pass
    elif edad == nueva_lista[- 1]:      
      for item in lista_personas:
        if persona["identificacion"] == item["identificacion"]:
          print("Identificacion:", item["identificacion"])
          print("Nombre:", item["nombre"])
          print("Fecha de nacimiento:", item["fecha de nacimiento"])
          print("Nacionalidad:", item["nacionalidad"])
          telefono = item["telefono"]
          print('Telefono :')
          for x , y in telefono.items():
            print(x , y)
          print("Emails:")
          for email in item["emails"]:
              print(email)
          print("Direccion:", item["direccion"])
          print("Estado civil:", item["estado_civil"])
          print("Cantidad de hijos:")
          for hijo, datos in item["cantidad_hijos"].items():
            print(" Hijo:", hijo)
            print(" Genero:", datos["genero"])
            print(" Fecha de nacimiento:", datos["fecha_nacimiento"])
          if item['identificacion'] == 204820191:
            ruta_carpeta = '/content/drive/MyDrive/Proyecto/Images/Fotos_Entrevista1'
            archivos = os.listdir(ruta_carpeta)
            for archivo in archivos:
              limg = os.path.join(ruta_carpeta, archivo)
              analizar_imagen(limg)
              cv2.destroyAllWindows()
          elif item['identificacion'] == 502940102:
            ruta_carpeta = '/content/drive/MyDrive/Proyecto/Images/Fotos_Entrevista2'
            archivos = os.listdir(ruta_carpeta)
            for archivo in archivos:
              limg = os.path.join(ruta_carpeta, archivo)
              analizar_imagen(limg)
              cv2.destroyAllWindows()
      nueva_lista.pop()
      cont += 1
    else:
      pass

