#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - check for cycle
 * @list: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL || (*list).next == NULL)
		return (0);
	tmp = list;

	while ((*tmp).next != NULL && (*tmp).next != list)
	{
		if ((*tmp).next == list)
			return (1);
		tmp = (*tmp).next;
	}
	return (0);
}
