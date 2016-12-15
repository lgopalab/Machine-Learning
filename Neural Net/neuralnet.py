import numpy as np


class NeuralNet:
    def __init__(self, input_size, hidden_size, out_size, learning_factor, input_matrix, input_values, test_matrix, test_values):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.out_size = out_size
        self.learning_factor = learning_factor
        self.input_matrix = input_matrix
        self.input_vals = input_values
        self.test_matrix = test_matrix
        self.test_vals = test_values
        self.hidden_vector = np.zeros(self.hidden_size)
        self.out_vect = np.zeros(self.out_size)
        self.layer1_weights = np.random.randn(self.input_size, self.hidden_size)
        self.layer2_weights = np.random.randn(self.hidden_size, self.out_size)
        self.strin = ""

    def feed(self, index, train=True):
        if train:
            input_matrix_reshaped = np.reshape(self.input_matrix[index], (1, self.input_size))
        else:
            input_matrix_reshaped = np.reshape(self.test_matrix[index], (1, self.input_size))

        hidden_result = input_matrix_reshaped.dot(self.layer1_weights)
        hidden_result = self.sigmoid_function(hidden_result)

        output_result = hidden_result.dot(self.layer2_weights)
        output_result = self.sigmoid_function(output_result)

        self.input_vector = input_matrix_reshaped
        self.hidden_vector = hidden_result
        self.output_vector = output_result

    def train(self, epochs):
        for i in range(epochs):
            for mat_index in range(len(self.input_matrix)):
                self.feed(mat_index)

                expected_vector = np.zeros(self.out_size)
                expected_vector[self.input_vals[mat_index]] = 1.0

                out_err_vect = (expected_vector - self.output_vector) * self.output_vector * (1.0 - self.output_vector)

                hidden_err = self.layer2_weights.dot(out_err_vect.transpose())
                hidden_err = hidden_err * (self.hidden_vector.transpose()) * (1.0 - self.hidden_vector.transpose())

                layer2_delta = self.hidden_vector.transpose().dot(out_err_vect)
                layer1_delta = (hidden_err.dot(self.input_v+
                                               ector)).transpose()

                self.layer1_weights = self.layer1_weights + (layer1_delta * self.learning_factor)
                self.layer2_weights = self.layer2_weights + (layer2_delta * self.learning_factor)

    def test(self):
        predict_correct = 0
        for i in range(len(self.test_matrix)):
            self.feed(i, False)
            out_list = self.output_vector.tolist()[0]
            maxindex = out_list.index(max(out_list))
            if maxindex == self.test_vals[i]:
                predict_correct += 1
        print "\n_________________________________________________"
        print "Report"
        print "_________________________________________________"
        print "Correctly predicted: %d" % predict_correct
        print "over a sample of %d" % (len(self.test_matrix))
        print "Accuracy: %.06f \n \n" % (predict_correct * 100.0 / (len(self.test_matrix)))
        self.strin += ",{0},{1},{2}".format(predict_correct,(len(self.test_matrix)),(predict_correct * 100.0 / (len(self.test_matrix))))
        return self.strin

    def sigmoid_function(self, x):
        res = 1.0 / (1 + np.e ** (-x))
        return res


def read_inputs(filename, size):
    file_read = open(filename, 'r')
    file_text = file_read.read()
    file_read.close()
    file_text = file_text.replace('\n', ' ')
    file_text = file_text.replace(',', ' ')
    l = file_text.split(' ')
    for k in range(l.count('')):
        l.remove('')
    l = [int(i) for i in l]
    matrices = []
    num_list = []
    for i in range(size):
        temp = l[i * 65:(i + 1) * 65]
        num_list.append(temp.pop())
        mat = []
        for ind in range(1, 9):
            mat.append(temp[8 * (ind - 1):8 * ind])
        matrices.append(mat)
    return matrices, num_list

def main():

    #Defines input parameters here.
    INPUT_SIZE = 8 ** 2
    HIDDEN_SIZE = 38
    OUT_SIZE = 10
    LEARNING_FACTOR = .1
    TRAINING_SIZE = 3500
    TESTING_SIZE = 1500
    EPOCHS = 100
    str1=""
    str2=""
    str3=""

    train_matrices, train_num = read_inputs("optdigits_training.csv", TRAINING_SIZE)
    test_matrices, test_num = read_inputs("optdigits_test.csv", TESTING_SIZE)

    for i in (4,6,8,10,12,14,16,18,20,24,28,32,36,40):
        print "Learning factor 0.2"
        print "Hidden layer %d"%i
        print "Epochs 50"
        str1 = "0.2,{0},50".format(i)
        nn = NeuralNet(INPUT_SIZE, i, OUT_SIZE, 0.3, train_matrices, train_num, test_matrices, test_num)
        nn.train(50)
        str2 = nn.test()
        str3 += str1+str2+"\n"

    text_file = open("Output.txt", "w")
    text_file.write(str3)
    text_file.close()

if __name__ == "__main__":
    main()
