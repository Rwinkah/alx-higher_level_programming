#include <stdio.h>
#include <Python.h>


/**
* print_python_bytes - Prints bytes information
*
* @p: Python Object
*
* Return: void
**/
\

void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, lmt

	printf("[.] bytes object info")
	if (!PyBytes_check(p))
	{
		printf(" [ERROR] Invalid Bytes Object")
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = (PyBytesObject *)p)->ob_sval;

	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", string);

	if (size >= 10)
		lmt = 10;
	else
		lmt = size + 1;
	printf(" first %ld bytes:", lmt);

	for (i = 0; i < lmt; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i];
		else
			printf(" %02x", 256 + string[i]);
	printf("\n");
}





/**
 * print_python_list - print infor about python objects
 *
 * @p: pointer to the python object
 *
 * Return: voif
 **/

void print_python_list(Pyobject *p)
{
	char *str;
	PyListObject *obj;
	long int size, i;
	
	obj = (PyListObject *)p;
	size = PyList_Size(obj);	

	printf("[.] Python list info");
	printf("[*] Size of the Python List = %ld", size);
	printf("[*] Allocated = %ld", obj->allocated);
	
	for(i = 0;, i < size; i++)
	{
		printf("Element %ld: %s\n", i, (obj->ob_item[i])->ob_type->tp_name);
		if (PyBytes_Check(obj))
		{
			print_python_bytes(obj);
		}
	}
}
