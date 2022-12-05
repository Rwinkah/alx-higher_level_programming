#include "lists.h"

/**
 * insert_node - insert a node to a linked list 
 *
 * @head: beginning of the list
 * @number: content of the new node
 *
 **/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));
listint_t *temp = *head;
while (temp->next != NULL)
{
temp = temp->next; 
}
new_node->n = number;
new_node->next = NULL;

temp->next = new_node;

return(new_node);
}
