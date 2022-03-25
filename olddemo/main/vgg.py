import tensorflow as tf

def convolute(t, s, kh, kw, n_out, dh, dw, p):
    n_in = t.get_shape()[-1].value
    with tf.name_scope(s) as scope:
        kernel = tf.compat.v1.get_variable(
            scope+"w",
            shape=[kh,kw,n_in,n_out],
            dtype=tf.float32,
            initializer=
        )