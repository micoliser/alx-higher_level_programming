#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: pointer to list
 *
 * Return: 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *temp2 = *head;
	int length, *list_arr, i;

	if (!(*head))
		return (1);

	for (length = 0; temp2; length++)
		temp2 = temp2->next;

	list_arr = malloc(sizeof(int) * length);
	if (!list_arr)
		exit(100);

	for (i = 0; temp; temp = temp->next, i++)
		list_arr[i] = temp->n;

	for (i = 0; i < (length / 2); i++, length--)
	{
		if (list_arr[i] != list_arr[length - 1])
			return (0);
	}

	return (1);
}
