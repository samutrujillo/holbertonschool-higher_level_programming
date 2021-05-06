#include "lists.h"
/**
* is_palindrome - frees a listint_t list
* @head: pointer to list to be freed
* Return: 1 if it is palidrome, 0 if it is not
*/
int is_palindrome(listint_t **head)
{
	int len = 0, i;
	listint_t *h;
	int aux[1000000];

	h = *head;
	if (!h)
		return (1);
	while (h)
	{
		aux[len] = h->n;
		h = h->next;
		len++;
	}
	for (i = 0; i < len; i++)
	{
		if (aux[i] != aux[len - 1 - i])
			return (0);
	}
	return (1);
}