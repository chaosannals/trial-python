import os
import json
import numpy as np
from scipy.special import expit

class NumNeuralNetwork:
    '''
    
    '''

    def __init__(
        self,
        model_path='nnn_model.json',
        input_shape=3,
        hidden_shape=3,
        output_shape=3,
        learning_rate = 0.004,
    ):
        '''
        
        '''

        self.model_path=model_path

        # 模型存在就读取，否则就初始化。
        if os.path.exists(self.model_path):
            with open(self.model_path, 'r', encoding='utf8') as reader:
                data = json.load(reader)
                self.input_shape = data['input_shape']
                self.hidden_shape = data['hidden_shape']
                self.hidden_weight = np.array(data['hidden_weight'])
                self.output_shape = data['output_shape']
                self.output_weight = np.array(data['output_weight'])
                self.learning_rate = data['learning_rate']
        else:
            self.input_shape = input_shape
            self.hidden_shape = hidden_shape
            self.output_shape = output_shape
            self.learning_rate = learning_rate
            # 简单随机初始
            # self.hidden_weight = np.random.rand(hidden_shape, input_shape) - 0.5
            # self.output_weight = np.random.rand(output_shape, hidden_shape) - 0.5

            # 复杂正态初始
            self.hidden_weight = np.random.normal(0.0, pow(hidden_shape, -0.5), (hidden_shape, input_shape))
            self.output_weight = np.random.normal(0.0, pow(output_shape, -0.5), (output_shape, hidden_shape))

        self.activation_function = lambda x: expit(x)

    def train(self, x, t):
        '''
        
        '''
        inputs = np.array(x, ndmin=2).T
        hidden_outputs, final_outputs = self.foreward(inputs)
        targets = np.array(t, ndmin=2).T
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.output_weight.T, output_errors)

        self.output_weight += self.learning_rate * np.dot(output_errors * final_outputs * (1.0 - final_outputs), hidden_outputs.T)
        self.hidden_weight += self.learning_rate * np.dot(hidden_errors * hidden_outputs * (1.0 - hidden_outputs), inputs.T)
        
        return output_errors


    def query(self, x):
        '''
        
        '''
        inputs = np.array(x, ndmin=2).T
        _, oo = self.foreward(inputs)
        return oo

    def foreward(self, inputs):
        '''
        
        '''

        hidden_input = np.dot(self.hidden_weight, inputs)
        hidden_output = self.activation_function(hidden_input)
        final_input = np.dot(self.output_weight, hidden_output)
        final_output = self.activation_function(final_input)
        return hidden_output, final_output

    def save(self):
        '''
        
        '''

        with open(self.model_path, 'w', encoding='utf8') as writer:
            data = {
                'input_shape': self.input_shape,
                'hidden_shape': self.hidden_shape,
                'hidden_weight': self.hidden_weight.tolist(),
                'output_shape': self.output_shape,
                'output_weight': self.output_weight.tolist(),
                'learning_rate': self.learning_rate
            }
            json.dump(data, writer)