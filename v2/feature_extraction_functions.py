import librosa as lb
import numpy as np


def spectrogram_feature_extractor(path):
    data, sample_rate = lb.load(path, res_type='kaiser_fast')
    spectrogram = np.abs(lb.stft(data, n_fft=128))**2           #diff is in the power to 2, amplifies higher magintude values and suppresses lower ones
    spectrogram_features = np.mean(spectrogram, axis=1)
    return spectrogram_features

def lfcc_feature_extractor(path):
    data, sample_rate = lb.load(path, res_type='kaiser_fast')
    lfcc = lb.feature.mfcc(data, n_mfcc=128, dct_type=3)
    lfcc_features = np.mean(lfcc, axis=1)
    return lfcc_features

def mfcc_feature_extractor(path):
    data, simple_rate = lb.load(path, res_type='kaiser_fast')
    data = lb.feature.mfcc(data, n_mfcc=128)
    data = np.mean(data,axis=1)
    return data

# Doesn't make sense to do DFT since its outdated version of stft but we can
def stft_feature_extractor(path):
    data, sample_rate = lb.load(path, res_type='kaiser_fast')
    stft = np.abs(lb.stft(data, n_fft=128))
    stft_features = np.mean(stft, axis=1)
    return stft_features

# FTT feature extracter - Om J
def ftt_feature_extractor(path):
    data, sample_rate = lb.load(path, res_type='kaiser_fast')
    ftt = np.abs(lb.ftt(data, n_fft=128))
    ftt_features = np.mean(ftt, axis=1)
    return ftt_features

# Constant Q Transform feature extracter - Om J
def cq_feature_extractor(path):
    data, sample_rate = lb.load(path, res_type='kaiser_fast')
    cq = np.abs(lb.cqt(data, n_fft=128))
    cq_features = np.mean(cq, axis=1)
    return cq_features