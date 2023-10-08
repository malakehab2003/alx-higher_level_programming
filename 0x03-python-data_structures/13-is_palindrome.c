#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if function is palindorome
 *
 * Return: 1 if palindrome
 *
 * @head: the first point in the list to check
*/

int is_palindrome(listint_t **head)
{
	int count = 0, i = 0, j = 0, arr[50];
	listint_t *new;

	new = *head;
	if (*head == NULL)
		return (1);
	while (new != NULL)
	{
		count++;
		new = new->next;
	}

	new = *head;
	for (; i < count; i++)
	{
		arr[i] = new->n;
		new = new->next;
	}

	i--;
	for (; j < (count / 2); j++, i--)
	{
		if (arr[j] != arr[i])
			return (0);
	}
	return (1);
}
