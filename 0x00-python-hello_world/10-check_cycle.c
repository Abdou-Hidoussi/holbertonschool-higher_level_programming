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

	tmp = list;

	while ((*tmp).next != NULL && (*tmp).next != list)
	{
		tmp = (*tmp).next;
	}
	if ((*tmp).next == list)
	{
		return (1);
	}
	return (0);
}
