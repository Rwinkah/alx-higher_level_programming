#include "lists.h"

/**
 * check_cycle - check whether a linked list has a cycle
 *
 * @list: start of the list
 *
 * Return: int
**/

int check_cycle(listint_t *list)
{
listint_t *temp = malloc(sizeof(listint_t));
temp = list;

if (list == NULL)
{
return (0);
}

while (1)
{
if (temp->next == list)
{
	return (1);
}
else if (temp->next == NULL)
{
	break;
}
temp = temp->next;
}

free(temp);
return (0);
}
