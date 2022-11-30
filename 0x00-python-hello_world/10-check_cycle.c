#include "lists.h"

int check_cycle(listint_t *list)
{
listint_t *temp = malloc(sizeof(listint_t));
temp = list;

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

return (0);
}
