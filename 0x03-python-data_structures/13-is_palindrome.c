#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - function
 * @head: header
 * Return: 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp1, *tmp2;
	int i, size = 0;

	if (!head)
		return (0);
	if (!*head)
		return (1);
	tmp1 = tmp2 = *head;
	while (tmp2)
	{
		tmp2 = tmp2->next;
		size++;
	}
	while (tmp1->next)
	{
		tmp2 = *head;
		i =  0;
		while (i < size - 1)
		{
			tmp2 = tmp2->next;
			i++;
		}
		if (tmp1->n != tmp2->n)
			return (0);
		tmp1 = tmp1->next;
		size--;
	}
	return (1);
}