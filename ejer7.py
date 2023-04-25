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


emociones_1 = [{'angry': 0.10119841, 'disgust': 0.004195313, 'fear': 0.07053033, 'happiness': 0.2610281, 'sadness': 0.17423424, 'surprise': 0.01339811, 'neutral': 0.37541544},
             {'angry': 0.1286198, 'disgust': 0.004451646, 'fear': 0.3801115, 'happiness': 0.0011528326, 'sadness': 0.3957117, 'surprise': 0.009422931, 'neutral': 0.080529615},
             {'angry': 0.0053338064, 'disgust': 8.070903e-05, 'fear': 0.0029822472, 'happiness': 0.8399899, 'sadness': 0.0074582463, 'surprise': 0.0027992653, 'neutral': 0.14135583},
             {'angry': 0.00050308445, 'disgust': 4.7456488e-06, 'fear': 0.0009822247, 'happiness': 0.98893166, 'sadness': 0.0007247183, 'surprise': 0.0014038646, 'neutral': 0.007449827}]

emociones_2 = [{'angry': 0.1591461, 'disgust': 0.009909924, 'fear': 0.19247945, 'happiness': 0.05955094, 'sadness': 0.21374543, 'surprise': 0.06768564, 'neutral': 0.29748252},
              {'angry': 0.09891662, 'disgust': 0.004537768, 'fear': 0.052491672, 'happiness': 0.30518034, 'sadness': 0.10851848, 'surprise': 0.018608175, 'neutral': 0.41174695},
              {'angry': 0.016965296, 'disgust': 0.0003899955, 'fear': 0.018776843, 'happiness': 0.8419237, 'sadness': 0.012651512, 'surprise': 0.024389206, 'neutral': 0.08490333}, 
              {'angry': 0.0027494214, 'disgust': 4.565562e-05, 'fear': 0.0027756998, 'happiness': 0.9341804, 'sadness': 0.0052266982, 'surprise': 0.0023739669, 'neutral': 0.05264813}]

for d in emociones_1:
    plt.bar(range(len(d)), list(d.values()), align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.title('Emociones durante la entrevista 1')
    plt.show()
for d in emociones_2:
    plt.bar(range(len(d)), list(d.values()), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.title('Emociones durante la entrevista 2')
    plt.show()