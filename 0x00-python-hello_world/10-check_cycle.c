#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
        listint_t *new;
        new = list;

        while (new != NULL && new->next != NULL)
        {
                if (new->next == new)
                {
                        return (1);
                }
                new = new->next;
        }
        return (0);
}
