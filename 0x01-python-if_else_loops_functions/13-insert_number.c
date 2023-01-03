#include "lists.h"

/**
 * insert_node - inserts a number in a srted linked list
 * @head: head of the list
 * @number: number to be inserted
 *
 * Return: new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *list, *temp2;

	list = malloc(sizeof(listint_t));
	if (!list)
		return (NULL);

	list->n = number;
	
	while (temp->next)
	{
		if (temp->next->n >= number)
		{
			temp2 = temp->next;
			temp->next = list;
			list->next = temp2;
			return (list);
		}
		temp = temp->next;
	}

	temp->next = list;
	list->next = NULL;

	return (list);
}
