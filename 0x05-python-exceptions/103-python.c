#include <Python.h>

/**
 * print_python_list - Print basic information about a Python list object.
 * @p: The PyObject representing the Python list.
 */

void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");

	Py_ssize_t size = PyObject_Length(p);

	if (size < 0)
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		PyObject *type = PyObject_Type(item);
		const char *typeName = Py_TYPE(type)->tp_name;

		printf("Element %ld: %s\n", i, typeName);

		Py_DECREF(type);
	}
}

/**
 * print_python_bytes - Print basic information about a Python bytes object
 * @p: The PyObject representing the Python bytes
 */

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	Py_ssize_t size = PyObject_Length(p);

	if (size < 0)
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("Size of the bytes object = %ld\n", size);

	char *data = NULL;
	PyBytesObject *bytesObject = (PyBytesObject *)p;

	if (PyBytes_Check(p))
		data = PyBytes_AS_STRING(bytesObject);

	printf("First %ld bytes: ", (size > 10 ? 10 : size));
	if (data)
	{
		for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
		{
			printf("%02x", (unsigned char)data[i]);
		}
	}

	printf("\n");
}

/**
 * print_python_float - Print basic information about a Python float object
 * @p: The PyObject representing the Python float
 */

void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");

	if (PyFloat_Check(p))
	{
		double value = PyFloat_AS_DOUBLE(p);

		printf("Value: %f\n", value);
	} else
	{
		printf("[ERROR] Invalid Float Object\n");
	}
}
