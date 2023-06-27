#include "Python.h"

/**
 * print_python_list - Print basic information about a Python list object.
 * @p: The PyObject representing the Python list.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n  [ERROR]
				Invalid List Object\n");
		fflush(stdout);
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}

	fflush(stdout);
}

/**
 * print_python_bytes - Print basic information about a Python bytes object
 * @p: The PyObject representing the Python bytes
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes_str;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n
				[ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	size = PyBytes_Size(p);
	bytes_str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", bytes_str);

	printf("  first %zd bytes: ", size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf("%.2hhx ", bytes_str[i]);
	}

	printf("\n");
	fflush(stdout);
}

/**
 * print_python_float - Print basic information about a Python float object
 * @p: The PyObject representing the Python float
 */

void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n
				[ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}

	value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
	fflush(stdout);
}
