# Pseudo Quadrature Mirror Filter Bank Implementation using Python Keras 

Simple programs to use a keras convolutional neural network as implementation of a PQMF filter bank. For background on it, see:
https://ccrma.stanford.edu/~jos/sasp/Pseudo_QMF_Cosine_Modulation_Filter.html
Book:  Spanias, Painter: “Audio Signal Processing and Coding”, Wiley Press
and our lecture Audio Coding, 
https://www.tu-ilmenau.de/mt/lehrveranstaltungen/lehre-fuer-master-mt/audio-coding/
slides lecture 07.

PQMF filter banks have longer filters than MDCT filter banks with the same number of subbands, hence have (and need) a higher stopbband attenuation, but at the expense of a higher system delay (over the analysis and synthesis filter bank), and have only a near perfect reconstruction, which means there is always a reconstruction error, although hopefully very small (for that the high stopband attenuation is needed).

The advantages of a Keras implemenation are: 
* The possibility to use the GPU in this way and speed up the computation, 
* hence it might not need a specialized fast implementation,
* It can be easily integrated in Keras programs, for instance for source separation, or as a starting point for further optimization or training.

## Getting Started
In the "main" section of the PQMF programs, the variable N=64 is the number of subbands of the Low Delay Filter Bank. The function PQMF_init reads the prototype filter coefficients from the file "qmf.dat".

The analysis program keras_PQMFanalysis.py reads in a sound file, for instance the "test.wav" file. In Keras the different subbands appear in its "channels" dimension.
The program writes the subband signals into the file "pqmf_subbands.pickle".
The synthesis program keras\_PQMFsynthesis.py reads in the file "pqmf\_subbands.pickle" and plays back the reconstructed sound, using pyaudio.
The program keras\_PQMFanasyn.py calls the analysis and synthesis programs in a sequence.

To start, simply execute:
python keras\_PQMFanasyn.py

Gerald Schuller, February 2018

