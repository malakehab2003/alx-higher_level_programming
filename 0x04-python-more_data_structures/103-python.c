#include <Python.h>

void print_python_list(PyObject *p)
{
  int i;
  Py_ssize_t size;

  if (!PyList_Check(p)) {
    printf("[ERROR] Invalid List Object\n");
    return;
  }

  size = PyList_Size(p);
  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %d\n", size);
  printf("[*] Allocated = %d\n", PyList_GetAllocated(p));

  for (i = 0; i < size; i++) {
    PyObject *item = PyList_GetItem(p, i);
    printf("Element %d: ", i);

    if (PyBytes_Check(item)) {
      printf("bytes\n");
      print_python_bytes(item);
    } else if (PyInt_Check(item)) {
      printf("int\n");
    } else if (PyFloat_Check(item)) {
      printf("float\n");
    } else if (PyTuple_Check(item)) {
      printf("tuple\n");
    } else if (PyList_Check(item)) {
      printf("list\n");
    } else {
      printf("other\n");
    }
  }
}

void print_python_bytes(PyObject *p)
{
  Py_ssize_t size;
  char *string;

  if (!PyBytes_Check(p)) {
    printf("[ERROR] Invalid Bytes Object\n");
    return;
  }

  size = PyBytes_Size(p);
  string = PyBytes_AS_STRING(p);

  printf("[.] bytes object info\n");
  printf("  size: %d\n", size);
  printf("  trying string: %s\n", string);
  printf("  first %d bytes: ", size > 10 ? 10 : size);

  for (int i = 0; i < (size > 10 ? 10 : size); i++) {
    printf("%02hhx ", string[i]);
  }

  printf("\n");
}

