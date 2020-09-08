#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - test list palindrom
 * @head: pointer to list to be tested
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *a, *b, *h;

	a = *head;
	b = *head;
	if (a == NULL || (*a).next == NULL)
	{
		return (1);
	}
	while ((*b).next)
	{
		b = (*b).next;
	}
	while ((*a).n == (*b).n)
	{
		if ((*a).next == b || (*a).next == (*b).next)
		{
			return (1);
		}
		a = (*a).next;
		h = b;
		b = *head;
		while ((*b).next != h)
		{
			b = (*b).next;
		}
	}
	return (0);
}
