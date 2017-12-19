import time
import numpy as np
import tensorflow as tf

# from grpc.beta import implementations
# from tensorflow_serving.apis import predict_pb2
# from tensorflow_serving.apis import prediction_service_pb2

from .export_model import make_network


# class ModelAPI(object):
#     def __init__(self, host, port):
#         channel = implementations.insecure_channel(host, int(port))
#         self.stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)
#
#     def predict(self, feature):
#         request = predict_pb2.PredictRequest()
#         request.model_spec.name = 'default'
#         request.model_spec.signature_name = 'predict'
#         request.inputs['data'].CopyFrom(tf.contrib.util.make_tensor_proto(feature))
#         result = self.stub.Predict(request, 10.0)
#         prediction = np.array(result.outputs['feature'].float_val)
#         return prediction


# if __name__ == '__main__':
#     input_shape = (500, 500, 3)
#     image = np.random.random(input_shape).astype(np.float32)
#
#     # test tensorflow model service prediction
#     # client_api = ModelAPI('0.0.0.0', 9001)
#     client_api.predict(image)  # first request to init model
#     tick = time.time()
#     [client_api.predict(image) for i in range(10)]
#     print 'TF model service: ', (time.time() - tick) / 10.
#
#     # test raw tensorflow model inference
#     feature = tf.placeholder(tf.float32, input_shape)
#     predictions = make_network(tf.expand_dims(feature, 0))
#
#     with tf.Session() as sess:
#         sess.run(tf.global_variables_initializer())
#         sess.run(predictions, feed_dict={feature: image})  # first request to init model
#         tick = time.time()
#         [sess.run(predictions, feed_dict={feature: image}) for i in range(10)]
#         print 'Raw TF model inference: ', (time.time() - tick) / 10.
