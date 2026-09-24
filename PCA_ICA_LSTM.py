# Model architecture of the proposed model PCA-ICA-LSTM
from keras.layers import Dense,Dropout,BatchNormalization,LSTM,Flatten
from keras.models import Sequential
from sklearn.decomposition import PCA
from sklearn.decomposition import FastICA

number_of_components=12

pca = PCA(n_components=number_of_components)
pca.fit(training_set)
tra_set = pca.transform(training_set)
tes_set = pca.transform(testing_set)
val_set = pca.transform(validation_set)

ica = FastICA()
ica.fit(tra_set)
training_SET = ica.transform(tra_set)
testing_SET = ica.transform(tes_set)
validation_SET = ica.transform(val_set)


m_training_data,m_train_y,m_train_current=reshape(training_SET,training_result.values,training_current.values,5)
m_testing_data,m_test_y,m_test_current=reshape(testing_SET,testing_result.values,testing_current.values,5)
m_validation_data,m_val_y,m_valid_current=reshape(validation_SET,validation_result.values,validation_current.values,5)


model = Sequential()
model.add(LSTM(64,activation='linear',return_sequences=True, input_shape=(m_training_data.shape[1],m_training_data.shape[2])))
model.add(Dropout(0.3))
model.add(LSTM(128,activation='linear',return_sequences=True,input_shape=(m_training_data.shape[1],m_training_data.shape[2])))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(256,activation='linear',kernel_initializer='he_normal'))
model.add(Dropout(0.3))
model.add(Dense(512,activation='linear',kernel_initializer='he_normal'))
model.add(Dropout(0.3))
model.add(Dense(1,activation='linear',kernel_initializer='he_normal'))

model.summary()