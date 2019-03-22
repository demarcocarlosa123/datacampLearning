import scipy.io

filename = 'files/ja_data2.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))