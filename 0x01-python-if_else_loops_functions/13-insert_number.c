#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - insert a node in sorted list
 *
 * Return: the address of the added node
 *
 * @head: the head of the linked list
 *
 * @number: the number of the added node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *itr, *slowitr;

	itr = (*head)->next;
	slowitr = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new = *head;
		(*head)->next = NULL;
	}
	while (itr != NULL)
	{
		if (number <= (*head)->n)
		{
			new->next = *head;
			*head = new;
			return (*head);
		}
		else if (itr->n >= number)
		{
			slowitr->next = new;
			new->next = itr;
			return (new);
		}
		itr = itr->next;
		slowitr = slowitr->next;
	}
	slowitr->next = new;
	new->next = NULL;
	return (new);
}
