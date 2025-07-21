import os
import numpy as np
import shutil

path = '/home/jspark/lsmm_proj/facenet-master/datasets/lfw/K-face'

folderN = os.listdir(path)
def createFolder(directory):
  try:
  if not os.path.exists(directory):
    os.makedirs(directory)
  except OSError:
    print('Error')

testpath = '/home/jspark/lsmm_proj/facenet-master/datasets/lfw/K-face_Test_svm/'
for subdir in folderN:
  output = glob.glob(subdir + '*.jpg')
  nFile = len(output)
  nTest = int(np.round(nFile*0.2))
  directory = subdir[0][-8:-1]


  newPath = testpath + directory
  createFolder(subdir)
  shutil.move(output)





