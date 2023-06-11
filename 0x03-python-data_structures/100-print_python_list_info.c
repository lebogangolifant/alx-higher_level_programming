#include <Python.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 *
 * @p: Pointer to the Python list object to be analyzed.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, index;
	PyObject *obj;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (index = 0; index < size; index++)
    {
        obj = PyList_GetItem(p, index);
        printf("Element %ld: %s\n", index, Py_TYPE(obj)->tp_name);
    }
}

