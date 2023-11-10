#include <Python.h>

/**
 * print_python_bytes - Print basic info about Python bytes objects
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p) {
    ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first 10 bytes:");

    for (i = 0; i < size && i < 10; ++i) {
        printf(" %02x", (unsigned char)str[i]);
    }

    printf("\n");
}

/**
 * print_python_list - Print basic info about Python lists
 * @p: PyObject representing a Python list object
 */
void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    ssize_t size, allocated, i;
    PyObject *item;

    printf("[*] Python list info\n");

    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    allocated = Py_SIZE(list);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; ++i) {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(item)) {
            printf("bytes\n");
            print_python_bytes(item);
        } else if (PyFloat_Check(item)) {
            printf("float\n");
        } else if (PyTuple_Check(item)) {
            printf("tuple\n");
        } else if (PyList_Check(item)) {
            printf("list\n");
            print_python_list(item);
        } else if (PyLong_Check(item)) {
            printf("int\n");
        } else if (PyUnicode_Check(item)) {
            printf("str\n");
        }
    }
}
