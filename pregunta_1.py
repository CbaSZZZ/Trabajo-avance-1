lista_personas = [{'identificacion' : 508410065 , 'nombre' : 'Roberto Chacon Chavarria', 'fecha de nacimiento' : '17/04/1998', 
          'nacionalidad' : 'Costarricense' , 'telefono' : {'numero1' : 67709622, 'numero2' : 62696086} , "emails" : 
          ['rchavarria@gmail.com', 'rcc2000@gmail.com'] ,'direccion' : 'Frente Plaza', 'estado_civil' : 'Casado', 
          'cantidad_hijos' : {'hijo1': {'genero' : 'female', 'fecha_nacimiento' : '14/08/2014'} , 'hijo2': {'genero' : 'female', 'fecha_nacimiento' : '22/01/2017'}}}, 
         
         {'identificacion' : 7900093123 , 'nombre' : 'Sofia Villalovos Matamoros', 'fecha de nacimiento' : '08/11/1996', 
          'nacionalidad' : 'Costarricense' , 'telefono' : {'numero1' : 87020222} , "emails" : 
          ['Sof090990@hotmail.com'] ,'direccion' : 'Frente al cementerio de platanar', 'estado_civil' : 'Soltera', 
          'cantidad_hijos' : {'hijo1': {'genero' : 'female', 'fecha_nacimiento' : '14/08/2020'} , 'hijo2': {'genero' : 'male', 'fecha_nacimiento' : '22/01/2017'}, 'hijo3': {'genero' : 'male', 'fecha_nacimiento' : '22/01/2017'}}}]



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
    predictions = model.predict(image_pixels)
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

def mostrar_informacion():
  for item in lista_personas:
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
      if item['identificacion'] == 508410065:
        ruta_carpeta = '/content/drive/MyDrive/Proyecto/Images/Sebastian'
        archivos = os.listdir(ruta_carpeta)
        for archivo in archivos:
          limg = os.path.join(ruta_carpeta, archivo)
          analizar_imagen(limg)
          cv2.destroyAllWindows()
      elif item['identificacion'] == 7900093123:
        ruta_carpeta = '/content/drive/MyDrive/Proyecto/Images/Messi'
        archivos = os.listdir(ruta_carpeta)
        for archivo in archivos:
          limg = os.path.join(ruta_carpeta, archivo)
          analizar_imagen(limg)
          cv2.destroyAllWindows()
