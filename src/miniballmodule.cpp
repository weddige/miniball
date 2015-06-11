#include <Python.h>
#include "Miniball.hpp"

static PyObject * miniball_miniball(PyObject *self, PyObject *args)
{
  // Convert input to C++
  PyObject *list;
  if (!PyArg_ParseTuple(args, "O", &list))
    return NULL;

  PyObject *iter = PyObject_GetIter(list);
  if (!iter)
    return NULL;

  double** points = new double*[PyObject_Size(list)];

  PyObject *next = PyIter_Next(iter);
  int i = 0;
  int dimension = PyObject_Size(next); // TODO: Some integrity checks
  while (next) {
    PyObject *point_iter = PyObject_GetIter(next);
    points[i] = new double[dimension];
    PyObject *x = PyIter_Next(point_iter);
    int n = 0;
    while (x) {
      double xx = PyFloat_AsDouble(x);
      points[i][n] = xx;
      x = PyIter_Next(point_iter);
      n++;
    }
    next = PyIter_Next(iter);
    i++;
  }
  // Do the math
  typedef double* const* PointIterator;
  typedef const double* CoordIterator;

  typedef Miniball::
    Miniball <Miniball::CoordAccessor<PointIterator, CoordIterator> >
    MB;

  MB mb(dimension, points, points+i);

  const double* center = mb.center();

  // Convert result to python
  PyObject *result = PyList_New(dimension);
  for (int n = 0; n < dimension; n++)
    PyList_SetItem(result, n, PyFloat_FromDouble(center[n]));

  return result;
}

static PyMethodDef MiniballMethods[] = {
  {"miniball", miniball_miniball, METH_VARARGS, "Compute miniball"},
  {NULL, NULL, 0, NULL},
};

static struct PyModuleDef miniballmodule = {
  PyModuleDef_HEAD_INIT,
  "miniball",
  "Python bindings to Bernd Gaertners miniball software (V3.0)",
  -1,
  MiniballMethods
};

PyMODINIT_FUNC PyInit_miniball(void)
{
  return PyModule_Create(&miniballmodule);
}
