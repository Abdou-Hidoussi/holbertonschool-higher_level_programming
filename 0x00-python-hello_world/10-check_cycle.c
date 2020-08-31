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
	if (list == NULL || (*list).next == NULL)
		return (0);
	while ((*tmp).next != NULL && (*tmp).next != list)
	{
		tmp = (*tmp).next;
	}
	if ((*tmp).next == list)
		return (1);
	if ((*tmp).next == NULL)
		return (0);
	return (check_cycle((*list).next));
}
