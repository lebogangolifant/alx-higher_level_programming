#include <Python.h>

/**
 * print_python_list - Prints basic information about a Python list.
 * @p: The Python list object.
 */

void print_python_list(PyObject *p) {
    Py_ssize_t size, index;
    PyObject *item;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (index = 0; index < size; index++) {
        item = PyList_GetItem(p, index);
        printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object.
 * @p: The Python bytes object.
 */

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, index;
    unsigned char *bytes;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes);

    printf("  first 10 bytes:");
    for (index = 0; index < size && index < 10; index++)
        printf(" %02x", bytes[index]);
    printf("\n");
}
