import time
import tensorflow as tf
import tensorflow.contrib.layers as tfl


def make_network(features):
    x = features
    x = tfl.conv2d(x, 32, 3)
    x = tfl.conv2d(x, 32, 3)
    x = tfl.conv2d(x, 32, 3)
    x = tfl.conv2d(x, 1, 1)  # remove this and check difference
    return x


if __name__ == '__main__':
    model_input = tf.placeholder(tf.float32, [500, 500, 3])
    model_output = make_network(tf.expand_dims(model_input, 0))

    # create session and initialize model weights
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    model_input = tf.saved_model.utils.build_tensor_info(model_input)
    model_output = tf.saved_model.utils.build_tensor_info(model_output[0])
    prediction_signature = tf.saved_model.signature_def_utils.build_signature_def(
        inputs={'data': model_input},
        outputs={'feature': model_output},
        method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME)

    export_path = './tf_service_testing/served_models/%s' % (str(time.time()).split('.')[0])
    builder = tf.saved_model.builder.SavedModelBuilder(export_path)
    legacy_init_op = tf.group(tf.tables_initializer())
    builder.add_meta_graph_and_variables(
        sess=sess,
        tags=[tf.saved_model.tag_constants.SERVING],
        signature_def_map={'predict': prediction_signature},
        legacy_init_op=legacy_init_op)

    builder.save()
