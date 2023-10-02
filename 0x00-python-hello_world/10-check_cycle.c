#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
  listint_t *new;

  if (list == NULL) {
    return 0;
  }

  new = list;

  while (new != NULL && new->next != NULL) {
    if (new == NULL || new->next == NULL) {
      return 0;
    }

    if (new == new->next) {
      return 1;
    }

    new = new->next;
  }

  return 0;
}

