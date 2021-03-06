#MDCT analysis and synthesis filter bank, one after the other, for time measurement
#Gerald Schuller, November 2017

from keras_MDCTanalysis import *
from keras_MDCTsynthesis import *
from sound import sound
import time

N=1024 #Number of filters, stride
filtlen=2048 #Length of filter impulse response
modelana = generate_model_ana(N,filtlen)     # Compile an neural net analysis filter bank
modelsyn = generate_model_syn(N,filtlen)     # " Synthesis filter bank

#Test Perfect reconstruction and Delay:
X=np.arange(20*N)
a=time.time()
Y=keras_MDCT_ana(X,modelana)
b=time.time()
xrek= keras_MDCT_syn(Y,modelsyn)
c=time.time()
print("Analysis time:", b-a)
print("Synthesis time:", c-b)
#Plots reconstructed ramp if ok:
#print("xrek.shape=", xrek.shape)
#print("xrek=", xrek)
plt.plot(X)
plt.plot(xrek)
plt.legend(('Original', 'Reconstructed'))
plt.title("Original and Recontructed Test Signal")
plt.show()
#It shows no delay between original and reconstructed signal!

fs, X= wav.read('test.wav')
print("fs=", fs)
X=X*1.0/2**15
startime=time.time()
#Analysis Filter Bank:
Y=keras_MDCT_ana(X,modelana) 
#Synthesis Filter Bank:
xrek= keras_MDCT_syn(Y,modelsyn)
endtime=time.time()
print("Duration analysis-synthesis: ", endtime-startime)
os.system('espeak -ven -s 120 '+'"The output of the synthesis MDCT"')
sound(2**15*xrek,fs)


