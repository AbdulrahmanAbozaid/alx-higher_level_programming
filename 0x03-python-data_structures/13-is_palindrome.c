#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

/**
 * is_palindrome - fsaff
 * @head: dasfas
 * Return: fafsaf
 */

int is_palindrome(listint_t **head)
{
	int *nums, len = 0, i = 0;
	listint_t *l = *head;

	if (!head || !*head)
		return (1);
	while (l)
	{
		len++;
		l = l->next;
	}

	nums = malloc(sizeof(int) * len);
	l = *head;
	while (i < len / 2)
	{
		*nums = l->n;
		i++;
		nums++;
		l = l->next;
	}

	i--;
	nums--;
	if (len % 2 != 0)
		l = l->next;

	while (i >= 0)
	{
		if (l->n != *nums)
		{
			return (0);
		}
		l = l->next;
		i--;
		nums--;
	}

	return (1);
}
