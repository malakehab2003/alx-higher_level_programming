
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
/**
int is_palindrome(listint_t **head)
{
	int count = 0, i = 0, j, countcp = 0, half = 0;
	listint_t *new, *last;

	new = *head;
	last = *head;
	if (*head == NULL)
		return (1);
	while (new != NULL)
	{
		count++;
		new = new->next;
	}
	countcp = count - 1;
	new = *head;
	half = count / 2;

	for (; i <= half; i++)
	{
		for (j = 0; j < countcp; j++)
		{
			last = last->next;
		}
		countcp--;
		if (new->n != last->n)
		{
			return (0);
		}
		last = *head;
		new = new->next;
	}
	return (1);
}
*/
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        listint_t *next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    if (fast != NULL)
        slow = slow->next;

    while (slow != NULL)
    {
        if (prev->n != slow->n)
            return (0);

        prev = prev->next;
        slow = slow->next;
    }

    return (1);
}
