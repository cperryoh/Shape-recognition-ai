import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import drawWindow
import random
import pickle
#1 = square 2= circle 3=rectangle
imgres=20
pixelSize=40
data={}
lables={}
def flatten(arr):
    flat=[]
    count =0
    for x in range(imgres-1):
        for y in range(imgres-1):
            flat.append(arr[x][y])
            count+=1
    return flat
def getData():
    try:
        dbfile = open('data', 'rb')
        dta = pickle.load(dbfile)
        dbfile.close()
        lblFile =open('lables','rb')
        lbls=pickle.load(lblFile)
        lblFile.close()
        return dta,lbls
    except FileNotFoundError:
        dta=[]
        lbls=[]
        for i in range(10):
            shape = drawWindow.drawShape(cap=str(i + 1) + ")square", size=pixelSize, _res=imgres)
            dta.append(shape)
            lbls.append(0)
        for i in range(10):
            shape = drawWindow.drawShape(cap=str(i + 1) + ")circle", size=pixelSize, _res=imgres)
            dta.append(shape)
            lbls.append(1)
        for i in range(10):
            shape = drawWindow.drawShape(cap=str(i + 1) + ")rectagnle", size=pixelSize, _res=imgres)
            dta.append(shape)
            lbls.append(2)
        for i in range(len(dta)):
            index = random.randrange(len(dta))
            tempData = dta[i]
            tempLable = lbls[i]
            dta[i] = dta[index]
            dta[index] = tempData
            lbls[i] = lbls[index]
            lbls[index] = tempLable
        dbfile = open('lables', 'ab')

        # source, destination
        pickle.dump(lbls, dbfile)
        dbfile.close()
        dbfile = open('data', 'ab')

        # source, destination
        pickle.dump(dta, dbfile)
        dbfile.close()
        return dta,lbls

data,lables=getData()
model = keras.Sequential([
  keras.layers.Conv2D(input_shape=(imgres,imgres,1), filters=8, kernel_size=3, 
                      strides=2, activation='relu', name='Conv1'),
  keras.layers.Flatten(),
  keras.layers.Dense(3, name='Dense')
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(data, lables, epochs=10)
