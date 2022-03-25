#include"pch.h"
#include<Python.h>

static PyObject* SpamError;

static PyObject *say_hello(PyObject * self, PyObject * args) {
	Py_RETURN_NONE;
}

static PyMethodDef module_methods[] = {
	{ "say_hello", (PyCFunction)say_hello, METH_VARARGS, NULL },
	{ NULL, NULL, 0, NULL},
};

static struct PyModuleDef module_def = {
	PyModuleDef_HEAD_INIT,
	"hello",
	"hello yet a library",
	-1,
	module_methods
};

PyMODINIT_FUNC PyInit_hello() {
	return PyModule_Create(&module_def);
}